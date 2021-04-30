import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Sorry, I do not understand')
        except sr.RequestError:
            alexa_speak('Sorry, connection error')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Alther EGO')
    if 'what time is it' in voice_data:
        alexa_speak(ctime())
    if 'what is your favorite animal' in voice_data:
        alexa_speak('My favorite animal is cat')
    if 'what is your favorite song' in voice_data:
        alexa_speak('My favorite song is Lemon')
    if 'search' in voice_data:
        buscar = record_audio('what do you search?')
        url = 'https://www.google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('This is what I found: ' + buscar)
    if 'place' in voice_data:
        lugar = record_audio('what place?')
        url = 'https://www.google.nl/maps/place/' + lugar + '/&amp'
        webbrowser.get().open(url)
        alexa_speak('This is what I found: ' + lugar)
    if 'finish' in voice_data:
        exit()

time.sleep(1)
alexa_speak('can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
