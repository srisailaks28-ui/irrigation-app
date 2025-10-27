import streamlit as st
import pickle
import numpy as np
import re

# ---- Load model and scaler ----
model = pickle.load(open("irrigation_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---- Page setup ----
st.set_page_config(page_title="Smart Irrigation Predictor", page_icon="💧", layout="centered")

# ---- Custom CSS styling ----
st.markdown("""
<style>
/* 🌿 Background - dark sustainable green with soft texture overlay */
.stApp {
    background: linear-gradient(to bottom right, #204e30, #3a6b45);
    background-image: url('https://www.transparenttextures.com/patterns/green-fibers.png');
    background-repeat: repeat;
    background-attachment: fixed;
    color: #f1faee;
}

/* Input boxes */
.stTextInput > div > div > input {
    background-color: #edf6f9;
    color: #204e30;
    border: 1px solid #74c69d;
    border-radius: 10px;
    padding: 8px;
    font-size: 16px;
}

/* Buttons */
div.stButton > button {
    background-color: #40916c;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #1b4332;
    transform: scale(1.02);
}

/* Result text */
.stSuccess, .stWarning, .stInfo {
    background-color: rgba(255,255,255,0.15);
    border-radius: 8px;
    padding: 10px;
}

/* Credits blended softly at bottom */
.credits {
    position: fixed;
    bottom: 6px;
    left: 10px;
    font-size: 12px;
    color: rgba(255,255,255,0.6);
    background: rgba(32,78,48,0.3);
    padding: 3px 8px;
    border-radius: 5px;
    font-style: italic;
}
</style>

<div class="credits">Credits: Dharaniya · Balanivethidha · SriSaiLakshmi</div>
""", unsafe_allow_html=True)

# ---- App Title ----
st.markdown("<h1 style='text-align:center; color:#f1faee;'>🌾 Smart Irrigation Prediction System</h1>", unsafe_allow_html=True)
st.write("### Enter numeric values for your field data below:")

# ---- Input fields ----
fields = {
    "Soil pH": "6.5",
    "Organic Matter %": "3.3",
    "Sand %": "45",
    "Temperature (°C)": "32",
    "Rainfall (mm)": "10",
    "NDVI": "0.6"
}

cols = st.columns(2)
raw_inputs = {}
i = 0
for label, example in fields.items():
    with cols[i % 2]:
        raw = st.text_input(f"{label} (example: {example})", "")
        raw_inputs[label] = raw
    i += 1

# ---- Helper to clean numeric input ----
def parse_number(s):
    if s is None or s.strip() == "":
        raise ValueError("empty")
    s = s.strip().replace(",", ".")
    try:
        return float(s)
    except:
        m = re.search(r"[-+]?\d*\.?\d+", s)
        if m:
            return float(m.group(0))
    raise ValueError(f"cannot parse '{s}'")

# ---- Predict Button ----
if st.button("💧 Predict Irrigation Need"):
    parsed = {}
    bad = {}

    for k, raw in raw_inputs.items():
        try:
            val = parse_number(raw)
            parsed[k] = val
        except ValueError as e:
            bad[k] = {"raw": raw, "error": str(e)}

    if bad:
        st.error("⚠ Please enter valid numeric values for all fields.")
        for k, info in bad.items():
            st.write(f"{k}** → raw: {info['raw']} · error: {info['error']}")
    else:
        values = [parsed[k] for k in fields.keys()]
        X = np.array([values])
        try:
            X_scaled = scaler.transform(X)
            pred = model.predict(X_scaled)[0]
        except Exception as e:
            st.error(f"Model/scaler error: {e}")
        else:
            st.subheader("🌱 Result")
            if int(pred) == 0:
                st.success("Irrigation not required currently.")
                st.info("💧 Estimated water need: Low\n📅 Next irrigation suggested after 3–5 days.")
            else:
                st.warning("Irrigation required soon.")
                st.info("💧 Estimated water need: High\n📅 Immediate irrigation recommended.")
