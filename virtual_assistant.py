import pyttsx3#used for converting text to speech #pip install pyttsx3
import datetime
import smtplib#email
import speech_recognition as sr#pip install SpeechRecognition
from email.message import EmailMessage
import pyautogui#api for whatsapp#pip install pyautogui
import webbrowser as web
from time import sleep
import wikipedia#pip install wikipedia
import pywhatkit 
from newsapi import NewsApiClient
import pyjokes
import requests
from nltk.tokenize import word_tokenize



engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")#hour=I,Min=M,Sec=S
    speak("the current time is:")
    speak(Time)
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is:")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good Morning Sir!")
        
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir!")
        
    elif hour>=18 and hour <24:
        speak("Good Evening Sir!")
        
    else:
        speak("Good Night Sir!")
        
def wishme():
    speak("Wellcome back sir!")#its spelling it in a weird way so we writing wellcome
    time()
    date()
    greeting()
    speak("Jarvis at your service,please tell me how can I help")
    
def takeCommandCMD():
    query=input("please tell me how can i help you?\n")
    return query

def takeCommandMIC():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-IN")
        print("User said : "+query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return"None"
    return query
    

def sendEmail(receiver,subject,content):
    senderemail='#enter email id'
    epwd='#enter password'
    
    server=smtplib.SMTP('smtp.gmail.com',587)    
    server.starttls() 
    server.login(senderemail,epwd)
    email= EmailMessage()
    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email)
    server.close()
     
 
def sendwhatsmsg(phone_no,message):
    Message=message
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what should i search for')
    search = takeCommandMIC()
    web.open('https://www.google.com/search?q='+search)
    
def news():
       newsapi=NewsApiClient(api_key='71c85db587c24982aadf9b12a8e6d6dc')
       speak('what news do you want?')
       topic=takeCommandMIC()
       data = newsapi.get_top_headlines(q=topic,language='en',page_size=5)
       newsdata=data['articles']
       for x,y in enumerate(newsdata):
           print(f'{x}{y["description"]}')
           speak(f'{x}{y["description"]}')


if __name__=="__main__":
    print("Hello, I am Jarvis your virtual assistant,how can I help you")
    speak("Hello, I am Jarvis your virtual assistant,how can I help you")

    #getvoices(1)
    #wishme()
 
    wakeword="jarvis"
    while True:
        query=takeCommandMIC().lower()
        query=word_tokenize(query)
        print(query)
        if wakeword in query:
        
            if 'time' in query:
                time()
                    
            elif 'date' in query:
                date()
            
            elif 'email' in query:
                email_list={
                 #enter email ids here
                   }
                try:
                    speak("To whom do you want to send the mail?")
                    name=takeCommandMIC()
                    receiver=email_list[name]
                    speak("What is the subject?")
                    subject=takeCommandMIC()
                    speak('What should I send?')
                    content=takeCommandMIC()
                    sendEmail(receiver,subject,content)
                    speak("Email has been sent")
                
                except Exception as e:
                    print(e)
                    speak("unable to send the email")
            
                
            elif 'message' in query:
                user_name={#enter numbers here
                    }
                try:
                    speak("To whom do you want to send the whatsapp message?")
                    name=takeCommandMIC()
                    phone_no=user_name[name]
                    speak("What is the message?")
                    message=takeCommandMIC()
                    sendwhatsmsg(phone_no,message)
                    speak("Whatsapp message has been sent")
                
                except Exception as e:
                    print(e)
                    speak("unable to send the whatsapp message")
            
            
            elif 'wikipedia' in query:
                speak('searching on wikipedia')
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences = 4)
                print(result)
                speak(result)
            
            
            elif 'google' in query:
                searchgoogle()
                
            elif 'youtube'in query:
                speak('what should i play')
                topic=takeCommandMIC()
                pywhatkit.playonyt(topic)
            
            elif 'news' in query:
                news()
            
            elif'weather'in query:
                speak("Which city's weather information do you need?")
                url='https://api.openweathermap.org/data/2.5/weather?q=city&units=imperial&appid=7a83a9d0087f69c50ef136ce5ce73c46'
                city=takeCommandMIC().lower()
                res= requests.get(url)
                data=res.json()
                weather=data['weather'][0]['main']
                temp=data['main']['temp']
                desp=data['weather'][0]['description']
                temp=round((temp-32)*5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(weather)
                speak(temp)
                speak(desp)
            
            elif 'remember' in query:
                speak("What should i remember?")
                data=takeCommandMIC()
                speak("you have asked me to remember that"+data)
                remember=open('data.txt','w')
                remember.write(data)
                remember.close()
                
            elif 'do i have something' in query:
                remember=open('data.txt','r')
                speak("you told me to remember that"+remember.read())
            
            elif 'instagram' in query:
                web.open("instagram.com")
            
            
            elif 'joke' in query:
                speak(pyjokes.get_joke())    
            
            elif 'offline' in query:
                quit()
                
