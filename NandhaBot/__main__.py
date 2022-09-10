import config
import text
import random 
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *
from pyrogram.enums import *
from NandhaBot.helpers.dbfunctions import (
               user_add, is_user, get_users )
       


@bot.on_message(filters.command("start"))
async def start(_, message):
       user_id = message.from_user.id
       chat_id = message.chat.id
       if message.chat.type == ChatType.PRIVATE and not (await is_user(user_id):
           await add_user(user_id)
           info = await bot.get_chat(user_id) 
           user_count = len(await get_users)                                             
           await bot.send_message(chat_id, text.NEW_USERS.format(info.id,info.mention,user_count))                                           :
           await message.reply_text("<b> Nani boi? </b>")
       elif message.chat.type == ChatType.PRIVATE and (await is_user(user_id):    
            return await message.reply_text("<b> ok boi </b>")                                           
       elif not message.chat.type == ChatType.PRIVATE:                                           
           return await message.reply_text(random.choice(text.GROUP_START_TEXT)


if __name__ == "__main__":
     bot.run()
     photo_url = "http://telegra.ph/file/103f51de685933820f969.jpg"
     with bot:
        bot.send_photo(-1001724369346,photo=photo_url,caption="<b>I'm Awake Already!</b>")
