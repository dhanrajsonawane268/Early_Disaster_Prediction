import customtkinter as ctk
from predict import predict_disaster
from playsound import playsound
from reportlab.pdfgen import canvas
import datetime

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x450")
app.title("🌧️ Early Disaster Prediction")

title = ctk.CTkLabel(app, text="Disaster Risk Predictor", font=("Arial", 20))
title.pack(pady=20)

rainfall_input = ctk.CTkEntry(app, placeholder_text="Rainfall (mm)")
rainfall_input.pack(pady=10)

temperature_input = ctk.CTkEntry(app, placeholder_text="Temperature (°C)")
temperature_input.pack(pady=10)

humidity_input = ctk.CTkEntry(app, placeholder_text="Humidity (%)")
humidity_input.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

def predict():
    try:
        rain = float(rainfall_input.get())
        temp = float(temperature_input.get())
        hum = float(humidity_input.get())

        result = predict_disaster(rain, temp, hum)
        result_label.configure(text=result)

        # 🔊 Sound Alert
        if "High" in result:
            playsound("alert_high.mp3")  # add this mp3 to app/
        else:
            playsound("safe.mp3")        # add this mp3 to app/
    except:
        result_label.configure(text="⚠️ Invalid input!")

def export_to_pdf(rain, temp, hum, result_text):
    filename = f"Disaster_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, "🌧️ Early Disaster Prediction Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Rainfall: {rain} mm")
    c.drawString(100, 680, f"Temperature: {temp} °C")
    c.drawString(100, 660, f"Humidity: {hum} %")
    c.drawString(100, 640, f"Result: {result_text}")
    c.drawString(100, 620, f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    c.save()
    print(f"✅ Report exported as {filename}")

def export():
    try:
        rain = float(rainfall_input.get())
        temp = float(temperature_input.get())
        hum = float(humidity_input.get())
        result = predict_disaster(rain, temp, hum)
        export_to_pdf(rain, temp, hum, result)
        result_label.configure(text="✅ PDF Exported!")
    except:
        result_label.configure(text="⚠️ Cannot Export")

predict_btn = ctk.CTkButton(app, text="Predict", command=predict)
predict_btn.pack(pady=10)

export_btn = ctk.CTkButton(app, text="Export Report to PDF", command=export)
export_btn.pack(pady=10)

app.mainloop()
# app/gui.py
import customtkinter as ctk
from predict import predict_disaster
from playsound import playsound
from reportlab.pdfgen import canvas
import datetime

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x450")
app.title("🌧️ Early Disaster Prediction")

title = ctk.CTkLabel(app, text="Disaster Risk Predictor", font=("Arial", 20))
title.pack(pady=20)

rainfall_input = ctk.CTkEntry(app, placeholder_text="Rainfall (mm)")
rainfall_input.pack(pady=10)

temperature_input = ctk.CTkEntry(app, placeholder_text="Temperature (°C)")
temperature_input.pack(pady=10)

humidity_input = ctk.CTkEntry(app, placeholder_text="Humidity (%)")
humidity_input.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=20)

def predict():
    try:
        rain = float(rainfall_input.get())
        temp = float(temperature_input.get())
        hum = float(humidity_input.get())

        result = predict_disaster(rain, temp, hum)
        result_label.configure(text=result)

        if "High" in result:
            playsound("alert_high.mp3")
        else:
            playsound("safe.mp3")

    except:
        result_label.configure(text="⚠️ Invalid input!")

def export_to_pdf(rain, temp, hum, result_text):
    filename = f"Disaster_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, "🌧️ Early Disaster Prediction Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Rainfall: {rain} mm")
    c.drawString(100, 680, f"Temperature: {temp} °C")
    c.drawString(100, 660, f"Humidity: {hum} %")
    c.drawString(100, 640, f"Result: {result_text}")
    c.drawString(100, 620, f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    c.save()
    print(f"✅ Report exported as {filename}")

def export():
    try:
        rain = float(rainfall_input.get())
        temp = float(temperature_input.get())
        hum = float(humidity_input.get())
        result = predict_disaster(rain, temp, hum)
        export_to_pdf(rain, temp, hum, result)
        result_label.configure(text="✅ PDF Exported!")
    except:
        result_label.configure(text="⚠️ Cannot Export")

predict_btn = ctk.CTkButton(app, text="Predict", command=predict)
predict_btn.pack(pady=10)

export_btn = ctk.CTkButton(app, text="Export Report to PDF", command=export)
export_btn.pack(pady=10)

app.mainloop()
