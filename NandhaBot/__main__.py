from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *



if __name__ == "__main__":
     bot.run()
     photo_url = "http://telegra.ph/file/103f51de685933820f969.jpg"
     with bot:
        bot.send_photo(chat_id=-1001724369346,photo=photo_url,caption="I'm Awake Now!")
