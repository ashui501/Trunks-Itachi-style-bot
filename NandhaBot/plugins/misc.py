import config
import time

from NandhaBot.rank import (
RANK_A_USER as a,
RANK_B_USER as b,
RANK_C_USER as c )

from pyrogram import filter
from pyrogram.types import *
from NandhaBot import bot

@bot.on_message(filters.command("ping",config.COMMANDS))
def ping(_, message):
   if message.from_user.id in a or b or c:
      start_time = time.time()
      end_time = time.time()
      ping_time = round((end_time - start_time) * 1000, 3)
      msg = message.reply_text("processing...")
      msg.edit_text(f"**PONG**: `{ping_time}`")
      
