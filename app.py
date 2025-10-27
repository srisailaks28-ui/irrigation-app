import streamlit as st
import joblib
import numpy as np

# Load models
model = joblib.load("irrigation_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page configuration
st.set_page_config(
    page_title="Sustainable Irrigation System",
    layout="centered",
    page_icon="💧"
)

# 🌿 Custom Sustainable Agriculture Theme
page_bg = """
<style>
/* Background: soft agriculture green gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #b6e2a1 0%, #d6f5c7 100%);
    background-attachment: fixed;
}

/* Transparent header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Text styling */
h1, h2, h3, h4 {
    color: #1b4332;
    text-align: center;
    font-family: "Trebuchet MS", sans-serif;
}

label, input, p {
    color: #2d4739 !important;
    font-family: "Segoe UI", sans-serif;
}

/* Predict button styling */
div.stButton > button:first-child {
    background-color: #40916c;
    color: white;
    font-weight: 600;
    border-radius: 10px;
    border: none;
    padding: 10px 24px;
    transition: all 0.3s ease-in-out;
}
div.stButton > button:first-child:hover {
    background-color: #2d6a4f;
    transform: scale(1.03);
}

/* Subtle footer credits */
.footer-credit {
    position: fixed;
    bottom: 10px;
    width: 100%;
    text-align: center;
    color: #2d4739;
    font-size: 13px;
    opacity: 0.7;
    font-family: "Segoe UI", sans-serif;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🌾 Title
st.title("💧 Sustainable Irrigation Prediction System")
st.markdown("#### Empowering Smart Water Use for a Greener Future 🌱")

# 🧮 Manual numeric input fields with realistic examples
st.markdown("### Enter your field parameters below:")

soil_ph = st.text_input("Soil pH", placeholder="Example: 6.5")
organic_matter = st.text_input("Organic Matter %", placeholder="Example: 3.2")
sand_percent = st.text_input("Sand %", placeholder="Example: 45")
temperature = st.text_input("Temperature (°C)", placeholder="Example: 30")
rainfall = st.text_input("Rainfall (mm)", placeholder="Example: 10")
ndvi = st.text_input("NDVI", placeholder="Example: 0.6")

# Predict button
if st.button("🔍 Predict Irrigation Need"):
    if all([soil_ph, organic_matter, sand_percent, temperature, rainfall, ndvi]):
        try:
            # Convert inputs to float
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
        except ValueError:
            st.error("⚠ Please enter only numeric values (e.g., 6.5, 3.2, 45).")
    else:
        st.warning("⚠ Please fill in all fields before predicting.")

# 🌾 Footer credits (small & blended)
st.markdown("""
<div class="footer-credit">
    Credits: Dharaniya • Balanivethidha • SriSaiLakshmi
</div>
""", unsafe_allow_html=True)
