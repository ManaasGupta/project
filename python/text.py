import speech_recognition as sr

def text():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Specify the audio source (e.g., microphone or audio file)
    # For microphone input, you may need to install PyAudio library: pip install pyaudio
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)
        print("Time over, thank you")

    # Perform speech recognition
    try:
        text = r.recognize_google(audio)
        print("Recognized Text:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
    return text