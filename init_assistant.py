
#Copyright (C) May Realities, Inc. All Rights Reserved

#Iriis (C) Voice Controlled AI

from sys import dllhandle
from pyttsx3 import engine
import speech_recognition as sr
import os.path
from gtts import gTTS
import datetime
import warnings
import webbrowser
import smtplib
import wolframalpha
import ecapture
import email
import re
import pyttsx3
import pyaudio
import subprocess
import pywhatkit
import youtube_dl
import pyowm
import json
import calendar
import random
import wikipedia




warnings.filterwarnings('ignore')

    
def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('I didnt understand you')
    except sr.RequestError as e:
        print('Request Results ' + e)
        
    return data

    
def assistantResponse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)


def wakeWord(text):
    WAKE_WORDS = ['hey iris']

    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-list.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])



def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                       '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21th', '22nd', '23rd', '24th', '25th',
                       '26th', '27th', '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinal_numbers[dayNum - 1] + '. '




def greeting(text):
    GREETING_INPUTS = ['hey iris']

    GREETING_RESPONSES = ['What do you need' ]

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    return ''

def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]




while True:

    text = recordAudio()
    response = ''

    if (wakeWord(text) == True):

        response = response + greeting(text)

        if('date' in text):
            get_date = getDate()
            response = response + ' '+get_date

        if('write this' in text):
            now = datetime.datetime.now()
            note_text = recordAudio.lower()
            note(note_text)
            print('Note Taken')



        if('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >=12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)

            response = response +' It is '+str(hour)+ ':'+ minute+ ' '+meridiem+ '.'

        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if('open google' in text):
            webbrowser.open_new_tab("google.com")
            print("Enjoy!")

        if('weather' in text):
            subprocess.Popen("weather.mayrealities.com")
      
        if('Bye Iris' in text):
            quit()
           
            
        assistantResponse(response)

