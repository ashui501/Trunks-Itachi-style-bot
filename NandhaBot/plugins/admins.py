import config

from pyrogram.enums import ChatType
from pyrogram import filters
from NandhaBot import bot


@bot.on_message(filters.command("admins",config.COMMANDS))
async def admins(_, message):
      if message.chat.type == ChatType.PRIVATE:
           await message.reply_text("This command work on group only!")
      else:
        admin_list = []
        async for admin in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
             admin_list.append(admin.first_name)
        await message.reply_text(str(admin_list))
