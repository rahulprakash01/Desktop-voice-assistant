
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser 
import requests
import geocoder
import pyautogui 
import os
import keyboard
import pywhatkit
import wikipedia

from os import startfile
from playsound import playsound
from pyautogui import click
from keyboard import press 
from keyboard import write
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am personal voice assistant. Please tell me how may I help you")    

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
    
def whatsappMSG(name,message):
    
    startfile("C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15)
    click(x=273, y=138)
    sleep(2)
    write(name)
    sleep(2)
    click(x=225, y=296)
    write(message)
    press('enter')
 
def WhatsappCall(name):
    startfile("C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=273, y=138)
    sleep(2)
    write(name)
    sleep(2)
    click(x=225, y=296)   
    click(x=1711, y=67)
    
def WhatsappvideoCall(Name):
    startfile("C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=273, y=138)
    sleep(2)
    write(name)
    sleep(2)
    click(x=225, y=296)
    click(x=1649, y=71)
def screenshot():
    speak("Ok Boss , What Should I Name That File ?")
    path = takeCommand()
    path1name = path + ".png"
    path1 = "C:\\Users\\Dell\\OneDrive\\Pictures\\Screenshots\\"+ path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\Dell\\OneDrive\\Pictures\\Screenshots")
    speak("Here Is Your ScreenShot")     
    
    
def SpeedTest():
    import speedtest
    speak("Checking speed...")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)
    
    if 'uploading' in query:
        speak(f"The uploading speed is {correctUpload} mbp s")
    
    elif 'downloading' in query:
        speak(f"The Downloading speed is {correctDown} mbp s")
        
    else:
            speak(f"The Downloading is {correctDown} and The uploading speed is {correctUpload} mbp s")
    
def YouTubeAuto():
     speak("Whats Your Command ?")
     comm = takeCommand()

     if 'pause' in comm:
         keyboard.press('space bar')

     elif 'restart' in comm:
          keyboard.press('0')

     elif 'mute' in comm:
          keyboard.press('m')

     elif 'skip' in comm:
          keyboard.press('l')

     elif 'back' in comm:
          keyboard.press('j')

     elif 'full screen' in comm:
          keyboard.press('f')

     elif 'film mode' in comm:
          keyboard.press('t')

          speak("Done Sir")
          
def alarm():
         speak("Enter The Time !")
         time = input(": Enter The Time :")

         while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break
        
def My_location():
      ip_add = requests.get('https://api.ipify.org').text
      url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'       
      geo_q = requests.get(url)
      geo_d = geo_q.json()
      state = geo_d['city']
      country = geo_d['country']
      speak(f"sir,you are now in {state,country}.")
      print(state,country)  
      
def Notepad():
      speak("Tell me the query")
      speak("I am ready write")
      
      writes = takeCommand()
      time = (datetime.datetime.now().strftime("%H:%M"))
      
      
      filename=str(time).replace(":","-") + "-note.txt"
      with open(filename,"w") as file:
          file.write(writes)
          
      path_1 = "C:\\Users\\\Dell\\" + str(filename)
      path_2 = "C:\\Users\\Dell\\OneDrive\\Documents\\" + str(filename)
     
      os.rename(path_1,path_2)
      os.startfile(path_2)
      
def CloseNotepad():
      os.system("TASKKILL /F /im Notepad.exe")      
      
def GoogleMaps(Place):
      url_Place = "https://www.google.com/maps/place/" + str(Place)  
      
      geolocator = Nominatim(user_agent="myGeocoder")
      
      location = geolocator.geocode(Place  , addressdetails = True)
      
      target_latlon=location.latitude,location.longitude
      
      webbrowser.open(url=url_Place)
      
      location = location.raw['address']

      target = {'city' : location.get('city',''),
                   'state': location.get('state','') ,
                   'country' : location.get('country','')}
      
      current_loca = geocoder.ip('me')
      
      current_latlon = current_loca.latlng
      
      distance = str(great_circle(current_latlon,target_latlon))
      distance = str(distance.split(' ',1)[0])
      distance = round(float(distance),2)
      
      speak(target)
      speak(f"sir,{Place} is {distance} kilometer away from you")
      print(Place)
      print(distance)
 
def schedule():
           speak("Tell Me The Day!")
           dayName = takeCommand()  
           
           if 'Monday' in dayName:
               speak("9 to 10 maths class")
               speak("10 to 11 science class")
               speak("thank you")
               
           elif 'Tuesday' in dayName:
                 speak("9 to 10 history class")
                 speak("10 to 11 science class")  
                 speak("thank you")
           
           elif 'Wednesday' in dayName:
                  speak("9 to 10 history class")
                  speak("10 to 11 science class") 
                  speak("thank you")
                  
           elif 'Thursday' in dayName:
                  speak("9 to 10 history class")
                  speak("10 to 11 science class") 
                  speak("thank you")
          
           elif 'Friday' in dayName:
                  speak("9 to 10 history class")
                  speak("10 to 11 science class") 
                  speak("thank you")
                  
           elif 'Saturday' in dayName:
                  speak("9 to 10 history class")
                  speak("10 to 11 science class") 
                  speak("thank you")
                   
           elif 'Sunday' in dayName:
                  speak("today is sunday")
                  speak("Thank you")
def Music():
        speak("Tell Me The NamE oF The Song!")
        musicName = takeCommand()

        if 'kesariya' in musicName:
            os.startfile('D:\\Kesariya(PagalWorld.com.se).mp3')

        elif 'kal ho na ho' in musicName:
            os.startfile('D:\\bollywood_KHNH 2003 - Kal Ho Naa Ho.mp3')

        else:
            pywhatkit.playonyt(musicName)

        speak("Your Song Has Been Started! , Enjoy Sir!")
      
def Temp():
     search = "temperature in gaya"
     url = f"https://www.google.com/search?q={search}"
     r = requests.get(url)
     data = BeautifulSoup(r.text,"html.parser")
     temperature = data.find("div",class_ = "BNeawe").text
     speak(f"The Temperature Outside Is {temperature}")
     print(f"The Temperature Outside Is {temperature}")
              
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
          
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'newspaper' in query:
            webbrowser.open("timesofindia.indiatimes.com")
         
        elif 'open flipkart' in query:
              webbrowser.open("flipkart.com")
          
        elif 'open amazon' in query:
              webbrowser.open("amazon.com")  
              
        elif 'cricket score' in query:
              webbrowser.open("www.cricbuzz.com") 
              
        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message","")
            name = name.replace("send","")
            name = name.replace("to","")
            Name=str(name)
            speak(f"what message for {Name}")
            MSG=takeCommand()
            whatsappMSG(Name,MSG)
            
        elif 'Downloading speed' in query:
            SpeedTest()
        elif 'check internet speed' in query:
            SpeedTest()
            
        elif 'call' in query:
            name = query.replace("call","")
            name = name.replace("jarvis","")
            Name = str(name)
            WhatsappCall(Name)
        
        elif 'video connect' in query:
            name = query.replace("video connect","")
            name = name.replace("to","")
            name = name.replace("jarvis","")
            Name = str(name)
            WhatsappvideoCall(Name)

        elif 'youtube tool' in query:
            YouTubeAuto()    
         
        elif 'my location' in query:
            My_location()
            
        elif 'where is ' in query:
        
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis","")
            GoogleMaps(Place)   
           
        elif 'temperature' in query:  
               Temp()        
              
        elif 'take a screenshot' in query:   
               screenshot()
               
        elif 'set an alarm' in query:   
               alarm()    
               
        elif 'play music' in query:
              Music()
              
        elif 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            print(wiki)
            speak(f"According To Wikipedia : {wiki}")      
            
        elif 'notepad' in query:
            Notepad()
            
        elif 'close' in query:
              CloseNotepad()   
           
        elif 'schedule of today' in query:
              schedule()
              
                
       
            
        
            
            
            
            
            
            
