import PyPDF2                   #To read pdf files
import pyttsx3                  # covert text to speech
import speech_recognition as sr         #listen to your command via google api
import pywhatkit as wk
import datetime
import wikipedia as wiki
import pyjokes
import webbrowser
import smtplib
import requests
import os
#PyAudio
listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)                #pyttsx3
    engine.runAndWait()

def wishMe():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('Good Morning!')

    elif hour>=12 and hour<18:
        talk('Good Afternoon!')

    else:
        talk('Good Evening!')

    talk(f"I am Jarvis Sir  Current Time is {time} Please tell me how may I help you")
    print(f"I am Jarvis Sir.Current Time is {time} Please tell me how may I help you")


def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak....')
            listener.pause_threshold = 0.5                #It will wait for 2 sec then speak text will appear
            voice = listener.listen(source, timeout=10.0, phrase_time_limit=10)   #time(you can say within 5 sec
            print('Reconizing.....')                                          #Maximum gap b/t phrases is 5 sec
            command = listener.recognize_google(voice)
            command = command.lower()
        return command
    except Exception as e:
        print(e)
        talk('You took too long to speak! Try Again')
        exit()

def read_pdf():
    book = open('oop.pdf', 'rb') #read binary
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    talk(f'Number of pages are {pages}')
    print(f'Number of pages are {pages}')
    talk('Please Specify the page number')
    page_number = int(input('ENTER THE PAGE NUMBER: '))
    page = pdfReader.getPage(page_number - 1)
    text = page.extractText()
    talk(text)

def run_jarvis():
    wishMe()
    while True:
        command = take_command()
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
        print(f'User Said: {command}')
        if 'play' in command:
            song = command.replace('play', '')     #' '  empty string
            talk('playing' + song)
            print('playing' + song)
            wk.playonyt(song)

        elif 'open notepad' in command:
            path = "C:\Windows\system32\\notepad.exe"
            talk('Openning Notepad')
            print('Openning Notepad....')
            os.startfile(path)

        elif 'open cmd' or 'open command prompt' in command:
            os.system('start cmd')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')     #strf = standered formatting time
            print(time)                                             #%I = 12 hr format ,%M = minutes, %p = Am/Pm
            talk('Current time is' + time)
        elif 'tell me about' in command:
            data = command.replace('tell me about', '')
            info = wiki.summary(data, 2)
            print(info)
            talk('Here is what I found Sir!' + info)

        elif 'open youtube' in command:
            print('Openning youtube')
            webbrowser.open('www.youtube.com')

        elif 'open stackoverflow' in command:
            print('Openning stackoverflow')
            webbrowser.open('www.stackoverflow.com')

        elif 'open facebook' in command:
            print('Openning facebook')
            webbrowser.open('www.facebook.com')

        elif 'joke' in command:
            n = pyjokes.get_joke()
            print(n)
            talk(n)

        elif 'search' in command:
            data = command.replace('search', '')
            talk('Here is what I found')
            print('Here is what I found')
            wk.search(data)

        elif 'change' in command:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            talk('Hello I am Alice How can help you sir')

        elif 'reset' in command:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            talk('Hello I am Jarvis How can help you sir')

        elif 'whatsapp' in command:
            try:
                data = input('Enter the phone number ')
                modified_data = "+91" + str(data)
                talk('Tell me What message should I send sir ')
                message = take_command()
                hr = int(input('Enter the time in hour format '))
                min = int(input('Enter the minutes '))
                sec = int(input('Enter the time after which message will be send '))
                wk.sendwhatmsg(modified_data,message,hr, min, sec)
            except Exception as e:
                print(e)
                talk('Sorry your watsapp cannot be send')
                print('Sorry your watsapp cannot be send')


        elif 'sleep' in command:
            talk('Ok going to sleep now you can call me anytime Sir')
            print('Ok going to sleep now you can call me anytime Sir')
            break

        elif 'weather' in command:
            talk('Tell me the location sir')
            search = take_command()
            print('Displaying weather results')
            talk('Displaying weather results')
            url = "https://wttr.in/{}".format(search)               #requests module
            res = requests.get(url)
            print(res.text)

        elif 'send email' in command:
            talk('Tell me what should I send sir')
            content = take_command()
            talk('Please input the gmail account of the reciever')
            print('Enter the gmail:')
            to = input()
            sendmail(to, content)
            talk('Your email has been send sir')

        elif 'read' in command:
            read_pdf()

        elif 'shutdown' in command:
            talk('Initiating Shutdown procedure Hope your day was Awesome')
            print('Initiating Shutdown procedure Hope your day was Awesome')
            exit()
        else:
            talk('Please Repeat Sir')
            print('Please Repeat Sir...')


if __name__ == '__main__':
    #wishMe()
    while True:
        permission = take_command()
        if 'jarvis' in permission:
            run_jarvis()
        else:
            print('Error')
            exit()
