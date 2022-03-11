import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print(" recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)#adjust index to change mail female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)#adjust speaking speed
    engine.say(x)
    engine.runAndWait()

sptext()
speechtx("jai mata di")

if __name__=='__main__':
    if "hey harshal" in sptext().lower():
        while True:
            data1=sptext().lower()

            if "your name" in data1:
                name="my name is harshal"
                speechtx(name)

            elif "old are you" in data1:
                age="i am 1 day old"
                speechtx(age)