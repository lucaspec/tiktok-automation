from PIL import Image
import pytesseract
import pyttsx3
from pydub import AudioSegment
import os

# Path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on the image
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    # Remove line breaks from the text
    cleaned_text = text.replace('\n', ' ')
    return cleaned_text

# Function to generate MP3 from text using pyttsx3
def save_text_as_mp3(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 180)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty('voices')

    # Print available voices
    #for voice in voices:
    #    print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

    # You can set a specific voice using the voice's ID
    engine.setProperty('voice', voices[1].id)  # Example: Set to the second voice in the list

    # Convert text to speech
    engine.save_to_file(text, output_file)

    # Wait for the speech to finish
    engine.runAndWait()


if __name__ == "__main__":
    # Replace 'texts/exp1.png' with the path to your image file
    image_path = 'texts/exp1.png'

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print(extracted_text)

    # Replace 'output.mp3' with the desired output path for the generated MP3 file
    mp3_output_path = 'tts/exp1.mp3'

    # Generate MP3 from the extracted text
    save_text_as_mp3(extracted_text, mp3_output_path)
    print(f"saving mp3 file into {mp3_output_path}")