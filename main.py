from anal.analysis import Analysis
from mouth.mouthmac import Mouth
from chatbot.Chatbot import ChatBot
from random import randint

anal = Analysis()
mouth = Mouth()
bot = ChatBot()
available_voices = ["Alex", "Fred", "Victoria", "Samantha"]
user_voices = {}


def get_voice(user):
    if user not in user_voices:
        user_voices[user] = available_voices[randint(0, len(available_voices)-1)]
    return user_voices[user]


while True:
    comment, user = bot.readChat()
    voice = get_voice(user)
    mouth.speak(comment, voice) if anal.is_negative(comment) else None
