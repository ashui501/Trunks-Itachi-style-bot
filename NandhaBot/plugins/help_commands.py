
import config 
import strings
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot


#buttons

HELP_BACK_BUTTONS = [[
  InlineKeyboardButton(text="Misc help", callback_data="misc_help")]]

BACK_HELP = InlineKeyboardMarkup([[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help")]])
      
   
help_button = InlineKeyboardMarkup([[
InlineKeyboardButton("OPEN IN DM",url="https://t.me/trunksRobot?start"),
InlineKeyboardButton("OPEN IN GROUP",callback_data="help_back")]])


#commads

@bot.on_message(filters.command("help",config.COMMANDS))
def help(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        message.reply_text(strings.HELP_TEXT,reply_markup=HELP_BACK_BUTTONS)
    else:
        message.reply_text(strings.HELP_GROUP_TEXT,reply_markup=help_button)


      
#callbackdatas



@bot.on_callback_query(filters.regex("help_back"))
def helpdatas(_, query):
        def help(_, message):
     message.reply_text(strings.HELP_TEXT,reply_markup=help_button)


