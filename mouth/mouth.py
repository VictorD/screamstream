import pyttsx


class Mouth:
    def __init__(self):

        self.engine = pyttsx.init()
        for voice in self.engine.getProperty('voices'):
            print voice
            desiredVoice = "Cepstral Shouty"
            if voice.name == desiredVoice:
                self.engine.setProperty('voice', voice.id)

    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
    
    def close():
        self.engine.stop()



