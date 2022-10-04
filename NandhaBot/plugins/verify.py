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
         await bot.restrict_chat_member(message.chat.id, member.id, ChatPermissions(can_send_messages=False))
         key = InlineKeyboardMarkup([[InlineKeyboardButton("I'm a human", callback_data=f"unres:{member.id}")]])
         await message.reply(f"Hello ( {member.mention} ) You are restricted to make sure you are not a robot", reply_markup=key)
         
@bot.on_callback_query(filters.regex("unres"))
async def unres(_, q: CallbackQuery):
   user_id = int(q.data.split(":")[1])
   if not q.from_user.id == user_id:
     await q.answer("This message is not for you", show_alert=True)
   else:
     await q.edit_message_text("Verified successfully You can chat in the group now")
     await bot.restrict_chat_member(q.message.chat.id, user_id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
