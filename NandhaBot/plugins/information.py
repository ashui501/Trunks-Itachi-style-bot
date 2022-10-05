import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot


INFO_TEXT = """
𝗨𝗦𝗘𝗥𝗦𝗧𝗔𝗧𝗨𝗦:

**ID:** `{}`
**Name:** {}
**Username:** @{}
**Mention:** {}

**UserStatus:**\n`{}`
\n**Dc:** {}
**Bio:** {}

`note were sends you necessary information about user not at all`!
"""

def userstatus(user_id):
   try:
      user = bot.get_users(user_id)
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
def userinfo(_, message):
    
     chat_id = message.chat.id
     user_id = message.from_user.id
     if not message.reply_to_message and len(message.command) != 1:
         
         try:
            user_id = str(message.text.split(None, 1)[1])
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            status = userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = bot.download_media(user_info.photo.big_file_id)
            bot.send_photo(photo, caption=INFO_TEXT.format(
id,name, username, mention, status,dc_id, bio),reply_to_message_id=message.id)
         except Exception as e:
              message.reply_text(str(e))
    
     elif not message.reply_to_message and len(message.command) == 1:
         try:
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            status = userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = bot.download_media(user_info.photo.big_file_id)
            bot.send_photo(photo, caption=INFO_TEXT.format(
id,name, username, mention,status, dc_id, bio),reply_to_message_id=message.id)
         except Exception as e:
              message.reply_text(str(e))
     elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          try:
            user_info = bot.get_chat(user_id)
            user = bot.get_users(user_id)
            status = userstatus(user.id)
            id = user_info.id
            dc_id = user.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            photo = bot.download_media(message.reply_to_message.from_user.photo.big_file_id)
            bot.send_photo(photo,caption=INFO_TEXT.format(
id,name, username, mention,status, dc_id, bio),reply_to_message_id=message.id)
          except Exception as e:
              message.reply_text(str(e))
