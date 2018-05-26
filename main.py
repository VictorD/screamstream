from anal.analysis import Analysis
from mouth.mouthmac import Mouth
from chatbot.Chatbot import ChatBot
from random import randint
import threading

anal = Analysis()
mouth = Mouth()
bot = ChatBot()
voices = ["Alex", "Fred", "Victoria", "Samantha"]

def say_something_im_giving_up_on_you(comment):
    voice = voices[randint(0, 3)]
    mouth.speak(comment, voice) if anal.is_negative(comment) else None

while True:
    comment = str(bot.readChat())
    t = threading.Thread(target=say_something_im_giving_up_on_you, args=(comment,))
    t.start()