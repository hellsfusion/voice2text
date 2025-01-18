# Audio Transcription and Translation Script

This Python script performs audio transcription and translation. It allows users to transcribe audio files to text in a selected input language, and then optionally translates the transcribed text into another language.

## Features

- Convert audio files into the .wav format.
- Split long audio files into smaller segments for efficient processing.
- Use the Google Speech Recognition API for audio transcription.
- Translate the transcribed text into a different language using Google Translate API.
- Save the transcriptions and translations as text files.

## Requirements

To run this script, you need to install the following Python packages:

- speech_recognition: For recognizing speech from audio.
- pydub: For manipulating audio files (e.g., conversion to `.wav` and splitting).
- googletrans: For translating the transcribed text into another language.
- os: For handling file and directory operations.
- datetime: For generating timestamps for file names.
- ffmpeg: For handling media files

## Installation

1. Clone this repository to your local machine.

2. Make sure you have the necessary Python dependencies installed.

    pip install -r requirements.txt

3. Install ffmpeg, in windows you can install it with chocolatey by: choco install ffmpeg 

## Usage

### Step 1: Select Input and Output Language
When you run the script, you will be prompted to select:
- The language of the input audio.
- The language to which you want to translate the transcribed text.

Supported languages:
- Spanish (es-ES)
- English (en-US)
- French (fr-FR)
- German (de-DE)
- Italian (it-IT)
- Portuguese (pt-BR)

### Step 2: Provide Audio File Path

After selecting the languages, the script will prompt you to enter the path of the audio file you want to transcribe.

The script accepts audio files in various formats (e.g., MP3, WAV). The audio file will be automatically converted to .wav if necessary.

### Step 3: Transcription and Translation

The audio file will be split into smaller segments (if necessary), and each segment will be transcribed using Google’s Speech Recognition API. If a different output language is selected, the transcribed text will be translated using Google Translate API.

### Step 4: Save the Transcription

The transcribed (and possibly translated) text will be saved as a .txt file in the ./transcriptions directory. The file will be named output_<timestamp>.txt.

### Step 5: Submit Another File (Optional)

After the transcription is complete, the script will ask if you want to transcribe another file. You can type (y) to process another file or (n) to exit the script.

## Troubleshooting

- Make sure your audio file path is correct.
- Ensure that all required dependencies are installed.
- If you encounter errors, check the Python version and package versions to ensure compatibility.
