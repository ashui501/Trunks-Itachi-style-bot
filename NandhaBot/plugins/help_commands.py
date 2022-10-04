
import config 
import strings
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[
  InlineKeyboardButton(text="Misc help", callback_data="misc_help")]]

BACK_HELP = [[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help"),]]
      
   

@bot.on_message(filters.command("help",config.COMMANDS))
def help(_, message):
     message.reply_text(strings.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
      
@bot.on_callback_query(filters.regex("misc_help"))
def helpdatas(_, query):
        query.message.edit(strings.MISC_HELP.format(strings.NANDHA))
