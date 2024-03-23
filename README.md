# Desktop-voice-assistant
Project Title: Personalised Desktop Voice Assistant

Project description:
1) Speech Recognition:
The project begins with implementing speech 
recognition functionality using Python's speech recognition library. This 
library provides convenient methods to capture and process audio input 
from the user's microphone. The speech recognition module converts the 
captured audio into text, which forms the basis for understanding the 
user's commands.

2) Natural Language Processing (NLP): 
To process and understand the user's 
commands, Natural Language Processing techniques are employed. 
Various libraries are used for this in Python.

3) Task Execution: 
Once the user's commands are understood, the voice 
assistant performs various tasks or actions based on the requested 
functionality. This may include tasks such as retrieving weather 
information, searching the web, playing music, or any other task. The 
implementation of these tasks may involve utilizing APIs, web scraping, or 
integrating with external services.

Requierd Libraries:
import pyttsx3    #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime    #pip install DateTime
import webbrowser  #pip install pycopy-webbrowser
import requests    #pip install requests
import geocoder    #pip install geocoder
import pyautogui   #pip install PyAutoGUI
import os          #pip install os-sys
import keyboard    #pip install os-sys
import pywhatkit   #pip install pywhatkit
import wikipedia   #pip install wikipedia

from os import startfile
from playsound import playsound
from pyautogui import click
from keyboard import press 
from keyboard import write
from time import sleep
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup

STEPS TO RUN CODE:
1)Install the above libraries in your python compiler(e.g.- Spyder).
2)Run the code
3)give voice command accordingly.

VOICE COMMAND:
1)To send whatsapp message:
 "whatsapp message to abhishek"
2)To open youtube:
  "open youtube"
3)To check cricket score:
"cricket score"
4)To check Internet speed:
 "check internet speed"
5)For whatsapp voice call:
"call abhishek"
6)For whatsapp video call:
" video connect abhishek"
7)To know your location:
 "my location"
8)To know about any location in map and how much distance from your location:
 "where is patna"


