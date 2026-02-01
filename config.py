import dotenv, os

dfile = lambda: dotenv.find_dotenv('.env')
dotenv.load_dotenv(dfile())

get_var = lambda name, _default=None: os.getenv(name, default=_default)

# Bot
BOT_TOKEN = get_var("BOT_TOKEN")
BOT_USERNAME = get_var("BOT_USERNAME")

# Message
FILENAME = get_var("FILENAME", _default="message.txt")

# Markup
LINK = get_var("LINK", _default=None)
BUT_TEXT = get_var("BUT_TEXT", _default=None)