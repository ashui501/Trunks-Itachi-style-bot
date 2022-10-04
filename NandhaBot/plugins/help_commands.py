
import config 
import strings
from pyrogram import filters
from pyrogram import enums
from pyrogram.types import *
from NandhaBot import bot


#buttons

HELP_BACK_BUTTONS = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Misc help", callback_data="misc_help")]])

BACK_HELP = InlineKeyboardMarkup([[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help")]])
      
   
help_button = InlineKeyboardMarkup([[
InlineKeyboardButton("OPEN IN DM",url=f"https://t.me/{config.USERNAME}?start"),
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
def helpbacks(_, query):
     query.message.edit(strings.HELP_TEXT,reply_markup=HELP_BACK_BUTTONS)

@bot.on_callback_query(filters.regex("misc_help"))
def mischelp(_, query):
      query.message.edit(strings.MISC_HELP.format(config.NANDHA))
