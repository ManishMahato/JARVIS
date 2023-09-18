import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import numpy as np

# pyttsx3 -> A python library that will help us to convert text to speech.
# It works offline, and it is compatible with Python 2 as well as Python 3

# choosing MS-speech recognition API (sapi)
engine = pyttsx3.init('sapi5')

# Getting current voices of system
voices= engine.getProperty('voices') 

# Voice id helps us to select different voices.
# voice[0].id = Male voice 
# voice[1].id = Female voice
# setting male voice for jarvis----'0'->DAVID & '1'->ZIRA-----
engine.setProperty('voice', voices[0].id) 

# Initialize the recognizer
r = sr.Recognizer()

# JARVIS to speak using speak func
def speak(audio):
    # processing context & Jarvis speaks the content
    engine.say(audio) 
    engine.runAndWait()

# Jarvis greets
def wish():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")
    
# With the help of the takeCommand() function, 
# our A.I. assistant will return a string output by taking microphone input from the user.
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        # seconds of non speaking audio before a phrase is considered complete.
        r.adjust_for_ambient_noise(source, duration=0.5)
        # Adjusts the energy threshold dynamically using audio from ``source``
        # The ``duration`` parameter is the maximum number of seconds that it will dynamically 
        # adjust the threshold for before returning. 
        # This value should be at least 0.5 in order to get a representative sample of the ambient noise.
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        # speech recognition & language is Indian English
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# We will create a main() function, and inside this main() Function, we will call our speak function.
if __name__ == "__main__":
# Loop infinitely for user to speak
    while(1):   
        wish()
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 
            
        elif 'play music' in query:
            music_dir = 'D:\\UCDownloads'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[np.random.randint(low=0,high=10)]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'quit' or 'bye' in query:
            exit()