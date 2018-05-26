from anal.analysis import Analysis
from mouth.mouth import Mouth
from chatbot.Chatbot import ChatBot


anal = Analysis()
mouth = Mouth()
bot = ChatBot()

while True:
	comment = str(bot.readChat())
	mouth.speak(comment) if anal.is_negative(comment) else None


mouth.close()