
import config 
import strings
from pyrogram import filters
from pyrogram import enums
from pyrogram.types import *
from NandhaBot import bot


#buttons

HELP_BACK_BUTTONS = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="𝗠𝗜𝗦𝗖 𝗵𝗲𝗹𝗽", callback_data="misc_help")],[
  InlineKeyboardButton(text="𝗚𝗔𝗠𝗘 𝗵𝗲𝗹𝗽", callback_data="game_help")],[
  InlineKeyboardButton(text="𝗡𝗘𝗞𝗢 𝗵𝗲𝗹𝗽", callback_data="neko_help"),]])

BACK_HELP = InlineKeyboardMarkup([[InlineKeyboardButton(text="BACK TO HELP MENU", callback_data="help_back")]])
      
   
help_button = InlineKeyboardMarkup([[
InlineKeyboardButton("𝗢𝗣𝗘𝗡 𝗜𝗡 𝗗𝗠",url=f"https://t.me/{config.USERNAME}?start"),
InlineKeyboardButton("𝗢𝗣𝗘𝗡 𝗜𝗡 𝗚𝗥𝗢𝗨𝗣",callback_data="help_back")]])


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
      query.message.edit(strings.MISC_HELP.format(strings.NANDHA),reply_markup=BACK_HELP)

@bot.on_callback_query(filters.regex("game_help"))
def gamehelp(_, query):
      query.message.edit(strings.GAME_HELP.format(strings.NANDHA),reply_markup=BACK_HELP)

@bot.on_callback_query(filters.regex("neko_help"))
def nekohelp(_, query):
      query.message.edit(strings.NEKOS_HELP.format(strings.NANDHA),reply_markup=BACK_HELP)


