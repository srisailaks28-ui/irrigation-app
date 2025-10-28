import streamlit as st
import random
from gtts import gTTS
import os
import speech_recognition as sr

# --- Page setup ---
st.set_page_config(page_title="Sustainable Irrigation System", layout="centered")

# --- Function: Voice input ---
def voice_input(label, lang_code="en"):
    recognizer = sr.Recognizer()
    mic_input = None
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"🎙 Speak your {label}")
    with col2:
        record = st.button(f"Record {label}")
    if record:
        with sr.Microphone() as source:
            st.info("Listening... please speak now.")
            audio = recognizer.listen(source, timeout=5)
        try:
            text = recognizer.recognize_google(audio, language=lang_code)
            st.success(f"You said: {text}")
            try:
                mic_input = float(text)
            except:
                st.warning("Could not detect a numeric value, please try again.")
        except Exception:
            st.error("Sorry, could not understand your voice. Please speak clearly.")
    return mic_input

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
        "sustainable_tip": "🌾 Sustainable Tip"
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
        "sustainable_tip": "🌾 நிலைத்தன்மை குறிப்பு"
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
        "sustainable_tip": "🌾 स्थिरता सुझाव"
    }
}
t = translations[language]

# --- Page title ---
st.title(t["title"])

# --- Voice language codes ---
lang_code = "en" if language == "English" else ("ta-IN" if "Tamil" in language else "hi-IN")

# --- Input fields (voice + manual) ---
st.write("🎧 You can either speak or type the values below.")

ph_voice = voice_input(t["ph"], lang_code)
ph = ph_voice if ph_voice is not None else st.number_input(t["ph"], 0.0, 14.0, 6.5)

temp_voice = voice_input(t["temp"], lang_code)
temp = temp_voice if temp_voice is not None else st.number_input(t["temp"], 0.0, 60.0, 30.0)

rain_voice = voice_input(t["rain"], lang_code)
rain = rain_voice if rain_voice is not None else st.number_input(t["rain"], 0.0, 500.0, 10.0)

ndvi_voice = voice_input(t["ndvi"], lang_code)
ndvi = ndvi_voice if ndvi_voice is not None else st.number_input(t["ndvi"], 0.0, 1.0, 0.5)

# --- Predict button ---
if st.button(t["predict"]):
    irrigation_needed = temp > 35 or rain < 5

    if irrigation_needed:
        msg = t["irrigation_required"]
    else:
        msg = t["irrigation_not_required"]

    st.subheader("💧 " + msg)

    # Sustainability score
    sustainability_score = random.uniform(6.0, 10.0)
    st.subheader(t["sustainability_score"])
    st.write(f"{sustainability_score:.1f} / 10**")

    # Tip section
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

    # Voice output for result
    try:
        lang_code_tts = "en" if language == "English" else ("ta" if "Tamil" in language else "hi")
        speech_text = f"{msg}. Sustainability score is {sustainability_score:.1f}. {tip}"
        tts = gTTS(text=speech_text, lang=lang_code_tts)
        tts.save("speak.mp3")
        st.audio("speak.mp3")
    except Exception as e:
        st.warning(f"Voice not available in this environment: {e}")
