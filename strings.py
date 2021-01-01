# (c) https://t.me/iamarupmandal
# TeleBot - UserBot
# Copyright (C) 2020 TeleBot
#
# You should have received a copy of the GNU Affero General Public License along with this program.
# If not, see <https://github.com/arupmandal/TeleBot>.
import os

os.system('pip install --upgrade pip')
os.system('pip install telethon==1.18.2')
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

a = """
 _____    _      _           _   
|_   _|__| | ___| |__   ___ | |_ 
  | |/ _ \ |/ _ \ '_ \ / _ \| __|
  | |  __/ |  __/ |_) | (_) | |_ 
  |_|\___|_|\___|_.__/ \___/ \__|
"""
print(a)
print("""Session String Generator.
Please go to https://my.telegram.org or https://t.me/ScrapperRoBot and get your details."""
      )
print("")

APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as tb:
    print("")
    print("Below is your STRING_SESSION")
    print("")
    print(tb.session.save())
    print("")
    print("This can be found in your saved messages in telegram too.")
    tele = tb.send_message("me", f"`{tb.session.save()}`")
    tele.reply("The above is the `STRING_SESSION`.\n@iamarupmandal")
