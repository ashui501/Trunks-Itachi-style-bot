import config


from pyrogram import filters
from NandhaBot import bot
from NandhaBot.helpers.scansdb (
get_scan_users, add_scan_user, get_scan_details,
 is_scan_user, remove_scan_user
)
from NandhaBot.rank import RANK_USERS

SCAN_TEXT = """
the user: {}

details:

the reason why were scan: 
{}

the proof for screenshots:
{}
"""

@bot.on_message(filters.command("scan",config.COMMANDS))
async def scan(_, message):
      reply = message.reply_to_message
      msg = await message.reply_text("`scanning....`")
      if not message.from_user.id in (await RANK_USERS()):
          return await msg.edit("`you don't enough rights to use me.`")
      elif reply or not reply and len(message.text) <2:
          return msg.edit("`you need to use correct /formatting scanning someone else.`")
      elif reply:
         try:
            user_id = reply.from_user.id
            reason = message.text.split("-r")[1].split("-tm")[0]
            proof = message.text.split("-p")[1]
            if user_id in (await is_scan_user(user_id)) == True:
               await msg.edit("`your trying to scan someone but that user already scanned.`")
            else:
                await add_scan_user(user_id,reason,proof)
                await msg.edit("the user successfully 𝗦𝗖𝗔𝗡𝗡𝗘𝗗!")
                await bot.send_message(config.GROUP_ID, text=SCAN_TEXT.format(reply.from_user.mention, reason, proof))




         
         
