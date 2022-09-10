import config 
import text
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[InlineKeyboardButton(text="YT/DL", callback_data="youtube"),]]
BACK_HELP = [[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help"),]]
      
   

@bot.on_message(filters.command("help",config.COMMANDS))
async def help(_, message):
     await message.reply_text(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
      

@bot.on_callback_query()
def helpdata(_, query):
   if query.data == "help":
      query.message.edit_caption(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
   elif query.data == "youtube":
       query.message.edit_caption(text.YT_HELP.format(text.NANDHA),reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
