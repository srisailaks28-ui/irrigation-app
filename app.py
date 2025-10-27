import streamlit as st
import joblib
import numpy as np

# Load models
model = joblib.load("irrigation_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page configuration
st.set_page_config(page_title="Sustainable Irrigation System", layout="centered")

# 🌿 Custom background (agriculture green)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #b7d7a8; /* soft agriculture green */
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
h1, h2, h3 {
    color: #1b4332;
    text-align: center;
}
footer {
    visibility: hidden;
}
.credit-box {
    background-color: rgba(255,255,255,0.8);
    border-radius: 12px;
    padding: 10px;
    text-align: center;
    color: #1b4332;
    font-weight: 500;
    margin-top: 30px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🌾 Title
st.title("💧 Sustainable Irrigation Prediction System")

st.write("### Enter your field parameters below:")

# 🧮 Manual input fields with realistic examples
soil_ph = st.text_input("Soil pH (example: 6.5)")
organic_matter = st.text_input("Organic Matter % (example: 3.2)")
sand_percent = st.text_input("Sand % (example: 45)")
temperature = st.text_input("Temperature (°C) (example: 30)")
rainfall = st.text_input("Rainfall (mm) (example: 10)")
ndvi = st.text_input("NDVI (example: 0.6)")

# Predict button
if st.button("🔍 Predict Irrigation Need"):
    try:
        # Convert to float
        inputs = np.array([[float(soil_ph), float(organic_matter), float(sand_percent),
                            float(temperature), float(rainfall), float(ndvi)]])
        
        # Scale + Predict
        scaled = scaler.transform(inputs)
        prediction = model.predict(scaled)[0]

        # Output result
        st.subheader("🌱 Result:")
        if prediction == 0:
            st.success("Irrigation not required currently.")
            st.info("💧 Estimated water need: Low\n📅 Next irrigation suggested after 3–5 days.")
        else:
            st.warning("Irrigation required soon.")
            st.info("💧 Estimated water need: High\n📅 Immediate irrigation recommended.")
    except:
        st.error("⚠ Please enter valid numeric values for all fields.")

# Footer credits
st.markdown("""
<div class='credit-box'>
    <p>Credits to:<br>
    Dharaniya<br>
    Balanivethidha<br>
    SriSaiLakshmi</p>
</div>
""", unsafe_allow_html=True)
