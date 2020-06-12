import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import sys
import random 
  
engine = pyttsx3.init('sapi5')      #sapi5 is a speech Application Programming Interface(API) developed by Microsoft   
voices = engine.getProperty('voices') #you can you other voice according to your choice
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning BOSS!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon BOSS!")   

    else:
        speak("Good Evening BOSS!")  

    speak("hello , I am friday sir , please tell me how may i help you")
    speak("Welcome To Iron Region")
    speak("What you like to do today")
 


          

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
    




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password') #you email and password
    server.sendmail('anotherpersonemail@gmail.com', to, content)  #that person whom you want to send an email
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #If you want more sentences, change the value of sentences
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "repeat" in query:                      #Repeat what you said
            speak('repeating')
            print('repeating..........')
            query = query.replace('repeat', "")
            print(query)
            speak(query)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'photos' in query:
            photoPath = "D:\\facebook"
            os.startfile(photoPath)
            


        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[401]))  # put the directory of music file and you can use random function play a random music 
        
        elif 'open cmd' in query:
            cmd_Path = "C:\\Windows\\system32\\Cmd.exe"                       #path of cmd.exe
            speak("opening cmd")
            os.startfile(cmd_Path)

        elif "think" in query:
            f=open("think.txt","r")       #make a think.txt file in current directory and put some lines
            lines= f.readlines()
            read_line= random.randint(0,2)     #Randomely select any line ***carefully put maximum line value***
            print(lines[read_line])
            speak(lines[read_line])

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to person' in query:        #in place of person use name of that person       
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "persons98@gmail.com"    #use person email to send an email
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir right now I am not able to send this email")




        if 'sys'in query: 
            speak("Ok Boss,Have a good day")
            speak("I'm going to take a rest")
            print("Ok Boss,Have a good day")
            quit=sys.exit()                #Here I am using sys.exit(),you can use break statement also