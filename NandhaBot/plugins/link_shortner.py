import pyshorteners
import config

from NandhaBot import bot
from pyrogram import filters


@bot.on_message(filters.command("short",config.COMMANDS))
async def short(_, message):
    if len(message.command) <2:
         return await message.reply_text("Give Some URL to Short")
    link = message.text.replace("/short", "")
    msg = await message.reply_text("processing...")
    try:
        search = pyshorteners.Shortener()
        short_url = search.tinyurl.short(link)
        await msg.edit_text(f"Shortlink: {short_url}")
    except Exception as e:
        await msg.edit_text(str(e))
