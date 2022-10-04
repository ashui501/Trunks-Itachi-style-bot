import config

from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters
from NandhaBot import bot


@bot.on_message(filters.command("admins",config.COMMANDS))
async def admins(_, message):
      chat_id = message.chat.id
      if message.chat.type == ChatType.PRIVATE:
           await message.reply_text("This command work on group only!")
      else:
        admin_list = "here the total admins:\n"
        async for admin in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                   admin_list += f"{admin.user.mention}\n"
        await message.reply_text(admin_list)
