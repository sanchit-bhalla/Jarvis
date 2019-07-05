import pyttsx3       # pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  # sapi5 is used for voices (take ?)
voices = engine.getProperty('voices')
# print(voices[0].id)  use 1 for girl voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I'm jarvis sir. How i help you")

def takeCommand():
    ''' this function take microphone input
        from user and returns string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # You can change other parameters according to your requirements
        audio = r.listen(source)
    try:
        print("Recognising...")
        # instead of google you can use some other also
        query = r.recognize_google(audio, language='en-in')  #en-in --> english-india
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please ...")
        return "None"     #here None is just a string not the actual None used in python

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # 587 is port number
    server.ehlo()
    server.starttls()
    server.login('your  emailaddress', 'Your password')
    server.sendmail('your emailaddress', to, content)
    server.close()
    
if __name__ == "__main__":
    wishme()
    while(True):
        query = takeCommand().lower()

        # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2) # number of sentences you want to speak out
            speak("According to wikipedia")
            #print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "c:\\python programs\\piano_sound"
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) # you can use random funtion to lay random music

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H %m %S")
            speak(f"Time is {strTime}")
        
        elif 'code blocks' in query:
            codepath = "C:\Program Files (x86)\CodeBlocks\codeblocks.exe"
            os.startfile(codepath)

        # you can make a dictionary of names  and corresponding gmail for sending to more people
        elif "mail to receiver" in query:  #here receiver is name of person yu want to send email
            try:
                speak("What should i sent ?")
                content = takeCommand()
                to = "xyz@gmail.com"  # whom you want to sent
                sendEmail(to, content)
                speak("mail has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, i'm unable to send mail for some reasons")

        elif "stop" in query or "end" in query or "close" in query or "exit" in query:
            speak("Thanks for using . Ask anything if you have trouble")
            break

        else:
            speak("Sorry, i can't  understand you")
            speak("Please speak clearly")

            








