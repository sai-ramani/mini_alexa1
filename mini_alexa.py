import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date

engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer = sr.Recognizer()

def engine_speak(text):
        engine.say(text)
        engine.runAndWait()

def run_alexa():
        with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration = 1)
                print("Start speeking ...")
                engine_speak("Listening...")
                print("Listening...")
                audio = recognizer.listen(source)
        try:
                print("Recognizing....")
                command = recognizer.recognize_google(audio,language='en-in')
                command = command.lower()
                if "alexa" in command:
                    command = command.replace('alexa','')
                    print("you said: ",command)
                else:
                    print("you said: ",command)
                if 'hello' in command:
                    print("Hello ! how can I help you ?")
                    engine_speak("Hello ! how can I help you ?")
                elif 'who are you' in command:
                    print("Hi I am mini alexa, your virtual assistant,how can i help you?") 
                    engine_speak("Hi I am mini alexa, your virtual assistant,how can i help you?") 
                elif 'you do' in command:
                    print("I can play music on youtube, search on wikipedia, say current date and time, tell a joke, find your location, open different websites like gmail, instagram, github and search on google")
                    engine_speak("I can play music on youtube, search on wikipedia, say current date and time, tell a joke, find your location, open different websites likegmail, instagram, github and search on google")
                elif 'play' in command:
                    song = command.replace('play','')
                    print("playing :",song)
                    engine_speak('playing '+song)
                    pywhatkit.playonyt(song)
                elif 'date and time' in command:
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    d2 = today.strftime('%B %d,%Y')
                    print("Today's date is",d2,"Current time is",time)
                    engine_speak("Today is: "+d2)
                    engine_speak("and current time is: "+time)
                elif 'time and date' in command:
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    d2 = today.strftime('%B %d,%Y')
                    print("Today's date is",d2,"Current time is",time)
                    engine_speak("current time is: "+time)
                    engine_speak("and Today's date is: "+d2)    
                elif 'time' in command:
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print("Time is:",time)
                    engine_speak("Time is")
                    engine_speak(time)
                elif 'date' in command:
                    today = date.today()
                    d2 = today.strftime('%B %d,%Y')
                    print("Date is: ",d2)
                    engine_speak("Date is "+d2)
                elif 'tell me about' in command:
                    name = command.replace('tell me about','')
                    info = wikipedia.summary(name,1)
                    print(info)
                    engine_speak(info)
                elif 'what is' in command:
                    name = command.replace('what is','')
                    info = wikipedia.summary(name,1)
                    print(info)
                    engine_speak(info)
                elif 'who is' in command:
                    name = command.replace('who is','')
                    info = wikipedia.summary(name,1)
                    print(info)
                    engine_speak(info)
                elif 'joke' in command:
                    _joke = pyjokes.get_joke()
                    print(_joke)
                    engine_speak(_joke)
                elif 'search' in command:
                    search = "https://www.google.com/search?q="+command
                    engine_speak("Searching...") 
                    webbrowser.open(search)
                elif 'my location' in command:
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.open(url)   
                    engine_speak("You must be somewhere near here, as per google maps") 
                elif 'open gmail' in command:
                    print("opening gmail...")
                    engine_speak("opening gmail...")
                    webbrowser.open_new("https://mail.google.com/")
                elif 'open youtube' in command:
                    print("opening youtube...")
                    engine_speak("opening youtube...")
                    webbrowser.open_new("https://www.youtube.com/")  
                elif 'open instagram' in command:
                    print("opening instagram...")
                    engine_speak("opening instagram...")
                    webbrowser.open_new("https://www.instagram.com/")
                elif 'github' in command:
                    print("opening github..")
                    engine_speak("opening github...")
                    webbrowser.open_new("https://www.github.com/")
                elif 'open google' in command:
                    print("opening google")
                    engine_speak("opening google")
                    webbrowser.open_new("https://www.google.com/")
                elif 'bye' in command:
                    print("Good Bye...")
                    engine_speak("good bye.....,have a nice day")
                    sys.exit()
                elif 'thank you' in command:
                    print("Your Welcome..")
                    engine_speak("Your Welcome")
                elif 'stop' in command:
                    print("Good bye...")
                    engine_speak("Good bye,have a nice day")
                    sys.exit()                      
                else:
                        print("here what i found on the internet!")
                        engine_speak("here what i found on the internet!")
                        search = "https://www.google.com/search?q="+command
                        webbrowser.open(search)
        except Exception as ex:
                print(ex)
print("clearing background noise, please wait!")
engine_speak("clearing background noise, please wait!") 
print("hello i am mini alexa ! how can i help you?")
engine_speak("hello i am mini alexa ! how can i help you?")  
while True:
    run_alexa()                         
                                                        

