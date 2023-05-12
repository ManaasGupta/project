import pyttsx3
def speech(statment:str):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties for the speech
    engine.setProperty('rate', 130)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 

    # Enter the text you want to convert to speech

    # Convert the text to speech
    engine.say(statment)

    # Wait until the speech is complete
    engine.runAndWait()
