import datetime
import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am jarvis sir . Please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogninzing..")
        query=r.recognize_google(audio , language="en")
        print(f"user said:{query}\n:")
    
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "none"

    return query

def sendemail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',535)
    server.ehlo()
    server.starttls()
    server.login('dedgeyashraj13@gmail.com','Lamborghini@13')
    server.sendmail("dedgeyashraj13@gmail.com", to , content)
    server.close()


if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open movies' in query:
            webbrowser.open('mkvcinemas.cymru')
        
        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'play music' in query:
            music_dir ='D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'what is the time' in query :
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time}")

        elif 'open vs code' in query:
            path="C:\\Users\\Yashraj Dedge\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif 'send email' in query:
            try:
                speak("What should i say")
                content = takecommand()
                to = "dedgeyashraj13@gmail.com"
                sendemail(to,content)
                speak("Email has been sent !")
            except Exception as e :
                print(e)
                speak("Sorry Sir. I am not able to send the mail")

        