"credits to @NandhaxD"

import config

from pyrogram import filters
from pyrogram import enums
from NandhaBot import bot

pinned_text = """
**Chat:** {}
**Admin:** {}

**Pinned:** **[message]({})**
"""

@bot.on_message(filters.command("pin",config.COMMANDS))
def pin(_, message):
      chat = message.chat
      chat_title = message.chat.title
      chat_id = message.chat.id
      user_id = message.from_user.id
      first_name = message.from_user.first_name
      
      if message.chat.type == enums.ChatType.PRIVATE:
            return message.reply_text("work only on groups!")
    
      user_stats = bot.get_chat_member(chat_id, user_id)
      if user_stats.privileges.can_pin_messages and not message.reply_to_message:
         
          try:
            message_id = int(message.text.split(None,1)[1])
            msg = bot.pin_chat_message(chat_id, message_id)
            message.reply_text(pinned_text.format(chat_title,first_name,msg.link),disable_web_page_preview=True)
          except Exception as e:
                 return message.reply_text(str(e))

      else:
          try:
            if user_stats.privileges.can_pin_messages and message.reply_to_message:
               message.reply_to_message.pin()
               message.reply_text(pinned_text.format(chat_title,first_name, message.reply_to_message.link), disable_web_page_preview=True)
          except Exception as e:
                return message.reply_text(str(e))
