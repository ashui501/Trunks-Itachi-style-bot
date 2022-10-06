import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot, user
from NandhaBot.rank import RANK_USERS as RANK

INFO_TEXT = """
𝗨𝗦𝗘𝗥𝗦𝗧𝗔𝗧𝗨𝗦:

**ID:** `{}`
**Name:** {}
**Username:** @{}
**Mention:** {}

**UserStatus:**\n`{}`\n
**RankUser**: {}

**Dc:** {}
**Bio:** {}

`note were sends you necessary information about user not at all`!
"""

async def userstatus(user_id):
   try:
      user = await bot.get_users(user_id)
      x = user.status
      if x == enums.UserStatus.RECENTLY:
         return "User was seen recently."
      elif x == enums.UserStatus.LAST_WEEK:
          return "User was seen last week."
      elif x == enums.UserStatus.LONG_AGO:
          return "User was seen long ago."
      elif x == enums.UserStatus.OFFLINE:
          return "User is offline."
      elif x == enums.UserStatus.ONLINE:
         return "User is online."
   except:
        return "somthing wrong happened!"
    



@bot.on_message(filters.command(["info","userinfo"],config.COMMANDS))
async def userinfo(_, message):
    
     chat_id = message.chat.id
     user_id = message.from_user.id
     if not message.reply_to_message and len(message.command) == 2:
         
         try:
            user_id = message.text.split(None, 1)[1]
            user_info = await bot.get_chat(user_id)
            user = await bot.get_users(user_id)
            rank = user.id in (await RANK())
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await bot.download_media(user.photo.big_file_id)
            await bot.send_photo(chat_id,photo=photo, caption=INFO_TEXT.format(
id,name, username, mention, status, rank,dc_id, bio),reply_to_message_id=message.id)
         except Exception as e:
              await message.reply_text(str(e))
    
     elif not message.reply_to_message:
         try:
            user_info = await bot.get_chat(user_id)
            user = await bot.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            rank = user.id in (await RANK())
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await bot.download_media(user.photo.big_file_id)
            await bot.send_photo(chat_id,photo=photo, caption=INFO_TEXT.format(
id,name, username, mention,status,rank, dc_id, bio),reply_to_message_id=message.id)
         except Exception as e:
              await message.reply_text(str(e))
     elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          try:
            user_info = await bot.get_chat(user_id)
            user = await bot.get_users(user_id)
            status = await userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            rank = user.id in (await RANK())
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = await bot.download_media(message.reply_to_message.from_user.photo.big_file_id)
            await bot.send_photo(chat_id,photo=photo,caption=INFO_TEXT.format(
id,name, username, mention,status,rank, dc_id, bio),reply_to_message_id=message.id)
          except Exception as e:
              await message.reply_text(str(e))
