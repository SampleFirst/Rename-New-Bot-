import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6246821370:AAEwkSN8DWpmzt1C2AoRFN12DfhcK8rhPlw")

API_ID = int(os.environ.get("API_ID", "23906038"))

API_HASH = os.environ.get("API_HASH", "dff1eb42fad7971f16da662a99c0f376")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
