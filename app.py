import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Sustainable Irrigation System", page_icon="💧")

st.title("💧 Sustainable Irrigation Prediction System")
st.markdown("Enter soil and weather parameters below to get irrigation insights.")

# --- Input Section ---
ph = st.number_input("Soil pH", 0.0, 14.0, 6.8)
organic = st.number_input("Organic Matter (%)", 0.0, 10.0, 2.8)
sand = st.number_input("Sand (%)", 0.0, 100.0, 42.0)
temp = st.number_input("Temperature (°C)", 0.0, 60.0, 33.0)
rain = st.number_input("Rainfall (mm)", 0.0, 500.0, 4.0)
ndvi = st.number_input("NDVI", 0.0, 1.0, 0.5)

# --- Predict Button ---
if st.button("🔍 Predict Irrigation Requirement"):
    features = np.array([[ph, organic, sand, temp, rain, ndvi]])

    try:
        # 1️⃣ Irrigation status (required or not)
        try:
            status_model = joblib.load("model_status.pkl")
            status_pred = status_model.predict(features)[0]
            if int(status_pred) == 0:
                st.success("✅ Irrigation not required currently.")
            else:
                st.warning("⚠ Irrigation required soon!")
        except:
            # fallback if model not available
            if rain > 20:
                st.success("✅ Irrigation not required currently.")
            else:
                st.warning("⚠ Irrigation required soon!")

        # 2️⃣ Estimated water needed
        try:
            water_model = joblib.load("model_water.pkl")
            water_pred = water_model.predict(features)[0]
            st.info(f"💧 Estimated Water Needed: {round(water_pred, 2)} litres (approx)")
        except:
            # fallback simple logic
            est_water = max(0, (30 - rain) * 2)
            st.info(f"💧 Estimated Water Needed: {round(est_water, 2)} litres (approx)")

        # 3️⃣ Next irrigation suggested days
        try:
            days_model = joblib.load("model_days.pkl")
            days_pred = days_model.predict(features)[0]
            st.success(f"📅 Next irrigation suggested after {int(days_pred)} days.")
        except:
            # fallback logic
            if rain < 10:
                st.success("📅 Next irrigation suggested after 3 days.")
            else:
                st.success("📅 Next irrigation suggested after 6 days.")
                
    except Exception as e:
        st.error(f"Error occurred while predicting: {e}")

st.caption("Developed by Team Sustainable Irrigation 🌱")