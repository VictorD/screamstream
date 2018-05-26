import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

class ChatBot:

    def __init__(self):
        self.s = openSocket()
        joinRoom(self.s)

    def readChat(self):
        readbuffer =  self.s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            print(line)
            if "PING" in line:
                self.s.send(line.replace("PING", "PONG"))
                break
            user = getUser(line)
            message = getMessage(line)
            print user + " typed :" + message
            return str(message), str(user)
