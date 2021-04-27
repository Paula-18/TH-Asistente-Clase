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
            print('Lo siento, no te entedi')
        except sr.RequestError:
            print('Lo siento, error de conexión')
        return voice_data

def respond(voice_data):
    if 'como te llamas' in voice_data:
        print('Mi nombre es Alther EGO')
    if 'Hora' in voice_data:
        print(ctime())
    if 'Buscar' in voice_data:
        buscar = record_audio('¿Que necesitas buscar?')
        url = 'https://www.google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Es lo que encontre para: ' + buscar)
    if 'Lugarcl' in voice_data:
        lugar = record_audio('¿Que lugar?')
        url = 'https://www.google.nl/maps/place/' + lugar + '/&amp'
        webbrowser.get().open(url)
        print('Es lo que encontre para: ' + lugar)

time.sleep(1)
print('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)