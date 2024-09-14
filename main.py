import time
import speech_recognition as sr
from speech_to_text import listen_and_recognize, text_to_optimus_voice
from text_to_speech import play_voice

# Main flow - Infinite Loop until Ctrl + C
if __name__ == "__main__":
    try:
        # Initialize recognizer and microphone outside the loop
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        # Initial test message
        print("Testing text-to-speech with initial message...")
        audio_buffer = text_to_optimus_voice("Hi Autobots, I am Optimus Prime!")
        play_voice(audio_buffer)

        while True:
            # Step 1: Listen and convert speech to text
            print("Listening for your speech...")
            recognized_text = listen_and_recognize(recognizer, mic)

            # Step 2: Convert recognized text to Optimus Prime voice and play it
            if recognized_text:
                print("Converting recognized text to Optimus Prime voice...")
                audio_buffer = text_to_optimus_voice(recognized_text)
                play_voice(audio_buffer)
            else:
                print("No text recognized, trying again...")

            # Add a small delay before the next input
            time.sleep(1)  # Pause for 1 second

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
