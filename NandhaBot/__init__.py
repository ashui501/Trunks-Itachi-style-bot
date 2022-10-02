from pyrogram import filters , Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from aiohttp import ClientSession
import logging
import time
import os
import telebot


# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)


### Add This Vars On Your Deploying App. ###
API_ID = os.environ.get("API_ID", 7126006)
API_HASH = os.environ.get("API_HASH", "f92b05be529835381859ead64a195fa2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5515671520:AAFcuSq058VM8QmShpweRs1p0u0U5pWHIH8")


### telebot clinet run code ##

telebot = telebot.TeleBot(BOT_TOKEN)

### pyrogram Client Run Code ###
plugins = dict(root="NandhaBot")

bot = Client(name="nandhabot", 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=plugins)

###Mogondb Functions # You can use pymongo module also
DB_URL = "mongodb+srv://Bave999:Bave999@cluster0.1aheaa1.mongodb.net/?retryWrites=true&w=majority"
# mongo db url here
mongo = MongoClient(DB_URL)
mongodb = mongo.bot 

##some imports 
aiohttpsession = ClientSession()
