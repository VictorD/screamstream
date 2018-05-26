import pyttsx


class Mouth:
    def __init__(self):
        self.engine = pyttsx.init()

    def speak(self, sentence):
        self.engine.say('Good morning.')
        self.engine.runAndWait()



