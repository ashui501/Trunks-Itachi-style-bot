from pyrogram import filters
from NandhaBot import bot
import requests 
import config

BUTTON = [[InlineKeyboardButton(text="🔄",callback_data="basketball")]]

@bot.on_message(filters.command("basketball"))
async def basket(_, message):
       id = message.id
       await bot.send_dice(message.chat.id, "🏀",reply_to_message_id=message.id,
                           reply_markup=InlineKeyboardMarkup(BUTTON)


@bot.on_callback_query()
async def games(_, query):                  
    if query.data == "basketball":
        await query.message.delete()
        await bot.send_dice(message.chat.id, "🏀",reply_to_message_id=id,reply_markup=InlineKeyboardMarkup(BUTTON)
                 

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
