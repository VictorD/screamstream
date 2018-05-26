from anal.analysis import Analysis
from mouth.mouth import Mouth
from chatbot.Chatbot import ChatBot


anal = Analysis()
mouth = Mouth()
bot = ChatBot()


bot.readChat()

comment = "fuck you"
mouth.speak(comment) if anal.is_negative(comment) else ""

comment = "I hate you"
mouth.speak(comment) if anal.is_negative(comment) else ""

