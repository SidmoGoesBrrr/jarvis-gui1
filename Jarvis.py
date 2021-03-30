import datetime
import os
import random
import subprocess
import time
import webbrowser
# name u void
import PyPDF2 as PyPDF2
import cv2
from gtts import gTTS
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from PyDictionary import PyDictionary
from playsound import playsound
from pytube import YouTube
from tkinter import *
from tkinter import messagebox, filedialog
from googletrans import Translator
from random import randint
import requests
from bs4 import BeautifulSoup
from requests import get
from pywikihow import search_wikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import  QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisUi import Ui_JarvisGUI
from main import takecommand

dictionary = PyDictionary()

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 180)
reply_to_thanks = ["You're welcome sir",
                   "Always happy to Help!", "my pleasure sir"]
reply_to_hru = ["I am fine Sir!", "Top of the world sir", "As good as an AI assistant can be!",
                "sir you made me, you should know!", "I am doing great"]
reply_to_break_needed = ["Ok sir, you can call me anytime", "Bye Sir", "Yes Sir, I agree. Bye",
                         "taking break right now", "Your wish is my command sir! Bye"]
hour = datetime.datetime.now().hour
hour1 = int(datetime.datetime.now().hour)


def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"JARVIS: {audio}")
    print("  ")
    Assistant.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExe()

    def takecommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"listening.....")
            command.pause_threshold = 2
            audio = command.listen(source)

            try:
                print(f"Recognising....")
                self.query = command.recognize_google(audio, language='en-in')
                print(f"SIDDHANT: {self.query}")

            except Exception as Error:
                # Speak("Say that again please")
                return "None"

            return self.query.lower()

    def Wish_me(self):
        if hour1 >= 0 and hour1 <= 12:
            Speak("Good Morning")

        elif hour1 > 12 and hour1 < 6:
            Speak("Good afternoon")

        else:
            Speak("Good evening ")
        Speak("I am Jarvis")
        Speak("Your personal AI Assistant")
        Speak("How may I help you?")

    if __name__ == "__main__":
        print("J.A.R.V.I.S Initiated")
        Speak("JARVIS Initiated")
        # Speak("")
        Wish_me()

    def TaskExe(self):
        def Music():
            Speak("Sure! Tell me the song name")
            musicName = takecommand()
            pywhatkit.playonyt(musicName)

        def RockPaperScissors():

            # create a list of play options
            t = ["Rock", "Paper", "Scissors"]

            # assign a random play to the computer
            computer = t[randint(0, 2)]

            # set player to False
            player = False

            while player == False:
                # set player to True
                Speak("Choose rock, paper or scissors")
                playerChoice = takecommand()
                if 'rock' in playerChoice:
                    player = "Rock"

                elif 'paper' in playerChoice:
                    player = "Paper"

                elif 'scissors' in playerChoice:
                    player = "Scissors"

                else:
                    Speak("That's not a valid play. Check your spelling!")

                if player == computer:
                    Speak("It's a tie, you chose" + player +
                          "and Computer chose" + computer)

                elif player == "Rock":
                    if computer == "Paper":
                        Speak("You lose!" + computer + "covers" + player)
                    else:
                        Speak("You win!" + player + "smashes" + computer)
                elif player == "Paper":
                    if computer == "Scissors":
                        Speak("You lose!" + computer +
                              computer + "cut" + player)
                    else:
                        Speak("You win!" + player + "covers" + computer)
                elif player == "Scissors":
                    if computer == "Rock":
                        Speak("You lose..." + computer + "smashes" + player)
                    else:
                        Speak("You win!" + player + "cut" + computer)

                # player was set to True, but we want it to be False so the loop continues
                Speak("Do you wanna play again")
                ChoicePlayAgain = takecommand()
                if 'yes' in ChoicePlayAgain or 'ya' in ChoicePlayAgain:
                    ChoicePlayAgain = False

                else:
                    ChoicePlayAgain = True
                    Speak("Exited Rock Paper scissors")
                player = ChoicePlayAgain
                computer = t[randint(0, 2)]

        def Whatsapp():
            Speak("Tell me the name of the person to send the WhatsApp message to")
            name = takecommand()

            if 'dad' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg("+91 9619089263", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            elif 'mom' in name or 'mum' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg("+91 9619089262", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            elif 'jason' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg("+91 9082607664", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            elif 'tanishka' in name or 'germany' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg("+91 8369665548", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            elif 'sammriddhi' in name or 'sosa' in name or 'sam' in name or 'sammy' in name or 'sammwiddhi' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                # mins=mins.replace(" ", "")
                # mins=mins.replace("-", "")
                # mins=mins.replace("_", "")
                pywhatkit.sendwhatmsg("+91 9820719881", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            elif 'mama' in name:
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg("+1 (302) 559-1367", msg, hour, mins, 8)
                Speak("OK Sir sending.......")

            else:
                Speak("I don't know him/her tell Me The Phone number")
                PhoneNo = takecommand()
                ph = "+91" + PhoneNo
                Speak("Tell me what is the message?")
                msg = takecommand()
                Speak("Tell time in hour")
                hour = int(takecommand())
                Speak("Tell time in minutes now")
                mins = int(takecommand())
                pywhatkit.sendwhatmsg(ph, msg, hour, mins, 8)
                Speak("OK Sir sending.......")

        def OpenApps():
            Speak("OK let me find it")
            if 'deliverables input' in self.query:
                webbrowser.open(
                    "https://onedrive.live.com/edit.aspx?action=editnew&resid=471395B4839DF8BB!1767&ithint=file%2cxlsx&action=editnew&wdNewAndOpenCt=1615784389561&wdPreviousSession=0323529c-56ca-42c7-bb03-d2a21ad2963f&wdOrigin=OFFICECOM-WEB.START.NEW")
                Speak("Opening Deliverables")

            elif 'spotify' in self.query:
                os.startfile(
                    "C:\\Users\\user123\\AppData\\Roaming\\Spotify\\Spotify.exe")
                Speak("Opening Spotify")

            elif 'o b s' in self.query:
                os.startfile(
                    "C:\\Program Files\\obs-studio\\bin\64bit\\obs64.exe")
                Speak("Opening OBS studio")

            elif 'epic games' in self.query:
                os.startfile(
                    "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
                Speak("Opening Epic Games for the epic gamer")

            elif 'unity' in self.query:
                os.startfile("C:\\Program Files\\Unity Hub\\Unity Hub.exe")
                Speak("Opening Unity Hub")
            else:
                Speak("App not found")

        def SpeedTest():
            import speedtest
            Speak("Checking Speed..........")
            speed = speedtest.Speedtest()
            downloading = speed.download()
            correctDown = int(downloading / 800000)
            uploading = speed.upload()
            correctUploading = int(uploading / 800000)

            if 'uploading' in self.query:
                Speak(f"The uploading speed is {correctUploading} mbps")

            elif 'downloading' in self.query:
                Speak(f"The downloading speed is {correctDown} mbps")

            else:
                Speak(
                    f"The downloading speed is {correctDown} mbps and the uploading speed is {correctUploading} mbps")

        def Reader():

            Speak("Tell me the name of the book to read")

            name = takecommand(self)()

            if 'geography' in name and 'notes' in name:

                os.startfile(
                    "C:\\Users\\user123\\Downloads\\STD X - GEOG - SAMPLE NOTES - SOIL.pdf")
                book = open(
                    "C:\\Users\\user123\\Downloads\\STD X - GEOG - SAMPLE NOTES - SOIL.pdf", 'rb')
                pdfreader = PyPDF2.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number of pages in the book are {pages}")
                Speak("From which page do I have to start reading?")
                numPage = int(input("Enter No of pages here"))
                page = pdfreader.getPage(numPage)
                text = page.extractText()
                Speak("In which language do I have to read")
                lang = takecommand(self)()

                if 'hindi' in lang:
                    Speak("Ok reading in hind")
                    transl = Translator()
                    texthin = transl.translate(text, 'hi')
                    textm = texthin.text
                    speech = gTTS(text=textm)
                    try:

                        speech.save('book.mp3')
                        playsound('book.mp3')

                    except:
                        playsound('book.mp3')

                else:
                    Speak(text)

        def Dict():
            Speak("Dictionary initiated")
            Speak("Tell me the problem")
            problem = takecommand()

            if 'meaning' in problem:
                problem = problem.replace("what is the", "")
                problem = problem.replace("jarvis", "")
                problem = problem.replace("of", "")
                problem = problem.replace("meaning", "")
                result = dictionary.meaning(problem)
                Speak(f"The meaning for {problem} is {result}")

            elif 'synonym' in problem or 'same word':
                problem = problem.replace("what is the", "")
                problem = problem.replace("jarvis", "")
                problem = problem.replace("of", "")
                problem = problem.replace("synonym", "")
                result = dictionary.synonym(problem)
                Speak(f"The synonym for {problem} is {result}")

            elif 'antonym,' in problem or 'opposite' in problem:
                problem = problem.replace("what is the", "")
                problem = problem.replace("jarvis", "")
                problem = problem.replace("of", "")
                problem = problem.replace("antonym", "")
                problem = problem.replace("opposite", "")
                result = dictionary.antonym(problem)
                Speak(f"The antonym for {problem} is {result}")

            Speak("Exited Dictionary")

        def CloseApps():
            Speak("OK, Sir, wait a second ")

            if 'youtube' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'stack overflow' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'github' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'white hat junior' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'deliverables' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'google translate' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'zoom' in self.query:
                os.system("TASKILL /F /im Zoom.exe")

            elif 'brave' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'browser' in self.query:
                os.system("TASKILL /F /im brave.exe")

            elif 'o b s' in self.query:
                os.system("TASKILL /F /im obs64.exe")

            elif 'spotify' in self.query:
                os.system("TASKILL /F /im Spotify.exe")

            elif 'unity' in self.query:
                os.system("TASKILL /F /im Unity Hub.exe")

            elif 'epic' in self.query:
                os.system("TASKILL /F /im EpicGamesLauncher.exe")

            elif 'blender' in self.query:
                os.system("TASKILL /F /im blender.exe")

            elif 'fortnite' in self.query:
                os.system("TASKILL /F /FortniteClient-Win64-Shipping.exe")

            elif 'whatsapp' in self.query:
                os.system("TASKILL /F /im WhatsApp.exe")

            Speak("Your command has been completed")

        def temp():
            search = "temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            Speak(f"The temperature outside is {temperature}")

        def takeHindi():
            command = sr.Recognizer()
            with sr.Microphone() as source:
                print(f"listening.....")
                command.pause_threshold = 2
                audio = command.listen(source)

                try:
                    print(f"Recognising....")
                    self.query = command.recognize_google(audio, language='hi')
                    print(f"SIDDHANT: {self.query}")

                except Exception as Error:
                    return "None"

                return self.query.lower()

        def trans():
            Speak("Tell me the line")
            line = takeHindi()
            ts = Translator()
            # result = ts.translate(line)
            if line:
                result = ts.translate(line)
                ResultText = result.text
                Speak("The translation for this text is: " + ResultText)

        def YoutubeAuto():
            Speak("What's your command")
            comm = takecommand()
            if 'pause' in comm:
                pyautogui.hotkey('k')

            elif 'restart' in comm:
                pyautogui.hotkey('0')

            elif 'mute' in comm:
                pyautogui.hotkey('m')

            elif 'forward' in comm:
                pyautogui.hotkey('l')

            elif 'back' in comm:
                pyautogui.hotkey('j')

            elif 'full screen' in comm:
                pyautogui.hotkey('f')

            elif 'theatre mode' in comm:
                pyautogui.hotkey('t')

            elif 'skip' in comm:
                pyautogui.hotkey('shift', 'n')

            Speak("Done Sir")

        def BraveAuto():
            Speak("Ok, what do you want me to do?")
            command = takecommand()

            if 'close this tab' in command or 'close tab' in command:
                pyautogui.hotkey('ctr;', 'w')

            if 'open a new tab' in command or 'new tab tab' in command:
                pyautogui.hotkey('ctr;', 't')

            if 'reload this tab' in command or 'reload tab' in command:
                pyautogui.hotkey('ctr;', 'r')

            if 'show my history' in command or 'show history' in command:
                pyautogui.hotkey('ctr;', 'h')

            if 'open a new window' in command or 'new window' in command:
                pyautogui.hotkey('ctr;', 'n')

            if 'open console' in command or 'console' in command:
                pyautogui.hotkey('ctr;', 'shift', 'i')

            if 'show downloads' in command or 'downloads' in command:
                pyautogui.hotkey('ctr;', 'j')

            if 'book mark this tab' in command or 'book mark' in command or 'bookmark' in command:
                pyautogui.hotkey('ctr;', 'd')

            if 'incognito' in command or 'go incognito' in command:
                pyautogui.hotkey('ctr;', 'shift', 'n')

            else:
                Speak("Error, command not found")

            Speak("Done Sir")

        while True:

            self.query = self.takecommand()

            if 'hello' in self.query:
                Speak("Hello Sir, I am Jarvis .")
                Speak("Your Personal AI Assistant! ")
                Speak("How may I help you?")

            elif 'how are you' in self.query:
                Speak(random.choice(reply_to_hru))
                Speak("What About You")

            elif 'you need a break' in self.query or 'bye' in self.query or 'take a break' in self.query:
                Speak(random.choice(reply_to_break_needed))
                break

            elif 'am' in self.query and "great" in self.query:
                Speak("That's nice sir")
                # just to close loop

            elif 'youtube search' in self.query:
                Speak("OK SIR Here is what I found!")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_self.query=' + self.query
                webbrowser.open(web)
                Speak("Done Sir")

            elif 'greet' in self.query:
                self.query = self.query.replace("Jarvis", "")
                self.query = self.query.replace("greet", "")
                Speak("Hey," + self.query + ", How are you?")

            elif 'google search' in self.query:
                import wikipedia as googleScrap
                self.query = self.query.replace("google", "")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("google search", "")
                self.query = self.query.replace("search", '')
                Speak("This is what I found on the web")
                pywhatkit.search(self.query)
                try:
                    result = googleScrap.summary(self.query, 3)
                    Speak(result)

                except:
                    Speak("No speakable data found")

            elif 'launch website' in self.query:
                Speak("Ok Tell me name of website")
                Name = takecommand()
                Name.replace(" ", "")
                web = "https://www." + Name + ".com"
                webbrowser.open(web)
                Speak("Opened " + Name)

            elif 'thank you' in self.query or 'thanks' in self.query:
                Speak(random.choice(reply_to_thanks))
                # just to close loop

            elif 'open github' in self.query:
                Speak("Opening GitHub now!")
                webbrowser.open("https://github.com")

            elif 'open white hat junior' in self.query:
                Speak("Opening Whitehat Junior now!")
                webbrowser.open("https://code.whitehatjr.com/s/dashboard")

            elif 'open youtube' in self.query:
                Speak("Opening YouTube now!")
                webbrowser.open("https://youtube.com")

            elif 'open google translate' in self.query:
                Speak("Opening Google Translate now!")
                webbrowser.open("https://translate.google.com/")

            elif 'open stack over flow' in self.query or 'open stack overflow' in self.query or 'open stackoverflow' in self.query:
                Speak("Opening StackOverflow now!")
                webbrowser.open("https://stackoverflow.com/")

            elif 'play a song' in self.query:
                Music()
                #

            elif "sign out" in self.query or 'logoff' in self.query or "log off" in self.query:
                Speak(
                    "Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif "shutdown" in self.query:
                Speak("Shutting down system")
                os.system("shutdown /s /t 5")

            elif "restart" in self.query:
                Speak("Restarting system")
                os.system("shutdown /r /t 5")

            elif "sleep" in self.query:
                Speak("Going to sleep")
                os.system("rundll32.exe powrprof.dll , SetSuspendState 0,1,0")

            elif 'wikipedia' in self.query:
                Speak("Searching Wikipedia......")
                self.query = self.query.replace("Jarvis", "")
                self.query = self.query.replace("wikipedia", "")
                wiki = wikipedia.summary(self.query, 2)
                ans = takecommand()
                Speak(f"According to Wikipedia : {wiki}")
                if "stop" in ans or "ok" in ans:
                    break

            elif "mirror" in self.query or "show me" in self.query or 'show myself' in self.query:
                Speak("Opening image preview:)")
                Speak("Press Q To Quit")
                cam = cv2.VideoCapture(0)
                while (True):

                    # Capture the video frame
                    # by frame
                    ret, frame = cam.read()

                    # Display the resulting frame
                    cv2.imshow('Image Preview', frame)

                    # the 'q' button is set as the
                    # quitting button you may use any
                    # desired button of your choice
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                # After the loop release the cap object
                cam.release()
                # Destroy all the windows
                cv2.destroyAllWindows()

            elif 'whatsapp message' in self.query or 'send a whatsapp message' in self.query or 'WhatsApp message' in self.query:
                Whatsapp()
                #

            elif "capture" in self.query or "photo" in self.query or "pic" in self.query or 'picture' in self.query:
                Speak("Press 'P' to take a photo, esc to exit")
                cam = cv2.VideoCapture(0)
                while True:
                    _, frame = cam.read()  # We don't want ret in this
                    # Show the current frame
                    cv2.imshow("Image Preview", frame)
                    key = cv2.waitKey(1)
                    # If you press Esc then the frame window will close (and the program also)
                    if key == 27:
                        Speak("Exited Photo window")
                        break
                    elif key == ord('p'):  # If you press p/P key on your keyboard
                        cv2.imwrite("C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\pic.png",
                                    frame)  # Save current frame as picture with name pic.jpg
                        time.sleep(0.7)
                        Speak("Opening your picture now")
                        os.startfile(
                            "C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\pic.png")

                cam.release()
                cv2.destroyAllWindows()

            elif 'screenshot' in self.query or 'screen shot' in self.query:
                Speak("Screenshot taken and saved ,opening it now")
                pyautogui.screenshot('my_screenshot.png')
                time.sleep(0.3)
                os.startfile(
                    "C:\\Users\\user123\\PycharmProjects\\Jarvis_AI\\my_screenshot.png")

            elif 'open spotify' in self.query:
                OpenApps()

            elif 'open epic games' in self.query:
                OpenApps()

            elif 'open deliverables input' in self.query:
                OpenApps()

            elif 'open OBS studio' in self.query or 'OBS' in self.query:
                OpenApps()

            elif 'open Unity' in self.query or 'unity' in self.query:
                OpenApps()

            elif 'open Fortnite' in self.query or 'launch fortnite' in self.query:
                Speak("Launching Fortnite, this may take a while")
                pyautogui.click(x=602, y=1062)

            elif 'open Whatsapp' in self.query or 'open whatsapp' in self.query:
                os.startfile(
                    "C:\\Users\\user123\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
                Speak("Opening WhatsApp")

            elif 'open Zoom' in self.query or 'open zoom' in self.query:
                os.startfile(
                    "C:\\Users\\user123\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
                Speak("Opening Zoom")

            elif 'open blender' in self.query:
                os.startfile(
                    "C:\\Program Files\\Blender Foundation\\Blender 2.91\\blender.exe")
                Speak("Opening Blender")

            elif 'open vs code' in self.query or 'open vscode' in self.query:
                os.startfile(
                    "C:\\Users\\user123\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                Speak("Opening Visual Studio")

            elif 'open steam' in self.query:
                os.startfile("C:\\Program Files (x86)\\Steam\\Steam.exe")
                Speak("Opening Steam")

            elif 'open deliverables output' in self.query:
                webbrowser.open("https://technofrost27.github.io/spreadsheet/")
                Speak("Opening Deliverables Output Database")

            elif 'edit a photo' in self.query or 'open photoshop' in self.query:
                os.startfile(
                    "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe")
                Speak("Starting Photoshop 2021")

            elif 'edit a video' in self.query or 'open premier pro' in self.query:
                os.startfile(
                    "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe")
                Speak("Starting Premiere Pro 2020")

            elif 'full screen' in self.query and 'window' in self.query:
                Speak("Making this window fullscreen if supported ")
                pyautogui.hotkey('f11')

            elif 'max' in self.query and 'window' in self.query:
                Speak("Maximising current window")
                pyautogui.hotkey('alt', 'space')
                pyautogui.hotkey('x')

            elif 'restore' in self.query and 'window' in self.query:
                Speak("Restoring window to it's original size")
                pyautogui.hotkey('alt', 'space')
                pyautogui.hotkey('r')

            elif 'minimise' in self.query and 'window' in self.query:
                Speak("Minimising current window")
                pyautogui.hotkey('alt', 'space')
                pyautogui.hotkey('n')

            elif 'close' in self.query and 'window' in self.query:
                Speak("Closing current window")
                pyautogui.hotkey('alt', 'space')
                pyautogui.hotkey('c')

            elif 'switch windows' in self.query or 'switch window' in self.query or 'change windows' in self.query or 'alt tab' in self.query or 'all tab' in self.query:
                Speak("Switching Windows")
                pyautogui.hotkey('alt', 'tab')

            elif 'Show desktop' in self.query and 'windows d' in self.query:
                Speak("Here is the desktop")
                pyautogui.hotkey('win', 'd')

            elif 'task manager' in self.query:
                Speak("Opening task manager")
                pyautogui.hotkey('ctrl', 'shift', 'esc')

            elif 'command prompt' in self.query:
                Speak("Opening command prompt as admin")
                pyautogui.hotkey('win', 'x')
                pyautogui.hotkey('a')
                time.sleep(0.6)

            elif 'close youtube' in self.query:
                CloseApps()

            elif 'close stack overflow' in self.query:
                CloseApps()

            elif 'close github' in self.query:
                CloseApps()

            elif 'close white hat junior' in self.query:
                CloseApps()

            elif 'close deliverables' in self.query:
                CloseApps()

            elif 'close google translate' in self.query:
                CloseApps()

            elif 'close brave' in self.query:
                CloseApps()

            elif 'close browser' in self.query:
                CloseApps()

            elif 'close o b s' in self.query:
                CloseApps()

            elif 'close spotify' in self.query:
                CloseApps()

            elif 'close zoom' in self.query:
                CloseApps()

            elif 'close unity' in self.query:
                CloseApps()

            elif 'close epic games' in self.query:
                CloseApps()

            elif 'close blender' in self.query:
                CloseApps()

            elif 'close fortnite' in self.query:
                CloseApps()

            elif 'close whatsapp' in self.query:
                CloseApps()

            elif 'youtube' in self.query and 'action' in self.query:
                YoutubeAuto()

            elif 'brave' in self.query and 'action' in self.query:
                BraveAuto()

            elif 'joke' in self.query or 'make me laugh' in self.query:
                getJoke = pyjokes.get_joke()
                Speak(getJoke)

            elif 'repeat this' in self.query or 'repeat after me' in self.query:
                Speak("Speak sir")
                repeatedCommand = takecommand()
                Speak(repeatedCommand)

            elif 'my location' in self.query:
                Speak("Ok, here is your location......")
                webbrowser.open(
                    "https://www.google.co.in/maps/place/Megh+Tower,+Yashodham,+Goregaon,+Mumbai,+Maharashtra+400063/@19.1737215,72.8619565,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7b7a7c4a458d7:0xc036afcdd539602d!8m2!3d19.1737215!4d72.8641452!16s%2Fg%2F12hks6k21?hl=en")

            elif 'dictionary' in self.query:
                Dict()

            elif 'set an alarm' in self.query:
                Speak("Enter The Time")
                alarm_time = input("Enter the Time:")

                while True:
                    Time_AC = datetime.datetime.now()
                    now = Time_AC.strftime("%H:%M:%S")
                    Speak("Alarm Set for " + alarm_time)
                    if now == alarm_time:
                        Speak("Alarm Over")
                        playsound('alarm.mp3')

                    elif now > alarm_time:
                        break

            elif 'video downloader' in self.query or 'download youtube video' in self.query:
                Speak("OK, Enter video URL and file location")

                def Widgets():
                    link_label = Label(root,
                                       text="YouTube link  :",
                                       bg="#E8D579")
                    link_label.grid(row=1,
                                    column=0,
                                    pady=5,
                                    padx=5)

                    root.linkText = Entry(root,
                                          width=55,
                                          textvariable=video_Link)
                    root.linkText.grid(row=1,
                                       column=1,
                                       pady=5,
                                       padx=5,
                                       columnspan=2)

                    destination_label = Label(root,
                                              text="Destination    :",
                                              bg="#E8D579")
                    destination_label.grid(row=2,
                                           column=0,
                                           pady=5,
                                           padx=5)

                    root.destinationText = Entry(root,
                                                 width=40,
                                                 textvariable=download_Path)
                    root.destinationText.grid(row=2,
                                              column=1,
                                              pady=5,
                                              padx=5)

                    browse_B = Button(root,
                                      text="Browse",
                                      command=Browse,
                                      width=10,
                                      bg="#05E8E0")
                    browse_B.grid(row=2,
                                  column=2,
                                  pady=1,
                                  padx=1)

                    Download_B = Button(root,
                                        text="Download",
                                        command=Download,
                                        width=20,
                                        bg="#05E8E0")
                    Download_B.grid(row=3,
                                    column=1,
                                    pady=3,
                                    padx=3)

                def Browse():

                    download_Directory = filedialog.askdirectory(
                        initialdir="YOUR DIRECTORY PATH")

                    download_Path.set(download_Directory)

                def Download():

                    Youtube_link = video_Link.get()

                    download_Folder = download_Path.get()

                    getVideo = YouTube(Youtube_link)

                    videoStream = getVideo.streams.first()

                    videoStream.download(download_Folder)

                    messagebox.showinfo("SUCCESSFULLY",
                                        "DOWNLOADED AND SAVED IN\n"
                                        + download_Folder)
                    Speak("Video Downloaded sir!")

                root = Tk()

                root.geometry("600x120")
                root.resizable(False, False)
                root.title("YouTube_Video_Downloader")
                root.config(background="#000000")

                video_Link = StringVar()
                download_Path = StringVar()

                Widgets()

                root.mainloop()

            elif 'what is the time' in self.query or "what's the time" in self.query or 'tell me the time' in self.query or 'what is the current time' in self.query:

                now = datetime.datetime.now()

                current_time = now.strftime("%H:%M:%S")

                if 0 <= hour < 12:
                    Timed_Greeting = "morning!"

                elif 12 <= hour < 5:
                    Timed_Greeting = "afternoon!"

                elif 5 <= hour < 9:
                    Timed_Greeting = "evening!"

                else:
                    Timed_Greeting = "night!"

                Speak(
                    f"Current Time is {current_time}! Also have a great {Timed_Greeting}")

            elif 'copy text' in self.query or 'copy this' in self.query:
                pyautogui.hotkey('ctrl', 'c')
                Speak("Copied Text to clipboard! ")

            elif 'cut text' in self.query or 'cut this' in self.query:
                pyautogui.hotkey('ctrl', 'x')
                Speak("Cut text")

            elif 'paste text' in self.query or 'paste this' in self.query:
                pyautogui.hotkey('ctrl', 'v')
                Speak("Pasted text from clipboard!")

            elif 'mute' in self.query and 'teams' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'm')
                Speak("Ok, toggled mic")

            elif 'video' in self.query and 'teams' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'o')
                Speak("Ok, Toggled Video ")

            elif 'blur' in self.query and 'teams' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'p')
                Speak("Ok, blurred background")

            elif 'raise hand in teams' in self.query or 'raise my hand in teams' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'k')
                Speak("Ok sir, raised hand")

            elif 'leave meeting' in self.query or 'leave the meeting' in self.query:
                pyautogui.hotkey('ctrl', 'shift', 'b')
                Speak("Ok sir, left the meeting")

            elif 'translate' in self.query or 'translator' in self.query:
                trans()

            elif 'remember this' in self.query or 'remember that' in self.query:
                self.query = self.query.replace("remember this", "")
                self.query = self.query.replace("remember", "")
                self.query = self.query.replace("this", "")
                self.query = self.query.replace("that", "")
                self.query = self.query.replace("jarvis", "")
                remembermsg = self.query
                Speak("OK Sir, I will remember:" + remembermsg)
                remember = open('data.txt', 'w')
                remember.write(remembermsg)
                remember.close()

            elif 'what do you remember' in self.query or 'what did i tell you to remember' in self.query:
                remember = open('data.txt', 'r')
                Speak("I remember that: " + remembermsg)

            elif 'play' in self.query and ('rock' in self.query or 'paper' in self.query or 'scissors' in self.query):
                RockPaperScissors()

            elif 'Tell me the temperature' in self.query or 'what is the temperature' in self.query or 'temperature outside' in self.query:
                temp()

            elif 'read a book' in self.query or 'read me a book' in self.query or 'dictate a book' in self.query or 'read book' in self.query:
                Reader()

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                Speak(f"Your IP Address is {ip}")

            elif 'speedtest' in self.query or 'speed test' in self.query or 'internet speed' in self.query:
                SpeedTest()

            elif 'download speed' in self.query or 'downloading speed' in self.query:
                SpeedTest()

            elif 'uploading speed' in self.query or 'upload speed' in self.query:
                SpeedTest()

            elif 'how to' in self.query:
                Speak("Getting data from the internet")
                self.query = self.query.replace("tell me", "")
                command = self.query.replace("Jarvis", "")
                max_reult = 1
                how_to_func = search_wikihow(command, max_reult)
                assert len(how_to_func) == 1
                # how_to_func[0].print()
                Speak(how_to_func[0].summary)

            elif 'volume up' in self.query or 'increase volume' in self.query:
                Speak("Increased volume by 2 points")
                pyautogui.press("volumeup")

            elif 'volume down' in self.query or 'decrease volume' in self.query:
                Speak("Decreased volume by 2 points")
                pyautogui.press("volumedown")

            elif 'mute' in self.query:
                Speak("Muted Volume")
                pyautogui.press("volumemute")

            elif 'mobile camera' in self.query:
                import urllib.request
                import numpy as np
                URL = "http://192.168.43.1:8080/shot.jpg"
                while True:
                    img_arr = np.array(
                        bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWEBCAMERA', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break

                cv2.destroyAllWindows()

    TaskExe()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init_()
        self.ui = Ui_JarvisGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../../Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../../../Downloads/T8bahf.gif")
        self.ui.labe2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
