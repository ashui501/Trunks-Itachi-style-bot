from pyrogram import filters , Client
import os , time

from telegraph import Telegraph
StartTime = time.time()




#main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
bot = Client(name="Mikasa", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(name)))


print("Bot is Working")

help_message = []
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)
