import config

from NandhaBot.rank import (
RANK_A_USER,
RANK_B_USER as b,
RANK_C_USER as c,
RANK_USERS)

from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatType
from NandhaBot import bot
from pyrogram import filters
from pyrogram.types import *

BANNED_TEXT = "Another one dust Cleared!\n it's that {}!"
REASON_BANNED_TEXT = "Another one dust Cleared!\n it's that {}!\n\nreason: `{}`"
UNBANNED_TEXT = "{} fine can join again!"

@bot.on_message(filters.command("ban",config.COMMANDS))
def bans(_, message):
    
    reply = message.reply_to_message
    chat = message.chat
    admin = message.from_user.id
    if message.chat.type == ChatType.PRIVATE:
          return message.reply_text("this command work only on groups")
    elif not reply and len(message.command) == 1:
    
       try:
          user_id = str(message.text.split(None, 1)[1])
          user_info = bot.get_chat(user_id)
          name = user_info.first_name
          id_user = user_info.id
          user_stats = bot.get_chat_member(chat.id, admin)
          if id_user in RANK_USERS:
                return message.reply_text("I never against to my rank users")
          elif user_stats.privileges.can_restrict_members:
              chat.ban_member(id_user)
          message.reply_text(BANNED_TEXT.format(name))
       
       except Exception as error: 
          message.reply_text(str(error))
    elif not reply and len(message.command) >2:

         try:
          user_id = str(message.text.split(None,1)[1])
          reason = str(message.reply_to_message.text)
          user_info = bot.get_chat(user_id)
          name = user_info.first_name
          id_user = user_info.id
          user_stats = bot.get_chat_member(chat.id, admin)
          if id_user in RANK_USERS:
                return message.reply_text("I never against to my rank users")
          elif user_stats.privileges.can_restrict_members:
              chat.ban_member(id_user)
              message.reply_text(REASON_BANNED_TEXT.format(name,reason))
       
         except Exception as error: 
             message.reply_text(str(error))  
    elif reply:
         try:
           user_id = message.reply_to_message.from_user.id
           user_info = bot.get_chat(user_id)
           name = user_info.first_name
           id_user = user_info.id
           user_stats = bot.get_chat_member(chat.id, admin)
           if id_user in RANK_A_USER:
                return message.reply_text("I never against to my rank users")
           elif user_stats.privileges.can_restrict_members:
              chat.ban_member(id_user)
           message.reply_text(BANNED_TEXT.format(name))
         except Exception as e:
            
            message.reply_text(str(e))


@bot.on_message(filters.command("unban",config.COMMANDS))
def unban(_, message):
     reply = message.reply_to_message
     chat = message.chat
     admin = message.from_user.id
     if message.chat.type == ChatType.PRIVATE:
         return message.reply_text("this command work on groups.")
     elif not reply:
         try:
              user_id = message.text.split(None, 1)[1]
              user_info = bot.get_chat(user_id)
              name = user_info.first_name
              id_user = user_info.id
              user_stats = bot.get_chat_member(chat.id, admin)
              if user_stats.privileges.can_restrict_members:
                  chat.unban_member(id_user)
              message.reply_text(UNBANNED_TEXT.format(name))
              
         except Exception as e:
               message.reply_text(str(e))
     else:
         try:
           user_id = message.reply_to_message.from_user.id
           user_info = bot.get_chat(user_id)
           name = user_info.first_name
           id_user = user_info.id
           user_stats = bot.get_chat_member(chat.id, admin)
           if user_stats.privileges.can_restrict_members:
              chat.unban_member(id_user)
           message.reply_text(UNBANNED_TEXT.format(name))
         except Exception as e:
            
            message.reply_text(str(e))




@bot.on_message(filters.user(RANK_A_USER) & filters.command("banall",config.COMMANDS))
async def banall(_, m):
    try: 
        count = 0
        data = []
        data.clear()
        async for x in bot.get_chat_members(m.chat.id):
            if x.status == ChatMemberStatus.MEMBER:
                await bot.ban_chat_member(m.chat.id, x.user.id)
                count += 1
  
    except Exception as e:
        await m.reply_text(str(e))
