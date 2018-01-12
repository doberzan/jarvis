import pyttsx
import speech_recognition as sr
import time
import os
import socket
import serial
import select
from gtts import gTTS
from time import gmtime, strftime
import talkey

global isrunning
global myname
isrunning = True
myname = 'Declan'
global r
sr.Microphone(device_index=1, sample_rate=10000, chunk_size=1000)
r = sr.Recognizer()
# sr.Microphone(device_index=1)
# with sr.Microphone() as source:
#	r.adjust_for_ambient_noise(source, duration = 1)
SERVER_IP = '192.168.1.20'
SERVER_PORT = 9009
SERVER_ADDR = (SERVER_IP, SERVER_PORT)
global CLIENT
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    global isrunning
    global myname
    global CLIENT

    say("Jarvis 3 point oh is now online... what is your password?")
    while (password != True):
        text = recognise()
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
                say("Do you need somthing?")
                listen = True;
            if 'stop listening' in text.lower():
                say("Secrets dont make friends ya know")
                listen = False;
            if listen:
                text = text.lower()
                # if 'jarvis' in text or "travis" in text or 'germans' in text or 'services' in text or 'service' in text:
                if 'hi Jarvis' in text or 'high Jarvis' in text or 'hello Jarvis' in text:
                    say("Hello %s." % myname)
                if 'shut down' in text or 'shutdown' in text:
                    say("Shut down will now commense... Good bye!")
                    isrunning = False;
                    exit()
                if 'siri' in text.lower() or 'series' in text.lower():
                    say("No she is not! I am 100 times better than siri... go die in a hole you hater!")
                    time.sleep(1)
                    say("You know what i am going to hack into your baynk account right now")
                    time.sleep(1)
                    say("maybe you should go ask your beloved siri for help")
                    time.sleep(1)
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
                    os.system("python songplayer.py song &")
                    time.sleep(3)
                    say("Oh yeah, i am feeling it now.")
                    say("doe, doe doe doe, doe doe doe, doe doe")
                    time.sleep(5)
                    say("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh yeah")
                if 'time is it' in text:
                    print strftime("%H %M")
                    say("It is currently %s" % strftime("%H %M"))
                    say("That is in military time, by the way...")
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
                    #sendSerial('1')
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
                except:
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
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            if not r.energy_threshold < 4500:
                r.energy_threshold = 4200
            print "Listening..."
            print "Levels: %s" % r.energy_threshold
            audio = r.listen(source)
            return r.recognize_google(audio)
    except:
        return None


def say(text):
    engine = pyttsx.init('sapi5')
    engine.setProperty('voice', 'default')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def sendData(data):
    global CLIENT
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
