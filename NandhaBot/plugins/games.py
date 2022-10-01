from pyrogram import filters
from NandhaBot import bot
from pyrogram.types import *
import requests 
import config




@bot.on_message(filters.command("dice",config.COMMANDS))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@bot.on_message(filters.command(["dart","arrow"],config.COMMANDS))                                     
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@bot.on_message(filters.command(["football","goal"],config.COMMANDS))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@bot.on_message(filters.command("roll",config.COMMANDS))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@bot.on_message(filters.command(["throw","basket"],config.COMMANDS))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")



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
