import config 
import text
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[InlineKeyboardButton(text="YT/DL", callback_data="youtube"),]]

@bot.on_callback_query()
def help(_, query):
   if query.data == "about":
      query.message.edit_caption(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
   elif query.data == "youtube":
       query.message.edit_caption(text.YT_HELP.format(text.NANDHA))
