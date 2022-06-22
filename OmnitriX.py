import pyttsx3
import speech_recognition as sr
import datetime
import time as ti
from time import sleep
import wikipedia
from bs4 import BeautifulSoup
import requests
import webbrowser
import sys
import pyjokes
import pyautogui
from pyautogui import typewrite
from pyautogui import *
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import pywhatkit
import os
from playsound import playsound
from newsapi import NewsApiClient
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from omnitrix_gui import Ui_OmnitriX


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(text):
    engine.say(text)
    engine.runAndWait()

MASTER = "Priyanshu"



def wishme():
    hour = int(datetime.datetime.now().hour)
    time = ti.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        print(f"Good Morning! It's {time}")
        speak(f"Good Morning! It's {time}")

    elif hour >= 12 and hour < 17:
        print(f"Good Afternoon! It's {time}")
        speak(f"Good Afternoon! It's {time}")

    else:
        print(f"Good Evening! It's {time}")
        speak(f"Good Evening! It's {time}")

    speak("I am OmnitriX. How may I help you?")



def weather(city):
  # enter city name
  # speak("What's the city name?")
  # city = self.takeCommand()
  
  # creating url and requests instance
  try:
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    print("It's " + time)
    speak("It's " + time)
    print("It's "+temp+" in "+city+" and the sky is "+sky)
    speak("It's "+temp+" in "+city+" and the sky is "+sky)
  except Exception as e:
    print(e)
    speak("Sorry, I couldn't find the weather for you")
    speak("Say that again please")

def news():
  url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=0f21afb989aa4700976dc340cef71caf'
  main_page = requests.get(url).json()
  articles = main_page['articles']

  for i in range(10):
    print(articles[i]['title'])
    speak(articles[i]['title'])
    print(articles[i]['description'])
    speak(articles[i]['description'])
    print("\n")
    speak("\n")


def alarm(time):
    altime = str(datetime.datetime.now().strptime(time,"%I:%M %p"))

    altime = altime[11:-3]

    horeal = altime[:2]
    horeal = int(horeal)
    mireal = altime[3:5]
    mireal = int(mireal)
    print(f"Done, Alarm set for {time}")
    speak(f"Done, Alarm set for {time}")
    while True:
        if horeal == datetime.datetime.now().hour:
            if mireal == datetime.datetime.now().minute:
                speak("Wake up, it's time to wake up")
                print("Wake up, it's time to wake up")
                break
        else:
            continue


class MainThread(QThread):
  def __init__(self):
    super(MainThread, self).__init__()

  def run(self):
    self.wakeupExecution()


  def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print(e)
            # print("Say that again please...")
            return ""
        query = query.lower()
        return query



  def taskExecution(self):
      
      wishme()
      while True:
            self.query = self.takeCommand()
            if 'wikipedia' in self.query:
                # speak('Searching Wikipedia...')
                # self.query = self.query.replace("wikipedia", "")
                speak("What do you want to search?")
                wiki = self.takeCommand()
                results = wikipedia.summary(wiki, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'who are you' in self.query or 'who made you' in self.query or 'what is your name' in self.query or 'name' in self.query:
                speak("I am OmnitriX. Created by Priyanshu Modi")

            elif 'search' in self.query or 'google' in self.query or 'open google' in self.query:
                speak("Tell me what to search?")
                google = self.takeCommand()
                url = f"https://www.google.com/search?q={google}"
                webbrowser.open(url)
                speak(f"Here is what I found for {google}")

            elif 'youtube' in self.query or 'open youtube' in self.query:
                speak("Opening Youtube")
                speak("What do you want to search?")
                self.query = self.takeCommand()
                pywhatkit.playonyt(self.query)
                speak(f"opening {self.query} in youtube")

            elif 'spotify' in self.query or 'play spotify' in self.query or 'open spotify' in self.query:
                import spotipy
                username = 'c4n6dcfrk4zqsklryr3g7elp0'
                clientID = 'e9849d0408a94fb99fe690dd49bcf35b'
                clientSecret = '4c771c167cda4d85a57322f6a2b498b6'
                redirectURI = 'http://google.com/' 
                oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
                token_dict = oauth_object.get_access_token()
                token = token_dict['access_token']
                spotifyObject = spotipy.Spotify(auth=token)
                user = spotifyObject.current_user()
                speak("Opening Spotify")
                print("Welcome, "+ user['display_name'])
                speak("Welcome, "+ user['display_name'])
                print("What's the song name?")
                speak("What's the song name?")
                searchQuery = self.takeCommand()
                try:
                  searchResults = spotifyObject.search(searchQuery,1,0,"track")
                  tracks_dict = searchResults['tracks']
                  tracks_items = tracks_dict['items']
                  song = tracks_items[0]['external_urls']['spotify']
                  # Open the Song in Web Browser
                  webbrowser.open(song)
                  print('Song has opened in your browser.')
                  speak('Song has opened in your browser.')
                except:
                  print("Sorry, I couldn't find the song.")
                  speak("Sorry, I couldn't find the song.")
            
            elif 'weather' in self.query or 'temperature' in self.query or 'check weather' in self.query or 'please check weather' in self.query:
              speak("What's the city name?")
              city = self.takeCommand()
              weather(city)

            elif 'song' in self.query or 'play song' in self.query or 'play music' in self.query or 'music' in self.query:
                speak("What's the song name?")
                searchQuery = self.takeCommand()
                pywhatkit.playonyt(searchQuery)
                speak(f"Playing {searchQuery}")
              
            elif 'time' in self.query:
              tt = ti.strftime("%I:%M %p")
              print(f"It's {tt}")
              speak(f"It's {tt}")
            
            elif 'day' in self.query or 'date' in self.query:
              tt = ti.strftime("%A")
              from datetime import date
              today = date.today()
              d2 = today.strftime("%B %d, %Y")
              print(f"It's {tt} {d2}")
              speak(f"It's {tt} {d2}")

            # elif 'ok' in self.query or 'okay' in self.query:
            #   speak("Anything else?")
            
            elif 'chrome' in self.query or 'chrome browser' in self.query:
              speak("Opening Chrome")
              pyautogui.hotkey('winleft')
              pyautogui.typewrite('chrome')
              pyautogui.press('enter')
            
            elif 'brave' in self.query or 'brave browser' in self.query:
              speak("Opening Brave")
              pyautogui.hotkey('winleft')
              pyautogui.typewrite('brave')
              pyautogui.press('enter')
            
            elif 'firefox' in self.query or 'firefox browser' in self.query:
              speak("Opening Firefox")
              pyautogui.hotkey('winleft')
              pyautogui.typewrite('firefox')
              pyautogui.press('enter')
            
            elif 'opera' in self.query or 'opera browser' in self.query:
              speak("Opening Opera")
              pyautogui.hotkey('winleft')
              pyautogui.typewrite('opera')
              pyautogui.press('enter')

            elif 'application' in self.query or 'app' in self.query or 'launch' in self.query:
              speak("What's the application name?")
              app = self.takeCommand()
              speak("Opening "+app)
              pyautogui.hotkey('winleft')
              pyautogui.typewrite(app)
              pyautogui.press('enter')

            elif 'note' in self.query or 'reminder' in self.query:
              speak("What should i note?")
              data = self.takeCommand()
              #save the text file
              f = open("reminder.txt", "a")
              f.write("\n")
              f.write(data)
              f.close()
              speak("I have added "+data+" to your reminder list")
              while True:
                speak("Wanna add more?")
                self.query = self.takeCommand()
              # while True:
                if 'yes' in self.query:
                  f = open("reminder.txt", "a")
                  speak("What do you want me to remind you?")
                  data = self.takeCommand()
                  f.write("\n")
                  f.write(data)
                  f.close()
                  speak("I have added "+data+" to your reminder list")
                else:
                  break

            elif 'remember' in self.query or 'show me' in self.query:
              speak("This is what I remember ")
              f = open("reminder.txt", "r")
              data = f.read()
              print(data)
              speak(data)
              f.close()
              #remove the text
              f = open("reminder.txt", "w")
              f.write("")
              f.close()

            elif 'alarm' in self.query or 'set alarm' in self.query:
              speak("What time do you want to set the alarm?")
              alarm_time = self.takeCommand()
              alarm_time = alarm_time.replace("set the alarm to ", "")
              alarm_time = alarm_time.replace(".","")
              alarm_time = alarm_time.upper()
              alarm(alarm_time)

            elif 'screenshot' in self.query:
              speak("Please hold the screen, I am taking a screenshot")
              img = pyautogui.screenshot()
              speak("Would you like to give me a name for the screenshot?")
              name = self.takeCommand()
              img.save(f"{name}.png")
              speak("Screenshot saved")
              speak("Do you want to open the screenshot?")
              self.query = self.takeCommand()
              if 'yes' in self.query:
                os.startfile(f"{name}.png")
              elif 'no' in self.query:
                speak("Okay")

            elif 'news' in self.query:
              speak("Here are the latest news")
              news()

            elif 'jokes' in self.query or 'joke' in self.query or 'tell me a joke' in self.query:
              joke = pyjokes.get_joke()
              print(joke)
              speak(joke)
              while True:
                speak("Wanna hear another joke?")
                self.query = self.takeCommand()
                if 'yes' in self.query:
                  joke = pyjokes.get_joke()
                  print(joke)
                  speak(joke)
                else:
                  print("Okay")
                  speak("Okay")
                  break

            elif 'home screen' in self.query or 'desktop' in self.query:
              press_and_release('windows + m')

            elif 'minimize' in self.query:
                press_and_release('windows + m')

            elif 'show start' in self.query or 'start menu' in self.query or 'start' in self.query:
                pyautogui.press('winleft')

            elif 'open setting' in self.query or 'settings' in self.query:
                press_and_release('windows + i')

            elif 'discord' in self.query:
                speak("Opening Discord")
                pyautogui.hotkey('winleft')
                pyautogui.typewrite('discord')
                pyautogui.press('enter')
            
            elif 'volume up' in self.query or 'increase volume' in self.query:
                pyautogui.hotkey('volumeup')
            
            elif 'volume down' in self.query or 'decrease volume' in self.query:
                pyautogui.hotkey('volumedown')
              
            elif 'mute' in self.query or 'mute volume' in self.query:
                pyautogui.hotkey('volumemute')
              
            elif 'unmute' in self.query or 'unmute volume' in self.query:
                pyautogui.hotkey('volumemute')

            elif 'lock' in self.query or 'lock screen' in self.query:
                speak("Locking the screen")
                press_and_release('windows + l')

            elif 'hello' in self.query or 'hay' in self.query:
                speak("Hello "+ MASTER)
                speak("How can I help you?")

            elif 'how are you' in self.query or 'are you fine' in self.query:
                speak("I am fine, what about you?")

            elif 'also good' in self.query or 'fine' in self.query:
                speak("That's good to hear")
              
            elif 'thankyou' in self.query or 'thanks' in self.query or 'thank you' in self.query:
                speak("You're welcome" + MASTER)
              
            elif 'sleep' in self.query or 'sleep now' in self.query or 'standby' in self.query or 'stand by' in self.query:
                speak("ok,I'm going to sleep now, Call me anytime")
                break
            
            elif 'goodnight' in self.query or 'good night' in self.query:
                speak(f"Good night {MASTER}. See you soon")
                break


  def wakeupExecution(self):
    speak("System is now Online")
    while True:
      wakeup = self.takeCommand()
      if 'wake up' in wakeup or 'omnitrix' in wakeup or 'hello' in wakeup:
        sleep(0.5)
        self.taskExecution()
      elif "goodbye" in wakeup or "good bye" in wakeup or "see you later" in wakeup or 'good night' in wakeup or 'goodnight' in wakeup:
        print("Good bye "+MASTER)
        speak("Good bye "+ MASTER)
        sys.exit()
        


startExecution = MainThread()


class Main(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_OmnitriX()
    self.ui.setupUi(self)
    self.startTask()
    # self.ui.pushButton.clicked.connect(self.startTask)
    self.ui.pushButton_2.clicked.connect(self.close)




  def startTask(self):
    self.ui.movie = QtGui.QMovie("D:\OmnitriX\Omnitrix.gif")
    self.ui.label.setMovie(self.ui.movie)
    self.ui.movie.start()
    startExecution.start()
    


app = QApplication(sys.argv)
OmnitriX = Main()
OmnitriX.show()
sys.exit(app.exec_())