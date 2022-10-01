import config
import time
import io

from NandhaBot.rank import (
RANK_A_USER as a,
RANK_B_USER as b,
RANK_C_USER as c )

from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot
from NandhaBot.helpers.tools import get_readable_time

StartTime = time.time()

@bot.on_message(filters.command("ping",config.COMMANDS))
def ping(_, message):
   if message.from_user.id in a or b or c:
      start_time = time.time()
      end_time = time.time()
      ping_time = round((end_time - start_time) * 1000, 3)
      uptime = get_readable_time((time.time() - StartTime))
      msg = message.reply_text("processing...")
      msg.edit_text(f"**PONG**: `{ping_time}`\n**UPTIME**: `{uptime}`")
   else:
        message.reply_text("Only Rank User Can Acces")


@bot.on_message(filters.command("msginfo",config.COMMANDS))
def messageinfo(_, message):
     if message.reply_to_message:
        try:
          message.reply_text(message.reply_to_message)
        except Exception as e:
           with io.BytesIO(str.encode(str(message.reply_to_message))) as file:
               file.name = "msg.text"
               message.reply_document(
                document=file, caption=e)
     else:
        message.reply_text(message)
