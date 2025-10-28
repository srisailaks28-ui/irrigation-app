import streamlit as st
import random
from gtts import gTTS
import os
import speech_recognition as sr
from pydub import AudioSegment

# --- Page setup ---
st.set_page_config(page_title="Sustainable Irrigation System", layout="centered")

# --- Function: voice input from uploaded audio ---
def voice_from_audio(uploaded_file, lang_code="en"):
    if uploaded_file is not None:
        recognizer = sr.Recognizer()
        with open("temp_audio.wav", "wb") as f:
            f.write(uploaded_file.read())

        # Convert to wav if needed
        try:
            audio = AudioSegment.from_file("temp_audio.wav")
            audio.export("converted.wav", format="wav")
        except:
            st.error("Error converting audio file. Please try again.")
            return None

        with sr.AudioFile("converted.wav") as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=lang_code)
            st.success(f"You said: {text}")
            try:
                return float(text)
            except:
                st.warning("Could not detect a numeric value.")
        except Exception:
            st.error("Sorry, could not recognize your voice.")
    return None

# --- Language selection ---
language = st.selectbox("🌐 Select Language", ["English", "தமிழ் (Tamil)", "हिन्दी (Hindi)"])

# --- Translation dictionary ---
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
lang_code = "en" if language == "English" else ("ta-IN" if "Tamil" in language else "hi-IN")

# --- Title ---
st.title(t["title"])
st.write("🎧 You can upload a short voice recording (WAV/MP3) or type values manually.")

# --- Inputs (upload or manual) ---
uploaded_ph = st.file_uploader(f"Upload voice for {t['ph']} (optional)", type=["wav", "mp3"])
ph_voice = voice_from_audio(uploaded_ph, lang_code)
ph = ph_voice if ph_voice is not None else st.number_input(t["ph"], 0.0, 14.0, 6.5)

uploaded_temp = st.file_uploader(f"Upload voice for {t['temp']} (optional)", type=["wav", "mp3"])
temp_voice = voice_from_audio(uploaded_temp, lang_code)
temp = temp_voice if temp_voice is not None else st.number_input(t["temp"], 0.0, 60.0, 30.0)

uploaded_rain = st.file_uploader(f"Upload voice for {t['rain']} (optional)", type=["wav", "mp3"])
rain_voice = voice_from_audio(uploaded_rain, lang_code)
rain = rain_voice if rain_voice is not None else st.number_input(t["rain"], 0.0, 500.0, 10.0)

uploaded_ndvi = st.file_uploader(f"Upload voice for {t['ndvi']} (optional)", type=["wav", "mp3"])
ndvi_voice = voice_from_audio(uploaded_ndvi, lang_code)
ndvi = ndvi_voice if ndvi_voice is not None else st.number_input(t["ndvi"], 0.0, 1.0, 0.5)

# --- Predict button ---
if st.button(t["predict"]):
    irrigation_needed = temp > 35 or rain < 5
    msg = t["irrigation_required"] if irrigation_needed else t["irrigation_not_required"]

    st.subheader("💧 " + msg)

    # --- Sustainability score ---
    score = random.uniform(6.0, 10.0)
    st.subheader(t["sustainability_score"])
    st.write(f"{score:.1f} / 10**")

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
    st.subheader(t["sustainable_tip"])
    st.info(tip)

    # --- Voice output for result ---
    try:
        lang_code_tts = "en" if language == "English" else ("ta" if "Tamil" in language else "hi")
        full_text = f"{msg}. Sustainability score is {score:.1f}. {tip}"
        tts = gTTS(text=full_text, lang=lang_code_tts)
        tts.save("speak.mp3")
        st.audio("speak.mp3")
    except Exception as e:
        st.warning(f"Voice not available in this environment: {e}")
