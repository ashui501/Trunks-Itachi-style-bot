from pyrogram import filters , Client
import os , time

StartTime = time.time()


### Add This Vars On Your Deploying App. ###
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)


### Client Run Code ###
plugins = dict(root="NandhaBot/pligins")

bot = Client(name="nandhabot", 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=plugins)

if __name__ == "__main__:
     bot.start()
