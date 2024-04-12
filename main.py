import speech_recognition as sr
import webbrowser
import urllib.parse
import json
import os
import pyfiglet
from colorist import Color, green, yellow, red

appsFile = json.load(open("apps.json"))
apps = [app[0] for app in appsFile]
paths = [path[1] for path in appsFile]
processes = [process[2] for process in appsFile]
recognizer = sr.Recognizer()
microphone = sr.Microphone()
result = pyfiglet.figlet_format("VNSH INC", font = "slant" )

red(f'{result}')
print("Listening...")
def voice_assistant():

    try:
        while True:
            with microphone as source:
                audio_data = recognizer.listen(source)
            keyphrase = 'vanish'
            audio = recognizer.recognize_google(audio_data, language="en-US")
            if keyphrase in audio.lower():
                command = audio.lower().split(keyphrase)[1].strip().split()
                yellow("Command Recognized")
                cmdHandler(command)
    except sr.UnknownValueError:
        voice_assistant()
    except KeyboardInterrupt:
        red("Voice assistant stopped.")

def cmdHandler(command): 
    if 'open' in command[0]:
        os.system("start " + paths[apps.index(command[1])])
        green(f"Opening {command[1]}.")
        print("Resuming Listening...")
    elif 'search' in command[0]:
        lookup = ' '.join(command[1:])
        webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(lookup)}")
        green(f"Looking up '{lookup}'.")
        print("Resuming Listening...")
    elif 'close' or 'clothes' in command[0]:
        os.system("taskkill /im " + processes[apps.index(command[1])] + " /f")
        green(f"Closing {command[1]}.")
        print("Resuming Listening...")
voice_assistant()