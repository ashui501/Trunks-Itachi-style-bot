import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot

pinned_text = """
chat: {}
admin: {}

pinned: **[msg]({})**
"""

@bot.on_message(filters.commands("pin",config.COMMANDS))
def pin(_, message):
      chat = message.chat
      chat_title = chat.title
      chat_id = chat.id
      user = message.from_user
      user_id = user.id
      first_name = message.from_user.first_name
      user_stats = bot.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
            return message.reply_text("work only on groups!")
      elif user_stats.privileges.can_pin_messages and not message.reply_to_message:
         
          try:
            message_id = message.text.split(None,1)[1]
            msg = bot.pin_chat_message(chat_id, message_id)
            message.reply_text(pinned_text.format(chat_title,user_name,msg.link))
          except Exception as e:
                 return message.reply_text(str(e))

      else:
          try:
            if user_stats.privileges.can_pin_messages and message.reply_to_message:
               message.reply_to_message.pin()
               message.reply_text(pinned_text.format(chat_title,user_name, message.reply_to_message.link))
          except Exception as e:
                return message.reply_text(str(e))
