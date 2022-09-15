from pyrogram import filters
from NandhaBot import bot
from pyrogram.types import *
import requests 
import config

BASKET_BUTTON = [[InlineKeyboardButton(text="🔄",callback_data="basketball")]]
FOOT_BUTTON = [[InlineKeyboardButton(text="🔄",callback_data="football")]]


@bot.on_message(filters.command("basketball"))
async def basket(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "🏀",reply_to_message_id=message.id,
                           reply_markup=InlineKeyboardMarkup(BASKET_BUTTON))
       
@bot.on_message(filters.command("football"))
async def football(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "⚽",reply_to_message_id=message.id,
                           reply_markup=InlineKeyboardMarkup(FOOT_BUTTON))


@bot.on_callback_query()
async def games(_, query):                  
    if query.data == "basketball" and query.from_user.id == user:
        await query.message.delete()
        await bot.send_dice(query.message.chat.id, "🏀",reply_to_message_id=id,reply_markup=InlineKeyboardMarkup(BASKET_BUTTON))
    elif query.data == "football" and query.from_user.id == user:
        await query.message.delete()
        await bot.send_dice(query.message.chat.id, "⚽",reply_to_message_id=id,reply_markup=InlineKeyboardMarkup(FOOT_BUTTON))
              

#Truth OR Dare Game

@bot.on_message(filters.command("dare",config.COMMANDS))
async def dare(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
**Hey! {reply.from_user.mention}
{m.from_user.mention} give you a dare!
Dare**: `{text}`
               """
               await m.reply_text(dare)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
               text = api["question"]
               dare = f"""
 Hey! {m.from_user.mention} your dare here!
 **Dare**: `{text}`
               """
               await m.reply_text(dare)

@bot.on_message(filters.command("truth",config.COMMANDS))
async def truth(_, m):
         reply = m.reply_to_message
         if reply:
               api = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
               text = api["question"]
               truth = f"""
  Hey! {reply.from_user.mention}
  {m.from_user.mention} give you a Truth!
  **Truth**: `{text}`
               """
               await m.reply_text(truth)
         else:
               api = requests.get("https://api.truthordarebot.xyz/v1/Truth").json()
               text = api["question"]
               truth = f"""
    Hey! {m.from_user.mention} your Truth here!
    **Truth**: `{text}`
               """
               await m.reply_text(truth)
