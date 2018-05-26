from subprocess import Popen


class Mouth:
    def __init__(self):
        pass

    def speak(self, sentence, voice="Alex"):
        cmd = ["say", "-v", voice, sentence]
        Popen(cmd)
