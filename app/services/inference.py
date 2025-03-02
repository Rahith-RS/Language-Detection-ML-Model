import joblib
import numpy as np

# Load model
model = joblib.load("app/models/model.pkl")

def predict(features: list):
    prediction = model.predict([features])
    return {"prediction": int(prediction[0])}
