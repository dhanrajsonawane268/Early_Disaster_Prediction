# ✅ File: gui.py
import tkinter as tk
from tkinter import messagebox, filedialog
import re
from fpdf import FPDF
from csv_reader import read_latest_input
import datetime
import os
import pyttsx3
import sys
import joblib
import csv

# 🔁 Load model
model = joblib.load('../model/model.pkl')

# 🎙 Initialize Jarvis (speech engine)
engine = pyttsx3.init()

# 📁 Ensure log folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# 📤 Export to PDF (Fixed Version)
def clean_text(text):
    """Remove emojis and unsupported characters for FPDF (latin-1 only)."""
    if not isinstance(text, str):
        text = str(text)
    return re.sub(r'[^\x00-\xFF]', '', text)  # Removes emojis and non-latin chars

# 📤 Export to PDF (with encoding fix)
def export_to_pdf(data, prediction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt=clean_text("Early Disaster Prediction Report"), ln=True, align="C")
    pdf.ln(10)

    for key, value in data.items():
        pdf.cell(200, 10, txt=clean_text(f"{key}: {value}"), ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=clean_text(f"Prediction: {prediction}"), ln=True)

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile=f"Disaster_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )

    if file_path:
        pdf.output(file_path)
        messagebox.showinfo("✅ Success", f"PDF exported successfully:\n{file_path}")

# 🔊 Speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# 🌐 GUI Setup
root = tk.Tk()
root.title("🌍 Early Disaster Prediction")
root.geometry("520x500")
root.config(bg="#f0f8ff")

tk.Label(root, text="Early Disaster Predictor", font=("Helvetica", 18, "bold"),
         bg="#f0f8ff", fg="navy").pack(pady=10)

# 📥 Input fields
fields = {}
for label in ["🌧 Rainfall (mm):", "🌡 Temperature (°C):", "💧 Humidity (%)", "🌪 Wind Speed (km/h):", "🌱 Soil Moisture (%):"]:
    tk.Label(root, text=label, bg="#f0f8ff", font=("Arial", 12)).pack()
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack()
    fields[label] = entry

# 📊 Result label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14, "bold"),
                        bg="#f0f8ff", fg="green")
result_label.pack(pady=10)

# 🔍 Prediction function
def predict():
    try:
        # Get inputs
        try:
            rainfall = float(fields["🌧 Rainfall (mm):"].get().strip())
            temperature = float(fields["🌡 Temperature (°C):"].get().strip())
            humidity = float(fields["💧 Humidity (%)"].get().strip())
            wind_speed = float(fields["🌪 Wind Speed (km/h):"].get().strip())
            soil_moisture = float(fields["🌱 Soil Moisture (%):"].get().strip())
        except ValueError:
            messagebox.showerror("❌ Input Error", "Please enter valid numeric values.")
            return

        # Save to latest_input.csv
        with open("latest_input.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Temperature", "Humidity", "Wind Speed", "Soil Moisture"])
            writer.writerow([temperature, humidity, wind_speed, soil_moisture])

        # 🔁 Get input from CSV and predict
        latest_data = read_latest_input()
        if latest_data:
            prediction = model.predict([latest_data])[0]

            if prediction == 1:
                result_text.set("⚠️ Risk of Disaster Detected!")
                messagebox.showwarning("⚠️ Alert", "Risk of Disaster Detected!")
                speak("Warning! Risk of disaster detected.")
            else:
                result_text.set("✅ No Risk Detected.")
                messagebox.showinfo("Safe", "No Risk Detected.")
                speak("No risk detected.")

            # Save result for PDF
            root.last_data = {
                "Rainfall (mm)": rainfall,
                "Temperature (°C)": temperature,
                "Humidity (%)": humidity,
                "Wind Speed (km/h)": wind_speed,
                "Soil Moisture (%)": soil_moisture
            }
            root.last_prediction = result_text.get()

        else:
            result_text.set("⚠️ Could not read input CSV.")
            speak("Something went wrong reading CSV.")

    except Exception as e:
        result_text.set(f"❌ Error: {str(e)}")
        speak("Error occurred during prediction.")

# 🧹 Clear inputs
def clear_all():
    for entry in fields.values():
        entry.delete(0, tk.END)
    result_text.set("")

# 📤 Export PDF
def export_report():
    try:
        if hasattr(root, 'last_data') and hasattr(root, 'last_prediction'):
            export_to_pdf(root.last_data, root.last_prediction)
        else:
            messagebox.showerror("⚠ Error", "Please predict before exporting.")
    except Exception as e:
        messagebox.showerror("⚠ Error", f"Failed to export PDF:\n{str(e)}")

# 🔘 Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

buttons = [
    ("🔍 Predict", predict, "#4CAF50"),
    ("🧹 Clear", clear_all, "#f39c12"),
    ("📤 Export PDF", export_report, "#3498db"),
    ("❌ Exit", root.quit, "#e74c3c")
]

for i, (text, func, color) in enumerate(buttons):
    tk.Button(btn_frame, text=text, command=func, bg=color, fg="white",
              font=("Arial", 10, "bold"), width=12).grid(row=0, column=i, padx=5)

tk.Label(root, text="Developed by Dhanraj Sonawane",
         bg="#f0f8ff", font=("Arial", 9)).pack(side="bottom", pady=5)

# 🚀 Start GUI
root.mainloop()
