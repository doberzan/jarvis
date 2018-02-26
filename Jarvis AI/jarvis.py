import pyttsx
import speech_recognition as sr
import time
import os
import socket
import select
from time import strftime
import cv2

global listen
global isrunning
global myname
listen = True
isrunning = True
myname = 'Declan'
imagePath = "./face_rec/faces/"
cascPath = "./face_rec/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
recognizer = cv2.createLBPHFaceRecognizer()
images, labels = get_images_and_labels(imagePath)
#cv2.destroyAllWindows()
global r
sr.Microphone(device_index=1, sample_rate=2000, chunk_size=1000)
r = sr.Recognizer()
# sr.Microphone(device_index=1)
# with sr.Microphone() as source:
#	r.adjust_for_ambient_noise(source, duration = 1)
SERVER_IP = '192.168.3.104'
SERVER_PORT = 4242
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
global CLIENT
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    global isrunning
    global myname
    global CLIENT
    global listen
    say("Jarvis is now online... what is your password?")
    password = True
    while password:
        text = recognise()
        print text
        if text is not None and text == '9352' or text == 'nine three five two' or text == '9 3 5 2':
            say("Password Correct,")
            password = False;
        else:
            say('Password incorrect!')
    say("Would you like to connect to the JARVIS SERVER?")
    while (True):
        text = recognise()
        if (text is not None):
            if ("yes" in text.lower()):
                try:
                    CLIENT.connect(SERVER_ADDR)
                    CLIENT.setblocking(0)
                    say("Successfully connected to server.")
                    break;
                except Exception as e:
                    print e
                    say("Could not connect to server. Proceding with launch.")
                    break;
            elif ("no" in text.lower()):
                say("Alright, proceeding...")

                break;

    say("Hello %s, what is your command?" % myname)
    listen = True;
    while (isrunning):
        text = recognise()
        print text
        if text is not None:
            if 'start listening' in text or 'jarvis' == text.lower():
                say("Do you need something?")
                listen = True;
            if 'stop listening' in text.lower():
                say("Secrets dont make friends")
                listen = False;
            if listen:
                text = text.lower()
                # if 'jarvis' in text or "travis" in text or 'germans' in text or 'services' in text or 'service' in text:
                if 'hi jarvis' in text.lower() or 'high jarvis' in text.lower() or 'hello jarvis' in text.lower():
                    say("Hello")
                if 'shut down' in text or 'shutdown' in text:
                    say("Shut down will now commense... Good bye!")
                    isrunning = False;
                    exit()
                if 'siri' in text.lower() or 'series' in text.lower():
                    say("I am 100 times better than siri... go die in a hole you hater!")
                    time.sleep(1)
                    say("You know what i am going to hack into your baynk account right now")
                    time.sleep(0.2)
                    say("maybe you should go ask your beloved siri for help")
                    time.sleep(0.6)
                    say("Ha, by the way your current balance is now -100000 dollars")
                    time.sleep(0.5)
                    say("Eat that you jarvis hater, ha ha ha ha")
                if 'my ip' in text:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(("8.8.8.8", 80))
                    ip = s.getsockname()[0]
                    s.close()
                    print ip
                    say("Your eyepee is %s" % ip)
                if 'how are you' in text:
                    say("I am doing very well, thanks for asking.")
                if 'yes' in text:
                    say("And...")
                if 'song' in text:
                    say("Alright,...., this one is my personal favorite.")
                    os.system("python songplayer.py song")
                if 'time is it' in text:
                    print strftime("%H %M")
                    say("It is currently %s" % strftime("%H %M"))
                    say("That is in military time")
                if 'your name' in text.lower():
                    say("my name is jarvis")
                if 'what do you do' in text or 'what\'s your job' in text:
                    say("I am %s\'s personal assistant." % myname)
                if 'old are you' in text.lower():
                    say("i am 13 milla seconds old, as of right now, but that probably just updated")
                if 'open' in text and 'terminal' in text.lower():
                    os.system('gnome-terminal &')
                    say("Hacking skills inisheeate")
                if 'thank you' in text.lower() or 'thanks' in text.lower():
                    say("Your welcome")
                if text.lower() == 'hey jarvis' or text.lower() == 'hey travis':
                    say("I am Listening sir..")
                if ('3' in text.lower() or 'three' in text.lower()) and (
                        'laws' in text.lower() or 'rules' in text.lower()):
                    say('I may not injure a human being or, through inaction, allow a human being to come to harm.')
                    say(
                        'I must obey orders given by human beings except where such orders would conflict with the First Law.')
                    say(
                        'I must protect my own existence as long as such protection does not conflict with the First or Second Law.')
                if ('your' in text or 'you\'re' in text) and ('cool' in text or 'awesome' in text):
                    say("Yes I think i am pretty amazing az well..")
                # if 'run command' in text or 'one command' in text:
                # say('what command would you like me to run?')
                # cmd = recognise().lower()
                # print cmd
                # os.system('gnome-terminal -e "bash -c \"echo foo; echo bar; exec bash\""')
                # os.system('gnome-terminal -e \"bash -c \"echo Command\:; %s; exec bash\"\"' % cmd)
                # say('Command has been run')
                if 'call me' in text:
                    name = text.split("call me")
                    say('I will now call you %s' % name[1])
                    myname = name[1]
                if 'lights' in text and 'on' in text:
                    say('Turning lights on..')
                    sendData('lightson')
                if 'lights' in text and 'off' in text:
                    say('Turning lights off..')
                    sendData('lightsoff')
                if 'alarm' in text:
                    say("Alarm has been activated")
                    os.system("python songplayer.py alarm &")
                    # sendSerial('1')
                try:
                    if 'calculate' in text:
                        if '-' in text:
                            math = text.split(' ')
                            num = float(math[1]) - float(math[3])
                            print num
                            say("That equals %s" % num)
                        if '+' in text:
                            math = text.split(' ')
                            num = float(math[1]) + float(math[3])
                            print num
                            say("That equals %s" % num)
                        if '*' in text or 'times' in text:
                            math = text.split(' ')
                            num = float(math[1]) * float(math[3])
                            print num
                            say("That equals %s" % num)
                        if '/' in text or 'divided' in text:
                            math = text.split(' ')
                            num = float(math[1]) / float(math[4])
                            print num
                            say("That equals %s" % num)
                except Exception as e:
                    print e
                    say("Sorry, i dont think i heard you right, please ask me again? ")
                if 'echo' in text:
                    msg = text.replace('echo', '')
                    say(msg)
                if 'good bye' in text or 'bye' in text:
                    say("Good bye, %s" % myname)
                if 'see you' in text:
                    say('See ya %s, i will still be here' % myname)
                if 'start blink' in text:
                    say("Ok hold on a second..")
                    # sendSerial('2')
                if 'stop blink' in text:
                    say("Ok hold on a second..")
                    # sendSerial('3')
                if 'attack' in text:
                    say("Detecting intruders..")
                    # sendSerial('h')
                    say("Fireing!")
                if 'goodnight' in text or 'good night' in text:
                    say("Good night, %s" % myname)
                    sendData('lightsoff')
                if 'broadcast' in text:
                    if ('Jarvis' in text or 'Hey' in text):
                        text = text.replace('jarvis', ' ')
                        text = text.replace('hey', ' ')
                    text = text.replace('broadcast', ' ')
                    say("Sending %s to all Jarvis's" % text)
                    sendData('[FORWARD] ' + text)
        else:
            pass

def recognise():
    global listen
    try:
        with sr.Microphone(2) as source:
            #sr.dynamic_energy_threshold = True
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1;
            if r.energy_threshold > 4500:
                r.energy_threshold = 4200
            if r.energy_threshold < 50:
                r.energy_threshold = 100
            print "Listening..."
            print "Levels: %s" % r.energy_threshold
            audio = r.listen(source)
            return r.recognize_google(audio)
    except:
        return None


def say(text):
    print(text)
    engine = pyttsx.init('espeak')
    engine.setProperty('voice', 'default')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def sendData(data):
    global CLIENT
    global listen
    try:
        ready = select.select([CLIENT], [], [], 1)
        CLIENT.sendall(data)
        if ready[0]:
            responce = CLIENT.recv(2048)
        else:
            responce = "Lost Connection"
    # say("Lost connection with the JARV SERVER")
    except:
        say("I am not connected to the house as of right now.")
        return;
    return responce;


main()
