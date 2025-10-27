import streamlit as st
import joblib
import numpy as np

# Load model and scaler safely
model = joblib.load("irrigation_model.joblib")
scaler = joblib.load("scaler.joblib")
# Cell 8: Predict irrigation + water_needed_mm + next_irrigation_days

import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("irrigation_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

print("🌾 AI Sustainable Irrigation Assistant 🌱")
print("Enter soil and weather parameters below:")

soil_ph = float(input("Enter Soil pH: "))
organic_matter = float(input("Enter Organic Matter (%): "))
sand_pct = float(input("Enter Sand Percentage (%): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
rainfall = float(input("Enter Rainfall (mm): "))
ndvi = float(input("Enter NDVI: "))

# Combine and scale
features = np.array([[soil_ph, organic_matter, sand_pct, temperature, humidity, rainfall, ndvi]])
scaled_features = scaler.transform(features)

# Predict irrigation need
prediction = model.predict(scaled_features)[0]

# Estimate additional outputs
water_needed_mm = round(max(0, (temperature * 0.8 - rainfall * 0.3 + (100 - humidity) * 0.2)), 2)
next_irrigation_days = max(1, int(7 - rainfall / 50))

# Final output
print("\n--- Irrigation Prediction Result ---")
if prediction == 1:
    print("🚿 Irrigation IS REQUIRED for this field.")
else:
    print("✅ Irrigation NOT REQUIRED currently.")

print(f"💧 Estimated Water Needed: {water_needed_mm} mm")
print(f"📅 Next Irrigation Suggested After: {next_irrigation_days} days")

