#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import webbrowser 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()
 
#def speak(audioString):
#    print(audioString)
#    tts = gTTS(text=audioString, lang='en')
#    tts.save("audio.mp3")
#    os.system('mpg321 audio.mp3 -quiet')
    
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
            engine.say("I am fine")
            engine.runAndWait()
            print("I am fine")
    if "what time is it" in data:
          engine.say(ctime())
          engine.runAndWait()
          print(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        engine.say("Hold on Frank, I will show you where " + location + " is.")
        #os.system("chrome-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open('https://www.google.com/maps/place/' + location +"/&amp;")
        engine.runAndWait()
    if "quit" in  data:
         engine.say("Ok bye, see you later")
         print("Ok bye, see you later")
         engine.runAndWait()
         exit()
# initialization
time.sleep(2)
engine = pyttsx3.init()
engine.say("Hi Frank, what can I do for you?")
engine.runAndWait()
while 1:
    data = recordAudio()
    jarvis(data)
