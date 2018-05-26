from anal.analysis import Analysis
from mouth.mouthmac import Mouth
from chatbot.Chatbot import ChatBot
from random import randint

anal = Analysis()
mouth = Mouth()
bot = ChatBot()
voices = ["Alex", "Fred", "Victoria", "Samantha"]

while True:
    comment = str(bot.readChat())
    voice = voices[randint(0, 3)]
    mouth.speak(comment, voice) if anal.is_negative(comment) else None
