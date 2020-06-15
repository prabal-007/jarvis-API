import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning sir")
    elif 12 <= hour <= 18:
        speak("Good Morning sir")
    else: speak("Good Evening")


def takeCommand():
    '''
    it takes microphone input from user and returns stringoutput
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.6
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print("please say that again...")
        return "None"
    return query

def sendEmail(to, content):
     



if __name__ == '__main__':
    wishMe()
    maildict = {"prabal": "gprabal000@gmail.com", "srijan": "srijansharma2k@gmail.com"}
    while True:
        query= takeCommand().lower()

        # logic for performing taks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accouding to wikipedia ")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open python' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'send email' in query:
            try:
                speak("to whome..")
                rName = takeCommand()
                if f"{rName}" in query:
                    for name,mail in maildict:
                        maildict[rName] = mail
                        content = takeCommand()
                        sendEmail(mail, content)
                        speak(f"email has been sent to {name}")
                else:
                    print("no such email in contacts..")
            except Exception as e:
                speak("can't send the mail")

