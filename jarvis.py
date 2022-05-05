import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 180
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohulkumarshrivastava@gmail.com', 'password')
    server.sendmail('mohulkumarshrivastava@gmail.com', to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Hello Kavishankar Sir, our project is ready.")
    elif hour >=12 and hour < 16:
        speak("Good Afternoon Mohul!")
    else:
        speak('Good Eveneing Mohul!')
    
    speak("I am your Personal Assistant . Tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        print("0")
        r.pause_threshold = 0.8
        print("1")
        audio = r.listen(source)
        print("2")
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:

        print("Say that again please.....")
        return "None"
    return query

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)  
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
        
        elif "search youtube" in query:
            query = query.replace("search youtube","")
            result = "youtube.com/results?search_query=" + query
            webbrowser.get(chrome_path).open(result)

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        
        elif "google" in query:
            query = query.replace("google","")
            result = "google.com/search?q=" + query
            webbrowser.get(chrome_path).open(result)
        
        elif 'open website' in query:
            query = query.replace("open website ","")
            webbrowser.get(chrome_path).open(query)
        

        elif 'play music' in query or 'gaana baja' in query:
            music_dir = "E:\\mix tape\\"
            songs = os.listdir(music_dir)
            song_no = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[song_no]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Mohul the time is {strTime}")

        elif 'open vs code' in query:
            speak("Opening VS Code")
            vsCodePath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(os.path.join(vsCodePath))
        
        elif 'open code blocks' in query:
            speak("OPening Codeblocks")
            codeblocks_path = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\CodeBlocks\\CodeBlocks.lnk"
            os.startfile(os.path.join(codeblocks_path))
        
        elif 'say hi to' in query:
            query = query.replace('say hi to','')
            speak(f"Hello {query}, nice to mee you!")


        elif 'send email' in query:
            try:
                speak("Please tell what should i send?")
                content = takeCommand()
                to="mohulkumarshrivastava@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry there was some problem and email could not be sent.")
        
        #elif 'How are you?' in query:
          #  speak("I am good, hope you are great!")

        #elif 'Tell me a joke' in query:
         #   speak("Mrityunjay is a very goo boy. Ha Ha Ha Ha Ha")
        
        elif 'quit' in query or 'assistant you can go' in query or 'by assistant' in query or 'bhai assistant' in query:
            speak('It is always pleasure serving you Sir! Good bye')
            exit()

            


        