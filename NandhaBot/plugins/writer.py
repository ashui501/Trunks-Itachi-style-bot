import config
import io

from NandhaBot import bot
from pyrogram.types import *
from pyrogram import filters


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
def write_file(_, query):
    if query.from_user.id == user_id:
        msg = query.message.reply_text("Sending File...")
        with io.BytesIO(str.encode(text)) as file:
             file.name = "writer.txt"
        query.message.reply_document(
           document=file)
    else:
        query.answer("This Message Not For You", show_alert=True)
                 
