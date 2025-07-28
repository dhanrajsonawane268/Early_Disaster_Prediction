# ✅ File: csv_reader.py
import csv

def read_latest_input():
    try:
        with open("latest_input.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                temperature = float(row["Temperature"])
                humidity = float(row["Humidity"])
                wind_speed = float(row["Wind Speed"])
                soil_moisture = float(row["Soil Moisture"])
                return [temperature, humidity, wind_speed, soil_moisture]
    except Exception as e:
        print("Error reading CSV:", e)
        return None
