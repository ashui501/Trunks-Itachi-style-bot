import requests
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *

baby = InlineKeyboardMarkup([[
InlineKeyboardButton(text="Send as File", callback_data="logo_file"),]])

@bot.on_message(filters.command("logo"))
def logo(_, message):
    global user_id, req
    user_id = message.from_user.id
    if len(message.command) <2:
       return message.reply_text("Give Me logo name.")
    logo_name = message.text.split(None,1)[1]
    msg = message.reply_text("logo generating...")
    try:
       API = f"https://api.sdbots.tk/anime-logo?name={logo_name}"
       req = requests.get(API).url
       bot.send_photo(
            message.chat.id,
            photo=req,
            file_name="logo.jpg"
            caption=f"telegraph link:[link]({req})\nby @TrunksRobot"),
            reply_to_message_id=message.id,reply_markup=baby)
    except Exception as e:
        msg.edit_text(str(e))
  
     
@bot.on_callback_query(filters.regex("logo_file"))
def sendlogoasfile(_, query):
     if query.from_user.id == user_id:
        msg = query.message.reply_text("Sending file....")
        file = query.message.download()
        query.message.reply_document(
          file_name="logo.png",file,caption=f"telegraph link:[link]({req})\nby @TrunksRobot")
        query.message.delete()
        msg.delete()
     else:
         query.answer("This Message Not For You!", show_alert=True)
