from pyrogram import Client, filters
from pyrogram.types import (
InlineKeyboardMarkup,
InlineKeyboardButton,
CallbackQuery,
ChatPermissions
)

from NandhaBot import bot

@bot.on_message(filters.new_chat_members)
async def res(client, message):
     for member in message.new_chat_members:
        try:
           await bot.restrict_chat_member(message.chat.id, member.id, ChatPermissions(can_send_messages=False))
           key = InlineKeyboardMarkup([[InlineKeyboardButton("I'm a human", callback_data=f"unres:{member.id}")]])
           await message.reply(f"Hello ( {member.mention} ) You are restricted to make sure you are not a robot", reply_markup=key)
        except Exception as e:
           message.reply_text(str(e))

@bot.on_callback_query(filters.regex("unres"))
async def unres(_, query):
   user_id = int(query.data.split(":")[1])
   if not query.from_user.id == user_id:
     await query.answer("This message is not for you!", show_alert=True)
   else:
     try:
       name = (await bot.get_users(user_id)).first_name
       await query.edit_message_text(f"Verified successfully {name} can chat in the group now!")
       await bot.restrict_chat_member(query.message.chat.id, user_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
     except Exception as e:
          query.message.edit_message_text(str(e))
