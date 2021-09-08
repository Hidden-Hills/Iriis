from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import os
import pyttsx3
import pyaudio
import speech_recognition as sr
from werkzeug.wrappers import response


response = ''
app = Flask(__name__)
api = Api(app)




iriis_res = [
    {
        "id": 0,
        "quote": "Ok I am on it"
    }
]


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


class Listen(Resource):
    def get(self, id=0):
        if id == 0:
            return response

        for quote in iriis_res:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not Found", 404