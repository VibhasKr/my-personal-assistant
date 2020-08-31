import os
import pyttsx3
import speech_recognition as speech
import datetime
import wikipedia
import webbrowser

def speak(a):
    pyttsx3.speak(a)
    print(a)

def open():
    a="launching "+s
    speak(a)
    os.system(s)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")
    
    speak("I am your own personal assistant!")

def Command():
    c = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        c.pause_threshold = 1
        audio = c.listen(source)

    try:
        print("Recognizing...")
        query = c.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Pardon sir! Please repeat:)...")
        return "None"
    return query

if __name__ == "__main__":
    wish()
    while True:
        speak("chat with me with your requirements:")
        p = Command()
        p=p.lower()

        if((("not " in p) or ("don't" in p))):
            speak(("ask without negation"))

        elif 'wikipedia' in p:
            speak('Searching Wikipedia...')
            p = p.replace("wikipedia", "")
            result = wikipedia.summary(p, sentences=4)
            speak("According to Wikipedia"+result)

        elif 'open youtube' in p:
            webbrowser.open("youtube.com")

        elif 'open google' in p:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in p:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in p:
            music = 'D:\\songs'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[0]))

        elif ' time ' in p:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}\n")

        elif (("run" in p) or ("start" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("browser" in p) or ("chrome" in p)):
            speak("Chrome is set as default browser\nif you want to use another browser type the name of browser in the statement")
            open("chrome")

        elif(("run" in p) or ("start" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and  (("notepad" in p) or ("editor" in p) ) :
            open("notepad")

        elif(("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("player" in p) and ("media" in p):
            open("wmplayer")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("calculator" in p) :
            open("calc")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("paint" in p) :
            open("mspaint")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("keyboard" in p) :
            open("osk")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("vlc" in p) :
            open("vlc")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("firefox" in p):
            open("firefox")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("internet explorer" in p):
            open("iexplore")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("word " in p):
            open("WINWORD")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("excel" in p):
            open("EXCEL")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("powerpoint" in p):
            open("POWERPNT")

        elif (("run" in p) or  ("start" in p) or  ("execute" in p) or ("launch" in p) or ("open" in p)) and ("wordpad" in p):
            open("wordpad")

        elif  (("exit" in p)  or ("quit" in p)):
            speak("Signing off\nWish for your best sir")
            break
        else:
            print("please try again with better input")
            pyttsx3.speak("please try again with better input")


