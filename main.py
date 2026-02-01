# -- coding: utf-8

################# VER #################

VERSION = "1.0.0"
PATCH = "a"

################# VER #################

import asyncio, colorama, sys, os, time
from datetime import datetime, timedelta
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telebot.async_telebot import AsyncTeleBot
from log.log import Log
from config import BOT_TOKEN, BOT_USERNAME, LINK, BUT_TEXT

log = Log("Bot")

bot = AsyncTeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
async def message(message: Message):
    try:
        
        with open("message.txt", "r") as f:
            _message = f.read()
        
        markup = None

        if LINK and BUT_TEXT:
            markup = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(BUT_TEXT, url=LINK))

        await bot.send_message(message.chat.id, f"<b>{_message}</b>", parse_mode='html', reply_markup=markup, disable_web_page_preview=True)

    except Exception as e:
        log.exception(f"Failed to send message to user: {message.chat.id}")


if __name__ == "__main__":
    try:
        _log_session = log.log_session
        log.warning("Distribution was started")
        
        print(colorama.Fore.LIGHTBLUE_EX+"============"+(datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")+"====================")
        print(colorama.Fore.LIGHTMAGENTA_EX+"============Dist version: " + str(VERSION)+PATCH + "===================")
        print(colorama.Fore.LIGHTCYAN_EX+"============Log: "+_log_session + "====") 
        print(colorama.Fore.LIGHTGREEN_EX+"============Dist started===========================")
        print(colorama.Fore.RESET)

        asyncio.run(bot.polling(non_stop=True, request_timeout=100, skip_pending=True))
    except (KeyboardInterrupt, SystemExit):
        log.warning("Bot was stopped")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")
        time.sleep(5)
