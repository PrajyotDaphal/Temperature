from speak import *
from SpeechRecognition import *
import requests
from bs4 import BeautifulSoup

def Temp():
        search = "temperature in Baramati"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")
        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} ")

        else:
            speak("no problem sir")

Temp()