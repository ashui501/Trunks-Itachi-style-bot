import requests

from pyrogram.types import *
from pyrogram import enums
from pyrogram import filters

from NandhaBot import bot
from NandhaBot.rank import RANK_USERS

BAN_TEXT = "Another Bitch 𝗕𝗔𝗡𝗡𝗘𝗗!\n\n 𝗨𝗦𝗘𝗥: {}\n𝗥𝗘𝗔𝗦𝗢𝗡: `{}`"

@bot.on_message(filters.command("ban"))
async def bans(_, message):
      reply= message.reply_to_message
      chat_id = message.chat.id
      chat = message.chat
      user_id = message.from_user.id
      api = requests.get("https://api.waifu.pics/sfw/kick").json()
      url = api["url"]
      msg = await message.reply_text("trying to ban...")
      if reply or not reply and len(message.command) >2:
           user_id = message.command[1]
           reason = message.text.split(None, 2)[2]
           try:
             user = await bot.get_users(user_id)
           except Exception as e:
                await msg.edit(str(e))
           user = await bot.get_users(user_id)
           admin_check = await bot.get_chat_member(chat_id, user.id)
           try:
              if user.id in (await RANK_USERS()):
                   await msg.reply_text("I can't ban my rank users.")
              elif message.from_user.id in (await RANK_USERS()):
                   await chat.ban_member(user.id)
                   await msg.edit(BAN_TEXT.format(user.first_name, reason))
              elif admin_check.privileges.can_restrict_members:
                   await chat.ban_member(user.id)
                   await msg.edit(BAN_TEXT.format(user.first_name, reason))

           except Exception as e:
               await msg.edit(str(e))
              
