
from gtts import tts
import speech_recognition as sr
import webbrowser
from time import ctime
import time
import os
import playsound
import random
from gtts import gTTS


r = sr.Recognizer()

def record_audio(ask = False):
    if ask:
        alexa_speak(ask)

    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak("Sorry, I didn't get that ")
        except sr.RequestError:
            alexa_speak("Sorry, my speech service is down")
        
        return voice_data



def alexa_speak(audio_string):
    tts = gTTS(text = audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('my name is alexa')
    
    if 'search' in voice_data:
        search = record_audio('What do you want to search for ?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        alexa_speak("Here is what i found for " + search)

    if 'location' in voice_data:
        location = record_audio('What is the location you want to search for ?')
        url = 'https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        alexa_speak("Here is the location of " + location)
    if 'exit' in voice_data:
        exit()
    else:
        alexa_speak("Sorry, I didn't get that! ")
 

time.sleep(1)
alexa_speak('How can i help you ! ')

while 1:
    voice_data = record_audio()
    respond(voice_data)
