import speech_recognition as sp_recog
from time import sleep


def capture_audio():
    recog = sp_recog.Recognizer()

    audio_file = sp_recog.AudioFile('nnenna.wav')
    with audio_file as source:
        recog.pause_threshold = 1
        recog.adjust_for_ambient_noise(source)
        audio = recog.record(source)
        print("Recognizing your speech...")

    try:
        audio_text = recog.recognize_google(audio, language='en-Us')
        sleep(1)
        print("\n")
        print(audio_text)

    except Exception as e:
        print("An error occurred. Please ensure internet connection")

        return "None"

    return audio_text

audio_text = capture_audio()
sleep(10)
print("Exiting the program now")
sleep(3)
