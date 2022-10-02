import config
import io
import requests
from NandhaBot import bot
from pyrogram.types import *
from pyrogram import filters
from NandhaBot.helpers.paste import batbin



@bot.on_message(filters.command("write"))
def writer (_, message):
     global text, user_id
     if len(message.command) <2:
         return message.reply_text("`Give TEXT to send as file somthing.`")
     text = message.text
     user_id = message.from_user.id
     BUTTON = [[InlineKeyboardButton(text="FILE",callback_data="write_file"),
                InlineKeyboardButton(text="PHOTO",callback_data="write_photo"),]]
     message.reply_text("check what you wanted, below!",
     reply_markup=InlineKeyboardMarkup(BUTTON))



@bot.on_callback_query(filters.regex("write_file"))
async def write_file(_, query):
    if query.from_user.id == user_id:
        msg = await query.message.reply_text("Sending File...")
        write_text = text.replace("/write", "")
        with io.BytesIO(str.encode(write_text)) as file:
             file.name = "writer.txt"
             link = await batbin(write_text)
             await query.message.reply_document(document=file, caption=link)
             await msg.delete()
             await query.message.delete()
    else:
        await query.answer("This Message Not For You", show_alert=True)
                 
@bot.on_callback_query(filters.regex("write_photo"))
def write_photo(_, query):
     if query.from_user.id == user_id:
        msg = query.message.reply_text("Sending File...")
        write_text = text.split(None, 1)[1]
        API = f"https://api.sdbots.tk/write?text={write_text}"
        url = requests.get(API).url
        query.message.reply_document(document=url,caption=url)
        msg.delete()
        query.message.delete()

     else:
        query.answer("This Message Not For You", show_alert=True)
