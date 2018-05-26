from subprocess import call


class Mouth:
    def __init__(self):
        pass

    def speak(self, sentence, voice="Alex"):
        call(["say", "-v", voice, sentence])

    def close(self):
        pass
