import config

from pyrogram import filters , Client
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from aiohttp import ClientSession
import logging
import time
import os



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


### pyrogram Client Run Codes ###

plugins = dict(root="NandhaBot")
bot = Client(name=str(config.USERNAME), 
             api_id=API_ID, 
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=plugins)


DB_URL = "mongodb+srv://Bave999:Bave999@cluster0.1aheaa1.mongodb.net/?retryWrites=true&w=majority"

# mongodb from motor #
mongo = AsyncIOMotorClient(DB_URL)
mongodb = mongo.bot 

# mongodb from pymongo #
pymongo = MongoClient(DB_URL)
pymongodb = pymongo.bot

##some imports 
aiohttpsession = ClientSession()
