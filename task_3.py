import datetime
import speech_recognition as sr
from googletrans import Translator
import pytz

def translate_audio_to_hindi():
    # Check if the present time is after 6 PM IST(Indian Standard Time)
    current_time = datetime.datetime.now().astimezone(pytz.timezone('Asia/Kolkata')).time()
    if current_time < datetime.time(17, 0, 0):
        print("Please try again after 6 PM IST")
        return

    # Initialize speech recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the user
    with sr.Microphone() as source:
        print("Speak something in English:")
        audio = recognizer.listen(source)

    try:
        # Recognize the speech from the user
        english_text = recognizer.recognize_google(audio)

        # Preprocess the text
        english_text = english_text.lower().strip()

        # Check if the text starts from "M" or "O"
        if english_text.startswith('m') or english_text.startswith('o'):
            print("Sorry, I didn't understanding. Please repeat again.")
            return

        # Translate English text to Hindi
        translator = Translator()
        translation = translator.translate(english_text, src='en', dest='hi')

        # Display the translation voice
        print("Translated Hindi text:", translation.text)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio. Please repeat it again:")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service:")

# Call the translation function
translate_audio_to_hindi()
