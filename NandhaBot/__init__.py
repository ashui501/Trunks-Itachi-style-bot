import config

from pyrogram import filters , Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
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
SESSION = "BQBSaiIAFTQSEGBg5afPcIugQDMLPwN7f6WDs3PxTCgfvh-pjZLuUgjvkw6j4emqM5LU7ACrRSkGNDuv6HUky_9qYsQqQ1vkqTWvPD11vw_j2cohUrX8ucvSi4gLL8k5ZGfYVybydZipQ6UNqJo7eI60LAXoK4SzNZ3_exOSAnLNEx7MGzHv2cI1IUeGywMHZfoWp9M0OT1a8Y7ZyW3o0MjHn20dPLHMyAgBo6eHkk0Kg9flbN5DuSu30g880jhe5p02ES9InFFYNUzWRycVpHe_SURAxFOjiTzqE1vmU72aSIN4b40Ckz-nAQKbEV6ylTwCrL6tqvg0T85HIXC8Z-5mgn9x5AAAAAFIwnfgAQ"

### pyrogram Client Run Codes ###

plugins = dict(root="NandhaBot")

user = Client(name="NandhaxD",
              api_id=int(API_ID),
              api_hash=str(API_HASH),
              session_string=str(SESSION))



bot = Client(name=str(config.USERNAME), 
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
