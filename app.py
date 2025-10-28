import streamlit as st
import random
from gtts import gTTS
import os

# --- Page setup ---
st.set_page_config(page_title="Sustainable Irrigation System", layout="centered")

# --- Language selection ---
language = st.selectbox("🌐 Select Language", ["English", "தமிழ் (Tamil)", "हिन्दी (Hindi)"])

# --- Translations dictionary ---
translations = {
    "English": {
        "title": "🌾 Smart Sustainable Irrigation System",
        "ph": "Soil pH",
        "temp": "Temperature (°C)",
        "rain": "Rainfall (mm)",
        "ndvi": "NDVI",
        "predict": "Predict Irrigation",
        "irrigation_required": "Irrigation required soon. Estimated water need high. Immediate irrigation recommended.",
        "irrigation_not_required": "Irrigation not required currently. Estimated water need low. Next irrigation suggested after 3–5 days.",
        "sustainability_score": "♻ Sustainability Score",
        "sustainable_tip": "🌾 Sustainable Tip",
        "credits": "Designed by: Dharaniya | Balanivethidha | SriSaiLakshmi | Department of ECE, Anna University Regional Campus, Madurai"
    },
    "தமிழ் (Tamil)": {
        "title": "🌾 திறமையான நிலைத்த நீர்ப்பாசன முறை",
        "ph": "மண் pH",
        "temp": "வெப்பநிலை (°C)",
        "rain": "மழை அளவு (மிமீ)",
        "ndvi": "NDVI",
        "predict": "நீர்ப்பாசனம் கணிக்க",
        "irrigation_required": "விரைவில் நீர்ப்பாசனம் தேவை. நீரின் தேவை அதிகம். உடனடியாக நீர்ப்பாசனம் செய்ய பரிந்துரைக்கப்படுகிறது.",
        "irrigation_not_required": "தற்போது நீர்ப்பாசனம் தேவையில்லை. நீர் தேவை குறைவு. அடுத்த நீர்ப்பாசனம் 3–5 நாட்களுக்கு பிறகு பரிந்துரைக்கப்படுகிறது.",
        "sustainability_score": "♻ நிலைத்தன்மை மதிப்பெண்",
        "sustainable_tip": "🌾 நிலைத்தன்மை குறிப்பு",
        "credits": "வடிவமைப்பு: தரணியா | பாலநிவேதிதா | ஸ்ரீசாயிலட்சுமி | மின் மற்றும் மின்னணு பொறியியல் துறை, அண்ணா பல்கலைக்கழகம் பிராந்திய வளாகம், மதுரை"
    },
    "हिन्दी (Hindi)": {
        "title": "🌾 स्मार्ट स्थायी सिंचाई प्रणाली",
        "ph": "मिट्टी का pH",
        "temp": "तापमान (°C)",
        "rain": "वर्षा (मिमी)",
        "ndvi": "NDVI",
        "predict": "सिंचाई की भविष्यवाणी करें",
        "irrigation_required": "शीघ्र सिंचाई की आवश्यकता है। जल की आवश्यकता अधिक है। तुरंत सिंचाई की सिफारिश की जाती है।",
        "irrigation_not_required": "फिलहाल सिंचाई की आवश्यकता नहीं है। जल की आवश्यकता कम है। अगली सिंचाई 3–5 दिनों बाद सुझाई जाती है।",
        "sustainability_score": "♻ स्थिरता अंक",
        "sustainable_tip": "🌾 स्थिरता सुझाव",
        "credits": "डिज़ाइन: धरनिया | बालनिवेथिधा | श्रीसाइलक्ष्मी | इलेक्ट्रॉनिक्स एवं संचार विभाग, अन्ना विश्वविद्यालय क्षेत्रीय परिसर, मदुरै"
    }
}

t = translations[language]

# --- Page title ---
st.title(t["title"])

# --- Input fields ---
ph = st.number_input(t["ph"], 0.0, 14.0, 6.5)
temp = st.number_input(t["temp"], 0.0, 60.0, 30.0)
rain = st.number_input(t["rain"], 0.0, 500.0, 10.0)
ndvi = st.number_input(t["ndvi"], 0.0, 1.0, 0.5)

# --- Predict button ---
if st.button(t["predict"]):
    irrigation_needed = temp > 35 or rain < 5

    # --- Result based on condition ---
    if irrigation_needed:
        msg = t["irrigation_required"]
    else:
        msg = t["irrigation_not_required"]

    st.subheader("💧 " + msg)

    # --- Sustainability score ---
    sustainability_score = random.uniform(6.0, 10.0)
    st.subheader(t["sustainability_score"])
    st.write(f"{sustainability_score:.1f} / 10**")

    # --- Tips section ---
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
    st.subheader(t["sustainable_tip"])
    st.info(tip)

    # --- Voice output for full message ---
    try:
        lang_code = "en" if language == "English" else ("ta" if "Tamil" in language else "hi")
        speech_text = f"{msg}. Sustainability score is {sustainability_score:.1f}. {tip}"
        tts = gTTS(text=speech_text, lang=lang_code)
        tts.save("speak.mp3")
        st.audio("speak.mp3")
    except Exception as e:
        st.warning(f"Voice not available in this environment: {e}")

# --- Footer ---
st.markdown("---")
st.caption(t["credits"])
