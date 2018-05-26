from subprocess import call


class Mouth:
    def __init__(self):
        pass

    def speak(self, sentence):
        call(["say", sentence])

    def close(self):
        pass
