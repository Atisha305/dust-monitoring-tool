# Dust Monitoring & Control System (Python)

"""
Objective: Studied dust levels in mining areas to propose control strategies for safer and sustainable operations.

This tool:
- Takes in PM10/PM2.5 air quality data (CSV)
- Identifies high-risk periods/zones using CPCB thresholds
- Suggests control actions (sprinkling/fog/greenbelt)
- Visualizes dust trend graphs for reports

Useful for mine safety planning and sustainability audit support.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sample air quality dataset (timestamp, PM10, PM2.5)
filename = "dust_data.csv"
if not os.path.exists(filename):
    print("Error: dust_data.csv not found. Please place the file in the working directory.")
else:
    data = pd.read_csv(filename)

    # Check for necessary columns
    if 'Time' not in data.columns or 'PM10' not in data.columns or 'PM2.5' not in data.columns:
        print("Error: CSV must contain 'Time', 'PM10', and 'PM2.5' columns.")
    else:
        # CPCB limits
        PM10_limit = 100  # µg/m³
        PM25_limit = 60   # µg/m³

        # Flag high dust events
        data['PM10_High'] = data['PM10'] > PM10_limit
        data['PM25_High'] = data['PM2.5'] > PM25_limit

        # Summary
        high_pm10_hours = data['PM10_High'].sum()
        high_pm25_hours = data['PM25_High'].sum()
        print(f"✅ PM10 exceeded in {high_pm10_hours} time slots")
        print(f"✅ PM2.5 exceeded in {high_pm25_hours} time slots")

        # Recommendation logic
        if high_pm10_hours > 10:
            print("🔧 Suggest sprinkling or fog system during high PM10 hours.")
        if high_pm25_hours > 10:
            print("🌱 Consider greenbelt buffer or misting units to reduce PM2.5.")

        print("\n📊 Showing dust trend visualization...")

        # Plotting
        plt.figure(figsize=(12,6))
        plt.plot(data['Time'], data['PM10'], label='PM10', color='orange')
        plt.plot(data['Time'], data['PM2.5'], label='PM2.5', color='green')
        plt.axhline(PM10_limit, color='red', linestyle='--', label='PM10 Limit')
        plt.axhline(PM25_limit, color='blue', linestyle='--', label='PM2.5 Limit')
        plt.xlabel("Time")
        plt.ylabel("Concentration (µg/m³)")
        plt.title("Dust Level Monitoring")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("dust_sample_output.png")
        plt.show()

        print("✅ Analysis complete.")
