# app/predict.py
import pickle
import os

model_path = os.path.join("..", "model", "model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

def predict_disaster(rainfall, temperature, humidity):
    features = [[rainfall, temperature, humidity]]
    prediction = model.predict(features)
    if prediction[0] == 1:
        return "🔴 High Disaster Risk"
    else:
        return "🟢 No Disaster Risk"
