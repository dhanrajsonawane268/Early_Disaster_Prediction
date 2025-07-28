# app/predict.py

def predict_disaster(rainfall, temperature, humidity):
    """
    Predict disaster risk based on rainfall, temperature, and humidity.
    """
    if rainfall > 150 and temperature > 45 and humidity > 80:
        return "⚠ Severe Disaster Risk"
    elif rainfall > 100 and temperature > 35:
        return "⚠ Moderate Disaster Risk"
    elif rainfall > 50:
        return "⚠ Mild Disaster Risk"
    else:
        return "✅ No Immediate Disaster Risk"
