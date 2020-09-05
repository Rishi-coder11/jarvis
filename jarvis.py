import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import datetime
import os
import time
import wikipedia
import webbrowser
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sikhrishi@gmail.com', 'Rishi@2010')
    server.sendmail('sikhrishi@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()
            # open websites
            if 'open youtube' in query:
                webbrowser.open("youtube.com")   
            elif 'open connect' in query:
                webbrowser.open("connectline.herokuapp.com/python")
            # time
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"The time is {strTime}")
            # wikipedia
            elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
            # play music
            elif 'play music' in query:
                music_dir = 'C:\\Users\\Rishi Sikh\\Downloads\\Student Of The Year 2 (2019) Mp3 Songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            # open programs
            elif 'open vs code' in query:
                codePath = "C:\\Users\\Rishi Sikh\\Downloads\\VSCodeUserSetup-x64-1.47.3.exe"
                os.startfile(codePath)
            elif 'open zoom' in query:
                codePath = "C:\\Users\\Rishi Sikh\\Downloads\\ZoomInstaller.exe"
                os.startfile(codePath)
            # emails
            elif 'email to rishi' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()       
                    to = "sikhrishi@gmail.com" 
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Rishi. I am not able to send this email")
            elif 'email to dad' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()       
                    to = "satinderpals@gmail.com" 
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Rishi. I am not able to send this email")
            elif 'email to mom' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()       
                    to = "tarvindars@gmail.com" 
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Rishi. I am not able to send this email")
            elif 'email to krish' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()       
                    to = "8057964018@mms.att.net" 
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Rishi. I am not able to send this email")



                except Exception as e:
                    print(e)
                    speak("Sorry my friend Rishi. I am not able to send this email")
            # quit
            elif 'thank you jarvis' in query:
                speak("Your welcome!")
                print("Your welcome!")
            elif 'jarvis quit' in query:
                    print("Thank you for your time!")
                    speak("Thank you for your time!")
                    sys.exit()                    
            