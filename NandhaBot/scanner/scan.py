import config


from pyrogram import filters
from NandhaBot import bot
from NandhaBot.helpers.scansdb import (
get_scan_users, add_scan_user, get_scan_user,
 is_scan_user, remove_scan_user
)

from NandhaBot.rank import RANK_USERS


SCAN_TEXT = """
which date this 
scan process: {}

scanned user: {}
reason: {}

some telegraph 
links for proof:
{}
"""

@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      msg = await message.reply_text("`scanning....`")
      if not message.from_user.id in (await RANK_USERS()):
          return await msg.edit("`you don't have enough rights to use me.`")
      elif len(message.command) <2:
          return await msg.edit("`you need to use correct `/formatting` for scanning someone else.`")
      elif reply:
         try:
            user_id = int(reply.from_user.id)
            reason = message.text.split("-r")[1].split("-p")[0]
            proof = message.text.split("-p")[1]
            mention = f"[{user_id}](tg://user?id={user_id})"
            date = message.date
            if (await is_scan_user(user_id)) == True:
                  await remove_scan_user(user_id)
                  await add_scan_user(user_id, reason, proof)
                  await bot.send_message(config.GROUP_ID, text=SCAN_TEXT.format(date, mention, reason, proof))
                  await msg.edit("`the user already scanned I have updated the details!`")
            else:
                await add_scan_user(user_id,reason,proof)
                await bot.send_message(config.LOG_GROUP_ID, text=SCAN_TEXT.format(date, mention, reason, proof))
                await msg.edit("`the user successfully scanned!`")
         except Exception as e:
             await msg.edit(str(e))
      elif not reply:
            try:
               user_id = int(message.text.split("-u")[1].split("-r")[0])
               reason = message.text.split("-r")[1].split("-p")[0]
               proof = message.text.split("-p")[1]
               mention = f"[{user_id}](tg://user?id={user_id})"
               date = message.date
               if (await is_scan_user(user_id)) == True:
                  await remove_scan_user(user_id)
                  await add_scan_user(user_id, reason, proof)
                  await bot.send_message(config.GROUP_ID, text=SCAN_TEXT.format(date, mention, reason, proof))
                  await msg.edit("`the user already scanned I have updated the details!`")
               else:
                  await add_scan_user(user_id,reason,proof)
                  await bot.send_message(config.LOG_GROUP_ID, text=SCAN_TEXT.format(date, mention, reason, proof))  
                  await msg.edit("`the user successfully scanned!`")            
            except Exception as e:
               await msg.edit(str(e))


         
         
