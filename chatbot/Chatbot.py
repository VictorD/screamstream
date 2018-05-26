import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

from threading import Event

exit = Event()


class ChatBot:

    def __init__():
        s = openSocket()
        joinRoom(s)

    def readChat():
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            print(line)
            if "PING" in line:
                s.send(line.replace("PING", "PONG"))
                break
            user = getUser(line)
            message = getMessage(line)
            print user + " typed :" + message
            if "You Suck" in message:
                sendMessage(s, "No, you suck!")
                break