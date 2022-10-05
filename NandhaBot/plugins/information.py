import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot


INFO_TEXT = """
**here the user information:**

**ID:** `{}`
**Name:** {}
**Username:** @{}
**Mention:** {}

**DC ID:** {}
**Bio:** {}

`note were sends you necessary information about user not at all`!
"""

async def userstatus(user_id):
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
  else:
      return "somthin wrong happen"



@bot.on_message(filters.command(["info","userinfo"],config.COMMANDS))
def userinfo(_, message):
    
     chat_id = message.chat.id
     user_id = message.from_user.id
     if not message.reply_to_message and len(message.command) != 1:
         
         try:
            user_id = str(message.text.split(None, 1)[1])
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            message.reply_text(INFO_TEXT.format(
id,name, username, mention, dc_id, bio))
         except Exception as e:
              message.reply_text(str(e))
    
     elif not message.reply_to_message and len(message.command) == 1:
         try:
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            message.reply_text(INFO_TEXT.format(
id,name, username, mention, dc_id, bio))
         except Exception as e:
              message.reply_text(str(e))
     elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          try:
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            message.reply_text(INFO_TEXT.format(
id,name, username, mention, dc_id, bio))
          except Exception as e:
              message.reply_text(str(e))
