import aiml
import os
import pyttsx3
import speech_recognition as sr


engine=pyttsx3.init()
kernel = aiml.Kernel()
kernel.learn("sample.aiml")
kernel.respond("load aiml b")


while True :

 message = " "   
  #message = input(">>")
 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Say Something")
  audio = r.listen(source)
 try:
  message = r.recognize_google(audio)
 except sr.UnknownValueError:
   print("Google Speech Recognition could not understand audio")
   #except sr.RequestError as e:
    #print("Could not request results from Google Speech Recognition service; {0}".format(e))  
     
 if message == "quit" :
    print("Ok you want to quit , Bye")
    engine.say("Ok you want to quit , Bye")
    engine.runAndWait()
    exit()
 else :
    print(kernel.respond(message))
    engine.say(kernel.respond(message))
    engine.runAndWait()
    
