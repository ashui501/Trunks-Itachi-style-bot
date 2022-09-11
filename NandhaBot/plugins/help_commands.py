import config 
import text
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[
  InlineKeyboardButton(text="Youtube", callback_data="youtube"),
  InlineKeyboardButton(text="Paste", callback_data="paste"),
  InlineKeyboardButton(text="Telegraph", callback_data="telegraph"),],[
  InlineKeyboardButton(text="Wikipedia ", callback_data="wiki"),]]

BACK_HELP = [[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help"),]]
      
   

@bot.on_message(filters.command("help",config.COMMANDS))
async def help(_, message):
     await message.reply_text(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
      

@bot.on_callback_query()
async def helpdata(_, query):
   if query.data == "help":
      await query.message.edit_caption(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
   elif query.data == "youtube":
       await query.message.edit_caption(text.YT_HELP.format(text.NANDHA),reply_markup=InlineKeyboardMarkup(BACK_HELP))
   elif query.data == "paste":
       await query.message.edit_caption(text.PASTE_HELP.format(text.NANDHA),reply_markup=InlineKeyboardMarkup(BACK_HELP))
   elif query.data == "telegraph":
       await query.message.edit_caption(text.TELEGRAPH_HELP.format(text.NANDHA),reply_markup=InlineKeyboardMarkup(BACK_HELP))
   elif query.data == "wiki":
       await query.message.edit_caption(text.WIKI_HELP.format(text.NANDHA),reply_markup=InlineKeyboardMarkup(BACK_HELP))
   
