import speech_recognition as sr
from pyht import Client, TTSOptions, Format
from io import BytesIO
import json

with open('cred.json') as f:
    config = json.load(f)

API_ID = config["PLAYHT_API_ID"]
API_KEY = config["PLAYHT_API_KEY"]
# Initialize PlayHT API with your credentials
client = Client(API_ID, API_KEY)

# Configure TTS options
options = TTSOptions(
        voice="s3://voice-cloning-zero-shot/cda55a5e-68ab-463a-9ffe-69fd1f646acd/original/manifest.json",
  # Cloned voice
    sample_rate=44_100,
    format=Format.FORMAT_MP3,
    speed=0.75,
)

# Function to convert speech to text
def listen_and_recognize(recognizer, mic):
    try:
        with mic as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)

        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service; {e}")
        return None
    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to convert text to voice using PlayHT
def text_to_optimus_voice(text):
    if text:
        try:
            # Create an in-memory buffer to hold audio chunks
            audio_buffer = BytesIO()

            # Fetch the voice data from the PlayHT API
            print("Fetching voice data from PlayHT API...")
            response = client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options)
            print("Received response from PlayHT API.")

            if not response:
                print("No audio data received from PlayHT API.")
                return None

            for chunk in response:
                audio_buffer.write(chunk)

            return audio_buffer

        except Exception as e:
            print(f"An error occurred while processing the voice: {e}")
            return None
