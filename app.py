# app.py
import streamlit as st
from googletrans import Translator

# App title
st.title("🌐 AI-Powered Multi-Language Translator")
st.write("Enter text below and select the target language to translate.")

# Text input
text_to_translate = st.text_area("Enter text here:")

# Language selection
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn"
}

target_lang = st.selectbox("Select target language:", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translator = Translator()
        try:
            result = translator.translate(text_to_translate, dest=languages[target_lang])
            st.success("✅ Translation complete!")
            st.write(f"**Translated text ({target_lang}):**")
            st.write(result.text)
        except Exception as e:
            st.error(f"Translation failed: {e}")