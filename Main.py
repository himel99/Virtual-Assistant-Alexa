# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 00:02:31 2021

@author: ASUS
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('I am your Alexa! What can I do for you?')

def take_command():

    
    print("Listening......")
    voice = listener.listen(source)
    try:
        
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                           
    
    except:
        pass
        
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')       
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who the heck is ' in command:
        person = command.replace('who the hack is', '')
        print(person)
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry I have a headache')
    elif 'single' in command:
        talk('I am in a relationship with WIFI')
    else:
        talk('Please say again! I can not understand you.')

with sr.Microphone() as source:                 
    while True:
         run_alexa()
        

