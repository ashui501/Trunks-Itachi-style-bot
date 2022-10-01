import aiofiles
import os
from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot
from NandhaBot.helpers.utils.http import post as send

@bot.on_message(filters.command("paste"))
async def paste(_, message):
  try:
     reply = message.reply_to_message
     BASE = "https://batbin.me/"
     if not message.reply_to_message:
          return await message.reply_text("<b> Reply to Document</b>\n<b>OR Message </b>")
     elif message.reply_to_message.document:
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
          text = await f.read()
        os.remove(doc)
        resp = await send(f"{BASE}api/v2/paste", data=text)
        code = resp["message"]
        batbin_link = f"{BASE}{code}"
        await message.reply_photo(photo=batbin_link,caption=batbin_link,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="LINK", url=batbin_link)]]))
        
     elif reply.text or reply.caption:
        text = reply.text or reply.caption
        resp = await send(f"{BASE}api/v2/paste", data=text)
        code = resp["message"]
        batbin_link = f"{BASE}{code}"
        await message.reply_photo(photo=batbin_link,caption=batbin_link,
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="LINK", url=batbin_link)]]))
        
  except Exception as e:
       await message.reply_text(f"**ERROR**: {e}")
