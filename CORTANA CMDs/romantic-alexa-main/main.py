import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
speed = engine.setProperty("rate",160)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def hello():
    talk("Hi, how do you want me to help you?")
    talk("To see what i can do, say 'show list' . ")

def run_alexa():
    command = take_command()
    print(command)
    cmd_dict = {"hello":hello()}
    for k in cmd_dict:
        if k in command:
            cmd_dict[k]
        else:
            talk("I didn't get you. Could you please repeat it again ? . If you want to exit, please say exit.")


while True:
    run_alexa()
