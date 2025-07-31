from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[14].id)  # Set to the first voice
    engine.setProperty("rate", 110)  # Speed of speech
    engine.setProperty("volume", 1)  # Volume level (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()


def extract_text_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source, duration=10)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error sending request to google; {e}")


if __name__ == "__main__":
    load_dotenv()
    text = extract_text_from_mic()
    speak(text)
