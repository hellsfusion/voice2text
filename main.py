import speech_recognition as sr
from pydub import AudioSegment
import os
from googletrans import Translator  
from datetime import datetime

# supported languages
languages = [
    ["es-ES", "Spanish", "es"],
    ["en-US", "English", "en"],
    ["fr-FR", "Français", "fr"],
    ["de-DE", "Deutsch", "de"],
    ["it-IT", "Italiano", "it"],
    ["pt-BR", "Português", "pt"],
]

# create folders if not exist
if not os.path.exists("./data"):
    os.makedirs("./data")
if not os.path.exists("./transcriptions"):
    os.makedirs("./transcriptions")

# main function
def main():
    # current timestamp to string
    ran = datetime.now().strftime("%Y%m%d%H%M%S")

    # select language
    def language_select(message):
        print('\n-------------------------------------')
        print(message)
        print('-------------------------------------\n')
        for i, lang in enumerate(languages):
            print(f"{i + 1}. [{lang[0]}] {lang[1]}")
        while True:
            try:
                print('\n')            
                language = int(input("(1-" + str(len(languages)) + "): "))
                if 1 <= language <= len(languages):
                    return languages[language - 1]
                else:
                    print("\nInvalid language")
            except ValueError:
                print("\nInvalid language")

    languageInput = language_select('Select the language of the input')
    languageOutput = language_select('Select the language of the output')

    # audio path
    print('\n-------------------------------------')
    print('Enter the path of the audio file')
    print('-------------------------------------')
    audio_path = input(": ")
    audio_path = audio_path.replace('"', '')
    audio_path = audio_path.replace("'", "")
    converted_path = "./data/audio_" + ran + ".wav"

    # file extension
    extension = os.path.splitext(audio_path)[1]

    # convert to wav
    audio = AudioSegment.from_file(audio_path, format=extension[1:])
    audio.export(converted_path, format="wav")
    audio_path = converted_path

    # split audio
    def dividir_audio(audio_path, duracion_fragment=60000):    
        audio = AudioSegment.from_file(audio_path)
        fragments = [audio[i:i + duracion_fragment] for i in range(0, len(audio), duracion_fragment)]
        return fragments

    # recognize audio
    recognizer = sr.Recognizer()

    try:
        # split audio
        fragments = dividir_audio(audio_path, duracion_fragment=60000)

        # process each fragment
        final_text = ""
        for idx, fragment in enumerate(fragments):
            fragment_path = f"./data/fragment_{idx}_{ran}.wav"
            fragment.export(fragment_path, format="wav")
            
            with sr.AudioFile(fragment_path) as source:
                print(f"\nProcessing {idx + 1} of {len(fragments)}...")
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language=languageInput[0])
                final_text += text + " "
            
            # delete temporal file
            os.remove(fragment_path)

        print('\n-------------------------------------')
        print("Transcription Complete:")
        print('-------------------------------------\n')
        # translate / print final text
        if languageInput[2] != languageOutput[2]:
            translator = Translator()
            translated = translator.translate(final_text, dest=languageOutput[2])
            final_text = translated.text
            print(final_text)
        else:
            print(final_text)

        # export to txt
        with open(f"./transcriptions/output_{ran}.txt", "w") as text_file:
            text_file.write(final_text)

        print("\nTranscription Saved: output_" + ran + ".txt")

        if os.path.exists(converted_path):
            os.remove(converted_path)

        # submit another transcription
        print('\n-------------------------------------')
        print("Do you want to submit another file? (y/n)")
        print('-------------------------------------')
        answer = input(": ")
        if answer.lower() == 'y':
            main()
        else:
            exit()

    except Exception as e:
        print(f"\nError : {e}")

main()

