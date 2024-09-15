import os
import pygame
import tempfile

# Initialize pygame for audio playback
pygame.mixer.init()

# Function to play the audio
def play_voice(audio_buffer):
    temp_audio_file_path = None
    try:
        if audio_buffer is None:
            print("No audio data to play.")
            return

        # Create a temporary file to save the MP3 data
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_audio_file.write(audio_buffer.getvalue())
            temp_audio_file_path = temp_audio_file.name

        # Play the MP3 file using pygame
        pygame.mixer.music.load(temp_audio_file_path)
        pygame.mixer.music.play()
        
        # Wait for the music playback to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Playback finished.")

    except Exception as e:
        print(f"An error occurred during playback: {e}")

    finally:
        # Unload the music to free up the file
        pygame.mixer.music.unload()

        # Ensure the file is deleted after playback completes
        if temp_audio_file_path and os.path.exists(temp_audio_file_path):
            try:
                os.remove(temp_audio_file_path)
                # print(f"Temporary file {temp_audio_file_path} deleted.")
            except Exception as delete_error:
                print(f"An error occurred while deleting the file: {delete_error}")

