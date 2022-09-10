import config
import text
import random 
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *
from pyrogram.enums import *


@bot.on_message(filters.command("start"))
async def start(_, message):
       if message.chat.type == ChatType.PRIVATE:
           return await message.reply_text("<b> Nani boi? </b>")
       elif not message.chat.type == ChatType.PRIVATE:
           return await message.reply_text(random.chioce(text.GROUP_START_TEXT))


if __name__ == "__main__":
     bot.run()
     photo_url = "http://telegra.ph/file/103f51de685933820f969.jpg"
     with bot:
        bot.send_message(-1001724369346,photo=photo_url,caption="<b>I'm Awake Already!</b>")
