import speech_recognition as sr
import time 
import webbrowser
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
            print('Sorry, I do not understand')
        except sr.RequestError:
            print('Sorry, connection error')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name Alther EGO')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        buscar = record_audio('what do you search?')
        url = 'https://www.google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('This is what I found: ' + buscar)
    if 'place' in voice_data:
        lugar = record_audio('what place?')
        url = 'https://www.google.nl/maps/place/' + lugar + '/&amp'
        webbrowser.get().open(url)
        print('This is what I found: ' + lugar)

time.sleep(1)
print('how can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
