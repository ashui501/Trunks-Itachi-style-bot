import config

from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters
from NandhaBot import bot




@bot.on_message(filters.command(["admins","adminlist"],config.COMMANDS))
async def admins(_, message):
      chat_id = message.chat.id
      admin_list = f"𝗔𝗗𝗠𝗜𝗡𝗦 in {message.chat.title}\n\n"
      bot_list = "\n𝗕𝗢𝗧𝗦:\n"

      if message.chat.type == ChatType.PRIVATE:
           await message.reply_text("This command work on group only!")
      else:
        async for admin in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
               
               if admin.user.is_bot:
                   bot_list += f"⊗ {admin.user.mention}\n"
               else:
                  admin_list += f"✮ {admin.user.mention}\n"
        await message.reply_text(admin_list+bot_list)


@bot.on_message(filters.command("setphoto"))
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("processing....")
      admin_check = await bot.get_chat_member(chat_id, user_id)
      if not reply:
           await msg.edit("`reply to a photo or document.`")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = reply.download()
                await message.chat.set_photo(photo)
                await message.reply_text("Successfully New Profile Photo insert!\nby {}".format(message.from_user.mention))
             else:
                await msg.edit("`sorry you don't have rights to change group photo.`")
     
          except Exception as e:
              await msg.edit(str(e))
                

