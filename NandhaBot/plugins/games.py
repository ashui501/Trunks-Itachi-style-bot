from pyrogram import filters
from NandhaBot import bot
from pyrogram.types import *
import requests 
import config



@bot.on_message(filters.command(["basketball","basket"],config.COMMANDS))
async def basket(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "🏀",reply_to_message_id=message.id)
                           
       
@bot.on_message(filters.command(["dart","target"],config.COMMANDS))
async def dart(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "🎯",reply_to_message_id=message.id)
                           
       
       
@bot.on_message(filters.command("football",config.COMMANDS))
async def football(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "⚽",reply_to_message_id=message.id)
                           
@bot.on_message(filters.command("roll",config.COMMANDS))
async def rollball(_, message):
       global id, user
       id = message.id
       user = message.from_user.id
       await bot.send_dice(message.chat.id, "🎰",reply_to_message_id=message.id)
                           


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
