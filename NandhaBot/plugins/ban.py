import config

from pyrogram.enums ChatType
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *

BANNED_TEXT = "Another one dust Cleared {}!"

@bot.on_message(filters.command("ban",config.COMMANDS))
def bans(_, message):
    
    reply = message.reply_to_message
    chat = message.chat
    admin = message.from_user.id
    if message.chat.type == ChatType.PRIVATE:
          return message.reply_text("this command work only on groups")
    elif not reply:
    
       try:
          user_id = message.text.replace("/ban", "")
          user_info = bot.get_chat(user_id)
          name = user_info.first_name
          id_user = user_info.id
          user_stats = bot.get_chat_member(chat.id, admin)
          if user_stats.privileges.can_restrict_members:
              chat.ban_member(id_user)
          message.reply_text(BANNED_TEXT.format(name))
       except Exception as error: 
          
          message.reply_text(str(error))
    else:
         try:
           user_id = message.reply_to_message.from_user.id
           user_info = bot.get_chat(user_id)
           name = user_info.first_name
           id_user = user_info.id
           user_stats = bot.get_chat_member(chat.id, admin)
           if user_stats.privileges.can_restrict_members:
              chat.ban_member(id_user)
           message.reply_text(BANNED_TEXT.format(name))
         except Exception as e:
            
            message.reply_text(str(e))
