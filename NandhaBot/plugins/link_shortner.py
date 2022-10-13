import pyshorteners
import config

from NandhaBot import bot
from pyrogram import filters


@bot.on_message(filters.command("getlink",config.COMMANDS))
async def short(_, message):
    if message.reply_to_message:
         link = message.reply_to_message.text
    elif not message.reply_to_message:
         link = message.text.split(None, 1)[1]
    msg = await message.reply_text("processing...")
    try:
        search = pyshorteners.Shortener()
        short_url = search.tinyurl.short(link)
        await msg.edit_text(f"**shorteners link**:\n`{short_url}`")
    except Exception as e:
        await msg.edit_text(str(e))
