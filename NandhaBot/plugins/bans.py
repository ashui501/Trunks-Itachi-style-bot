import requests
import config

from pyrogram.types import *
from pyrogram import enums
from pyrogram import filters

from NandhaBot import bot
from NandhaBot.rank import RANK_USERS

REASON_BAN_TEXT = "Another Bitch 𝗕𝗔𝗡𝗡𝗘𝗗!\n\n𝗨𝗦𝗘𝗥: {}\n𝗥𝗘𝗔𝗦𝗢𝗡: `{}`"
BAN_TEXT = "Another Bitch 𝗕𝗔𝗡𝗡𝗘𝗗!\n\n𝗨𝗦𝗘𝗥: {}"
@bot.on_message(filters.command("ban"))
async def bans(_, message):
      reply= message.reply_to_message
      chat_id = message.chat.id
      chat = message.chat
      user_id = message.from_user.id
      api = requests.get("https://api.waifu.pics/sfw/kick").json()
      url = api["url"]
      msg = await message.reply_text("trying to ban...")
      if not reply and len(message.command) >2:
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
                   await msg.edit_text("I can't ban my rank users.")
              elif user.id == config.BOT_ID:
                     await msg.edit("`yeh noob I ban myself?`")
              elif message.from_user.id in (await RANK_USERS()):
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=REASON_BAN_TEXT.format(user.mention, reason),
                   reply_to_message_id=message.id)
              elif admin_check.privileges.can_restrict_members:
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=REASON_BAN_TEXT.format(user.mention, reason),
                   reply_to_message_id=message.id)
           except Exception as e:
               await msg.edit(str(e))

      elif not reply and len(message.command) == 2:
           user_id = message.command[1]
           try:
             user = await bot.get_users(user_id)
           except Exception as e:
                await msg.edit(str(e))
           user = await bot.get_users(user_id)
           admin_check = await bot.get_chat_member(chat_id, user.id)
           try:
              if user.id in (await RANK_USERS()):
                   await msg.edit_text("I can't ban my rank users.")
              elif user.id == config.BOT_ID:
                     await msg.edit("`yeh noob I ban myself?`")
              elif message.from_user.id in (await RANK_USERS()):
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=BAN_TEXT.format(user.mention),
                   reply_to_message_id=message.id)
              elif admin_check.privileges.can_restrict_members:
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=BAN_TEXT.format(user.mention),
                   reply_to_message_id=message.id)
           except Exception as e:
               await msg.edit(str(e))
      elif reply:
           user = reply.from_user
           admin_check = await bot.get_chat_member(chat_id, user.id)
           try:
              if user.id in (await RANK_USERS()):
                   await msg.edit_text("I can't ban my rank users.")
              elif user.id == config.BOT_ID:
                     await msg.edit("`yeh noob I ban myself?`")
              elif message.from_user.id in (await RANK_USERS()):
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=BAN_TEXT.format(user.mention),
                   reply_to_message_id=message.id)
              elif admin_check.privileges.can_restrict_members:
                   await chat.ban_member(user.id)
                   await msg.delete()
                   await bot.send_animation(animation=url,caption=BAN_TEXT.format(user.mention),
                   reply_to_message_id=message.id)
           except Exception as e:
               await msg.edit(str(e))
              
