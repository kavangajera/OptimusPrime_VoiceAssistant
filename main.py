import time
import speech_recognition as sr
from speech_to_text import listen_and_recognize, text_to_optimus_voice
from text_to_speech import play_voice
import webbrowser

# Function to open websites based on recognized text
def open_website(command):
    # Define a mapping of site names to URLs
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "twitter": "https://twitter.com",
        "github": "https://github.com",
        "wikipedia":"https://www.wikipedia.org/",
        "chat GPT":"https://chatgpt.com/"
        # Add more sites as needed
    }

    # Find if a known site is in the command
    for site_name, url in sites.items():
        if site_name.lower() in command.lower():
            print(f"Opening {site_name}...")
            audio_buffer = text_to_optimus_voice(f"Opening {site_name}, Sir.")
            play_voice(audio_buffer)
            webbrowser.open(url)
            return True  # Successfully opened a website
    return False  # No matching site found

# Main flow - Infinite Loop until Ctrl + C
if __name__ == "__main__":
    try:
        # Initialize recognizer and microphone outside the loop
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        # Initial test message
        print("Testing text-to-speech with initial message...")
        audio_buffer = text_to_optimus_voice("Autobots, I am Optimus Prime, the AI bot!")
        play_voice(audio_buffer)

        while True:
            # Step 1: Listen and convert speech to text
            print("Listening for your speech...")
            recognized_text = listen_and_recognize(recognizer, mic)
            print(recognized_text)
            # Step 2: Convert recognized text to Optimus Prime voice and play it
            if recognized_text:
                print(f"Recognized: {recognized_text}")
                audio_buffer = text_to_optimus_voice(recognized_text)

                # Step 3: Check if the user asked to open a site
                if "optimus" in recognized_text.lower() and "open" in recognized_text.lower():
                    if open_website(recognized_text):
                        continue  # Successfully opened a website, go to the next iteration

                # Step 4: Check if the user wants to stop the program
                if "optimus" in recognized_text.lower() and "stop" in recognized_text.lower():
                    print("Optimus is stopping...")
                    play_voice(text_to_optimus_voice("Thank you Autobots"))
                    break  # Exit the loop

                # Play back the recognized speech in the Optimus Prime voice
                play_voice(audio_buffer)
            else:
                print("No text recognized, trying again...")

            # Add a small delay before the next input
            time.sleep(1)  # Pause for 1 second

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
