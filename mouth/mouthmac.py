from subprocess import Popen
from random import randint


class Mouth:
    def __init__(self):
        self.user_voices = {}
        self.available_voices = ["Alex", "Fred", "Victoria", "Samantha", "Karen", "Veena", "Moira", "Fiona", "Tessa",
                                 "Daniel"]

    def speak(self, sentence, voice="Alex"):
        cmd = ["say", "-v", voice, sentence]
        Popen(cmd)

    def get_voice(self, user):
        if user not in self.user_voices:
            self.user_voices[user] = self.available_voices[randint(0, len(self.available_voices) - 1)]
            print "user %s assigned voice %s" % (str(user), str(self.user_voices[user]))
        return self.user_voices[user]
