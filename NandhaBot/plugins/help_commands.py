import config 
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[InlineKeyboardButton(text="YT/DL", callback_data="youtube"),]]

@bot.on_callback_query()
def help(_, query):
   if query.data == "help":
      query.message.edit_caption(config.HELP,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
   elif query.data == "youtube":
       query.message.edit_caption(config.YT_HELP.format(config.NANDHA)))
