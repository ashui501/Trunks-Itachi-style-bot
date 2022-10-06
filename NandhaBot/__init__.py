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
SESSION = os.environ.get("SESSION", "BQBSaiIAo99yvNLnCudpQWAa8L2ivVFdbWzJt27Khgr-sMpVHSRcdjNfYD8J8zBh5jChyc55xZSaNjEMhtwMOGYzqs6e0CC8Bgrghuu5hH2HCre-AAyXHs2EglEsrnrXWsrkrFgLJ2tDgK2IEG4QPvRxlbaDrvCZ-40V_krnLIVaxcMj5w5wiSrUMWHuUCYnNtITPUTx8ap8B5FHcjuyxXMNVnvr1tSDcLWztn-KbhexULPUIZWdvpVDEBR-ONGH95VdSI12HiC8L03BeBowJd4sbW75NO7rfgjpG0ouSxdl31wB5MW8cvaBzY6YAHSJwmc3BgytxcnFUktw2HdxLvn9g4SX4gAAAAFIwnfgAQ")

### pyrogram Client Run Codes ###

plugins = dict(root="NandhaBot")

user = Client(name="NandhaxD",
              api_id=int(API_ID),
              api_hash=str(API_HASH),
              bot_token=str(BOT_TOKEN),
              session_string=str(SESSION),
              plugins=plugins)

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
