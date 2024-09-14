import pygame
import tempfile


# Initialize pygame for audio playback
pygame.mixer.init()

# Function to play the audio
def play_voice(audio_buffer):
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
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Playback finished.")

    except Exception as e:
        print(f"An error occurred during playback: {e}")
