# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

data = pd.read_csv("data/flood_dataset.csv")

X = data[['rainfall', 'temperature', 'humidity']]
y = data['flood']

model = RandomForestClassifier()
model.fit(X, y)

# Save the model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model/model.pkl")
