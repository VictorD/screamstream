import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

from threading import Event

exit = Event()

def main():
    s = openSocket()
    joinRoom(s)
    readbuffer = ""

    while not exit.is_set():
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
            
        exit.wait(60)

    print("All done!")
    # perform any cleanup here

def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit.set()

if __name__ == '__main__':
    import signal
    for sig in ('TERM', 'INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);

    main()

