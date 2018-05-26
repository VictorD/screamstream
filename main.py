from anal.analysis import Analysis
from mouth.mouthmac import Mouth
from chatbot.Chatbot import ChatBot

anal = Analysis()
mouth = Mouth()
bot = ChatBot()


while True:
    try:
        comment, user = bot.readChat()
        voice = mouth.get_voice(user)
        mouth.speak(comment, voice) if anal.is_negative(comment) else None
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        print(e)
