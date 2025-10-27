
import streamlit as st

st.set_page_config(page_title="Sustainable Irrigation System", page_icon="💧", layout="centered")

# 🌿 Stylish background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #2d6a4f, #1b4332);
    background-image: url('https://www.transparenttextures.com/patterns/green-fibers.png');
    background-repeat: repeat;
    background-attachment: fixed;
    color: #f1faee;
}
h1 {
    text-align: center;
    color: #f1faee !important;
    font-weight: 800;
}
.stTextInput > div > div > input {
    background-color: #edf6f9;
    color: #1b4332;
    border: 1px solid #74c69d;
    border-radius: 8px;
    padding: 8px;
    font-size: 16px;
}
div.stButton > button {
    background-color: #2d6a4f;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 17px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #1b4332;
    transform: scale(1.03);
}
.credits {
    position: fixed;
    bottom: 10px;
    left: 10px;
    font-size: 13px;
    color: rgba(255,255,255,0.7);
    background: rgba(27,67,50,0.3);
    padding: 4px 10px;
    border-radius: 6px;
    font-style: italic;
}
</style>

<div class="credits">
Credits to: Dharaniya · Balanivethidha · SriSaiLakshmi
</div>
""", unsafe_allow_html=True)

st.title("🌿 Sustainable Irrigation System")
st.write("Enter your field parameters below:")

# 🌱 Input fields
pH = st.text_input("Soil pH (example: 6.5)")
om = st.text_input("Organic Matter (%) (example: 2.5)")
sand = st.text_input("Sand (%) (example: 40)")
temp = st.text_input("Temperature (°C) (example: 30)")
rain = st.text_input("Rainfall (mm) (example: 5)")
ndvi = st.text_input("NDVI (example: 0.5)")

# 💧 Prediction simulation (no model file)
if st.button("🔍 Predict Irrigation"):
    try:
        float(pH); float(om); float(sand); float(temp); float(rain); float(ndvi)
        st.success("💧 Irrigation not required currently.")
        st.info("Estimated water needed: 20 mm.")
        st.warning("Next irrigation suggested after 3 days.")
    except:
        st.error("⚠ Please enter valid numeric values for all fields.")

