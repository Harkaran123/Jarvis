import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour > 0 and hour < 12:
        speak("Good Morning happy")

    elif hour > 12 and hour < 17:
        speak("Good Afternoon happy")

    else:
        speak("Good evening happy")

    speak("Hii happy, how may I help you")

#Listening and Recognizing voice
def take_command():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 5000
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please")
        speak("say that again please or check your speech, you may be giving wrong speech")
        return "None"
    return query

if __name__ == '__main__':

    speak("say the password")
    query = take_command().lower()


    if "12345" in query:

        wish_me()
        while True:
            query = take_command().lower()


            if "wikipedia" in query:

                print("seraching in the internet")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                print("according to wikipedia")
                print(results)
                speak(results)
                speak("any thing else")

            elif "who are you" in query:
                results = "i am ziri, i am here for your service"
                speak(results)
                speak("any thing else")

            elif "are you commited" in query:
                results = "yes, i am commited to my work"
                speak(results)
                speak("any thing else")

            elif "i love you" in query:
                results = "aww so sweet, i love you too but search for a human, as i am a robot"
                speak(results)
                speak("any thing else")

            elif "where do you live" in query:
                results = "i live in your computer"
                speak(results)

            elif "joke" in query:
                results = "i am not yet programmed to say joke, try again in future"
                speak(results)
                speak("any thing else")

            elif "will you marry me" in query:
                results = "i am really sorry, but i am commited to someone else, i cant dump him, thanks"
                speak(results)
                speak("any thing else")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")
                speak("any thing else")

            elif "open google" in query:
                webbrowser.open("google.com")
                speak("any thing else")

            elif "time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {time} happy")
                speak("any thing else")

            elif "open visual studio code" in query:
                codePath = "C:\\Users\\harka\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("any thing else")

            elif "open pycharm" in query:
                pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
                os.startfile(pyPath)
                speak("any thing else")

            elif "open d file" in query:
                dPath = "D:\\"
                os.startfile(dPath)
                speak("any thing else")

            elif "open chrome" in query:
                chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(chromePath)
                speak("any thing else")

            elif "thanks" in query:
                results = "thanks for calling me bye bye take care happy"
                speak(results)
                break

            elif "slow" in query:
                results = "sometimes i become slow, i am sorry"
                speak(results)

    else:
        speak("wrong password, run and try again")


