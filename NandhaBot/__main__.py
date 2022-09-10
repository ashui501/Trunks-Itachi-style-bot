import config
import text
import random 
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *
from pyrogram.enums import *
from NandhaBot.helpers.dbfunctions import add_user, is_user, get_users 
       

       
BUTTONS = [[ InlineKeyboardButton(text="GROUP", url=config.GROUP_URL),
             InlineKeyboardButton(text="CHANNEL", url=config.CHANNEL_URL),],[
             InlineKeyboardButton(text="ADD ME", url="t.me/TrunksRobot?startgroup=true"),
             InlineKeyboardButton(text="ABOUT ME", callback_data="about"),]]
            
@bot.on_message(filters.command("start",config.COMMANDS))
async def start(_, message):
    try:
       user_id = message.from_user.id
       chat_id = message.chat.id
       info = await bot.get_users(user_id) 
       if message.chat.type == ChatType.PRIVATE and not await is_user(info.id):
           await add_user(info.id)
           user_count = len(await get_users())                                                                                     
           await message.reply_text(
                  "<b>Happy to See you {} ↖(^ω^)↗</b>"
                  "<b>• Read the help menu for about futures.</b>".format(info.mention),reply_markup=InlineKeyboardMarkup(BUTTONS))                                         
           await bot.send_message(chat_id, text=text.NEW_USERS.format(info.id, info.mention, user_count))
       elif message.chat.type == ChatType.PRIVATE and await is_user(info.id):  
            return await message.reply_text("""<b>Happy to See you {}!</b>\n
                 <b>Read the help menu for about futures.</b>""".format(info.mention),reply_markup=InlineKeyboardMarkup(BUTTONS))                                         
       elif not message.chat.type == ChatType.PRIVATE:                                           
           return await message.reply_text(random.choice(text.GROUP_START_TEXT))

    except Exception as error:
                 await message.reply(f"**ERROR**: {error}")
       

if __name__ == "__main__":
     bot.run()
     photo_url = "http://telegra.ph/file/103f51de685933820f969.jpg"
     with bot:
        bot.send_photo(config.GROUP_ID,photo=photo_url,caption="<b>I'm Awake Already!</b>")
