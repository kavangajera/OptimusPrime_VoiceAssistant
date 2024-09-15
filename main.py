import time
import speech_recognition as sr
from speech_to_text import listen_and_recognize, text_to_optimus_voice
from text_to_speech import play_voice
import webbrowser
import os
from datetime import datetime
from genai import chat_session
from news import fetch_news
# Function to open websites based on recognized text
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
firefox = webbrowser.get('firefox')
def open_website(command):
    # Define a mapping of site names to URLs
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "twitter": "https://twitter.com",
        "github": "https://github.com",
        "wikipedia":"https://www.wikipedia.org/",
        "chat GPT":"https://chatgpt.com/",
        "student panel":"https://egov.ddit.ac.in/index.php?r=site/login",
        
        # Add more sites as needed
    }

    # Find if a known site is in the command
    for site_name, url in sites.items():
        if site_name.lower() in command.lower():
            if site_name == "student panel":
                play_voice(text_to_optimus_voice("Opening e.g.o.v , Sir!"))
                firefox.open(url)
                return True
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
                elif "optimus" in recognized_text.lower() and "news" in recognized_text.lower() and "sports" in recognized_text.lower():
                    title = fetch_news("sports")
                    play_voice(text_to_optimus_voice(title))
                    
                # Step 4: Check if the user wants to stop the program
                elif "optimus" in recognized_text.lower() and "stop" in recognized_text.lower():
                    print("Optimus is stopping...")
                    play_voice(text_to_optimus_voice("Thank you Autobots"))
                    break  # Exit the loop
                elif "optimus" in recognized_text.lower() and "music" in recognized_text.lower():
                    play_voice(text_to_optimus_voice("Playing , music of my kind"))
                    os.startfile(r"C:\Users\kavan\OneDrive\Documents\Rockstar Games\GTA V\User Music\pokemon theme song.mp3")
                    break
                elif "optimus" in recognized_text.lower() and "time" in recognized_text.lower():
                    now = datetime.now()
                    formatted_time = now.strftime("%I:%M %p")
                    
                    play_voice(text_to_optimus_voice(formatted_time))
                    
                elif "optimus" in recognized_text.lower():
                    response = chat_session.send_message(recognized_text[8:])
                    play_voice(text_to_optimus_voice(response.text))
                
                # play_voice(audio_buffer)
            else:
                print("No text recognized, trying again...")

            # Add a small delay before the next input
            time.sleep(1)  # Pause for 1 second

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
