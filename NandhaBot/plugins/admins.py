import config

from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters
from NandhaBot import bot




@bot.on_message(filters.command(["admins","adminlist"],config.COMMANDS))
async def admins(_, message):
      chat_id = message.chat.id
      admin_list = f"𝗔𝗗𝗠𝗜𝗡𝗦 in {message.chat.title}\n\n"
      bot_list = "\n\n𝗕𝗢𝗧𝗦:\n"

      if message.chat.type == ChatType.PRIVATE:
           await message.reply_text("This command work on group only!")
      else:
        async for admin in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
               
               if admin.user.is_bot:
                   bot_list += f"⊗ {admin.user.mention}\n"
               else:
                  admin_list += f"✮ {admin.user.mention}\n"
        await message.reply_text(admin_list+bot_list)
