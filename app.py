import streamlit as st
import random
from gtts import gTTS
import os

# --- Page setup ---
st.set_page_config(page_title="Sustainable Irrigation System", layout="centered")

st.title("🌾 Smart Sustainable Irrigation System")

# --- Language selection ---
language = st.selectbox("🌐 Select Language", ["English", "தமிழ் (Tamil)", "हिन्दी (Hindi)"])

# --- Input fields ---
ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
temp = st.number_input("Temperature (°C)", 0.0, 60.0, 30.0)
rain = st.number_input("Rainfall (mm)", 0.0, 500.0, 10.0)
ndvi = st.number_input("NDVI", 0.0, 1.0, 0.5)

# --- Translate button text ---
if language == "English":
    button_text = "Predict Irrigation"
elif language == "தமிழ் (Tamil)":
    button_text = "நீர்ப்பாசனம் கணிக்க"
else:
    button_text = "सिंचाई की भविष्यवाणी करें"

# --- Predict button ---
if st.button(button_text):
    # Dummy logic for demo
    irrigation_needed = temp > 35 or rain < 5

    # --- Result text by language ---
    if irrigation_needed:
        if language == "English":
            msg = "Irrigation required soon."
        elif language == "தமிழ் (Tamil)":
            msg = "விரைவில் நீர்ப்பாசனம் தேவை."
        else:
            msg = "शीघ्र सिंचाई की आवश्यकता है."
    else:
        if language == "English":
            msg = "Irrigation not required currently."
        elif language == "தமிழ் (Tamil)":
            msg = "தற்போது நீர்ப்பாசனம் தேவையில்லை."
        else:
            msg = "फिलहाल सिंचाई की आवश्यकता नहीं है."

    st.subheader("💧 " + msg)

    # --- Sustainability score ---
    sustainability_score = random.uniform(6.0, 10.0)
    st.subheader("♻ Sustainability Score")
    st.write(f"{sustainability_score:.1f} / 10**")

    # --- Tip section ---
    tips = {
        "English": [
            "Use mulching to retain soil moisture.",
            "Collect rainwater for irrigation.",
            "Irrigate early in the morning to reduce evaporation.",
        ],
        "தமிழ் (Tamil)": [
            "மண்ணின் ஈரத்தை தக்கவைத்துக்கொள்ள மடிப்பு முறையைப் பயன்படுத்துங்கள்.",
            "மழைநீரை சேகரித்து நீர்ப்பாசனத்திற்கு பயன்படுத்துங்கள்.",
            "நீராவி இழப்பை குறைக்க காலை நேரத்தில் நீர்ப்பாசனம் செய்யுங்கள்.",
        ],
        "हिन्दी (Hindi)": [
            "मल्चिंग का उपयोग करें ताकि मिट्टी में नमी बनी रहे।",
            "सिंचाई के लिए वर्षा जल एकत्र करें।",
            "वाष्पीकरण को कम करने के लिए सुबह सिंचाई करें।",
        ],
    }

    tip = random.choice(tips[language])
    st.subheader("🌾 Sustainable Tip")
    st.info(tip)

    # --- Voice output (optional) ---
    try:
        lang_code = "en" if language == "English" else ("ta" if language == "தமிழ் (Tamil)" else "hi")
        tts = gTTS(text=msg, lang=lang_code)
        tts.save("speak.mp3")
        st.audio("speak.mp3")
    except Exception as e:
        st.warning(f"Voice not available in this environment: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Designed by: Dharaniya | Balanivethidha | SriSaiLakshmi | ")
