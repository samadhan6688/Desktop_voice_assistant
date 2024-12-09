from tkinter import *
from PIL import ImageTk, Image
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

win = Tk()
win.geometry("1700x900")

def start():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am Sam. Sir, please tell me how may I help you")

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"
        return query

    if __name__ == "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak('yes sir')
                webbrowser.open("youtube.com")
                speak('What is the next order sir?')

            elif 'open google' in query:
                speak('yes sir')
                webbrowser.open("google.com")
                speak('What is the next order sir?')

            elif 'what is time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                speak('What is the next order sir?')

            elif 'open pbl classroom' in query:
                webbrowser.open("https://classroom.google.com/c/NDY5NzkwMDA3NTE3")
                speak('What is the next order sir?')

            elif 'open my class' in query:
                webbrowser.open("https://myclasscampus.com/login")
                speak('What is the next order sir?')

            elif 'open word' in query:
                wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(wordPath)
                speak('What is the next order sir?')

            elif 'open excel' in query:
                excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(excelPath)
                speak('What is the next order sir?')

            elif 'play music' in query:
                mPath = "C:\\Users\\Samadhan\\Music\\mp\\music.m4a"
                os.startfile(mPath)
                speak('What is the next order sir?')

            elif 'no thank you' in query:
                speak('Ok sir, have a nice day!')
                break

            else:
                speak("Sorry, I didn't understand that.")

# Load image for the GUI
load = Image.open("10812389.png")
render = ImageTk.PhotoImage(load)
img = Label(win, image=render)
img.place(x=-300, y=-50)

# Start the voice recognition loop with a button
Button(win, bg="yellow", text="Speak..", padx=25, pady=15, font=("comicsansms", 15, "bold"), command=start).place(x=700, y=10)

win.mainloop()
