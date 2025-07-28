import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# ✅ Proper dataset with 4 features + label
data = {
    'Temperature': [34, 30, 32, 28, 31],
    'Humidity': [85, 65, 75, 60, 70],
    'Wind Speed': [90, 60, 80, 40, 50],
    'Soil Moisture': [78, 55, 70, 35, 50],
    'label': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Temperature', 'Humidity', 'Wind Speed', 'Soil Moisture']]  # ✅ 4 features
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'model/model.pkl')

print("✅ Model trained and saved with 4 features.")
