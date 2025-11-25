import streamlit as st
from googletrans import Translator
from gtts import gTTS
import io
# pydub is installed but not explicitly used in this simplified Streamlit approach

class TTSService:
    def __init__(self):
        self.translator = Translator()
        # No API keys or external services needed for gTTS
        
    def translate_to_hindi(self, text):
        """Translate English text to Hindi"""
        try:
            translation = self.translator.translate(text, dest='hi') 
            return translation.text
        except Exception as e:
            # st.error(f"Translation error: {str(e)}") # Keep the app clean
            return None

    def generate_speech(self, hindi_text):
        """Generate speech from Hindi text using the free, local gTTS library"""
        if not hindi_text:
            st.error("No text provided for speech generation")
            return None

        try:
            # 1. gTTS se Hindi audio generate karo
            # 'hi' is the language code for Hindi
            tts = gTTS(text=hindi_text, lang='hi')
            
            # 2. Audio ko memory (BytesIO) mein save karo
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            
            return mp3_fp

        except Exception as e:
            st.error(f"Local TTS (gTTS) generation failed: {str(e)}")
            return None