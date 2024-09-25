from Extention.speak import *
from Extention.SpeechRecognition import *
from Temperature import *

if __name__ == "__main__":
    startup()
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

     # Logic for executing tasks based on query
        if 'temperature' in query:
            Temp()       