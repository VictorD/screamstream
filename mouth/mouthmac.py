from subprocess import call


class Mouth:
    def __init__(self, voice="Alex"):
        self.voice = voice

    def speak(self, sentence):
        call(["say", "-v", self.voice, sentence])

    def close(self):
        pass
