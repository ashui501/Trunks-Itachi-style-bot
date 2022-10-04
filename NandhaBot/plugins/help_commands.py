
import config 
import strings
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

HELP_BUTTONS = [[
  InlineKeyboardButton(text="Youtube", callback_data="youtube"),
  InlineKeyboardButton(text="Paste", callback_data="paste"),
  InlineKeyboardButton(text="Telegraph", callback_data="telegraph"),],[
  InlineKeyboardButton(text="Wiki", callback_data="wiki"),
  InlineKeyboardButton(text="Github", callback_data="github"),
  InlineKeyboardButton(text="Game", callback_data="game"),
  InlineKeyboardButton(text="Nekos", callback_data="nekos")]]

BACK_HELP = [[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help"),]]
      
   

@bot.on_message(filters.command("help",config.COMMANDS))
async def help(_, message):
     await message.reply_text(text.HELP_TEXT,reply_markup=InlineKeyboardMarkup(HELP_BUTTONS))
      
