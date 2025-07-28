import csv
from app.predict import predict_disaster  # jar path vegla asel tar import adjust kara
import os

def get_user_input():
    while True:
        try:
            rainfall = float(input("🌧 Rainfall (mm): "))
            temperature = float(input("🌡 Temperature (°C): "))
            humidity = float(input("💧 Humidity (%): "))
            return rainfall, temperature, humidity
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.\n")

def log_data_to_csv(rainfall, temperature, humidity, result):
    file_exists = os.path.isfile("data_log.csv")
    with open("data_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Rainfall", "Temperature", "Humidity", "Prediction"])
        writer.writerow([rainfall, temperature, humidity, result])

def main():
    print("\n🌍 Welcome to Early Disaster Predictor!")
    while True:
        rainfall, temperature, humidity = get_user_input()
        result = predict_disaster(rainfall, temperature, humidity)
        print(f"\n📢 Prediction Result: {result}\n")

        log_data_to_csv(rainfall, temperature, humidity, result)

        again = input("🔁 Do you want to test another input? (yes/no): ").lower()
        if again != "yes":
            print("\n📝 All your results are saved in 'data_log.csv'. Thank you!")
            break

if __name__ == "__main__":
    main()
