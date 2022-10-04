import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot


INFO_TEXT = """
**here the user information:**

his/her ID: {}
his/her name: {}
his/her username: @{}
his/her mention: {}

his/her DC ID: {}
his/her bio: {}


"""
@bot.on_message(filters.command(["info","userinfo"],config.COMMANDS))
def userinfo(_, message):
    
     chat_id = message.chat.id
     user = message.from_user
     user_id = message.from_user.id
     if not message.reply_to_message:
         user_id = int(message.text.split(None, 1)[1])
         try:
            user_info = bot.get_chat(user_id)
            id = user_info.id
            dc_id = user_info.dc_id
            name = user_info.first_name
            username = user_info.username
            mention = user.mention
            bio = user_info.bio
            message.reply_text(INFO_TEXT.format(
id,name, username, mention, dc_id, bio))
         except Exception as e:
              message.reply_text(str(e))
          
