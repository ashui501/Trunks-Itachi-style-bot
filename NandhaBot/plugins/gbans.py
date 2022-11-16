import config

from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot
from NandhaBot.rank import RANK_USERS


from NandhaBot import mongodb
collection = mongodb.GBAN



async def gban_user(chat):
    doc = {"_id": "Gban", "users": [chat]}
    r = await collection.find_one({"_id": "Gban"})
    if r:
        await collection.update_one({"_id": "Gban"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)

async def get_gbaned_users():
    results = await collection.find_one({"_id": "Gban"})
    if results:
        return results["users"]
    else:
        return []

async def ungban_user(chat):
    await collection.update_one({"_id": "Gban"}, {"$pull": {"users": chat}})


GBAN_TEXT = """
𝗚𝗕𝗔𝗡𝗡𝗘𝗗 𝗨𝗦𝗘𝗥!

`gbanned user {} 
banned in {}`
"""

UNGBAN_TEXT = """
𝗨𝗡𝗚𝗕𝗔𝗡𝗡𝗘𝗗!

`ungbanned user {}
by rank users`
"""


@bot.on_callback_query(filters.regex("ungban"))
async def ungban_btn(_, query):
      user_id = int(query.data.split(":")[1])
      chat_id = query.data.split(":")[2]
      if query.from_user.id in (await RANK_USERS()):
         try:
           await ungban_user(user_id)
           await bot.unban_chat_member(chat_id, user_id)
           user = await bot.get_users(user_id)
           await query.message.edit(UNGBAN_TEXT.format(user.first_name))
         except Exception as e:
             await query.message.edit(str(e))
      else:
          await query.answer("only rank user can acces!", show_alret=True)
 

@bot.on_message(filters.command("gban"))
async def gbans(_, message):
       reply = message.reply_to_message
       user_id = message.from_user.id
       chat_id = message.chat.id
       chat_title = message.chat.title
       msg = await message.reply_text("gbanning a user...")
       if not user_id in (await RANK_USERS()):
          await msg.edit("`rank user required.`")
       elif reply:
           user_id = message.reply_to_message.from_user.id
           if user_id in (await RANK_USERS()):
               await msg.edit("`This person is my rank user`.")
           elif user_id in (await get_gbaned_users()):
                await msg.edit("This user already 𝗚𝗕𝗔𝗡𝗡𝗘𝗗.")
           else:
              try:
                 await gban_user(user_id)
                 await msg.edit("Successfully 𝗚𝗕𝗔𝗡𝗡𝗘𝗗!")
                 await bot.send_message(config.GROUP_ID, text="`the rank user gbanned {}`".format(reply.from_user.mention))
              except Exception as e:
                  await msg.edit(str(e))
       elif not reply and len(message.command) == 2:
              user_id = int(message.text.split(None,1)[1])
              try:
                 user = await bot.get_users(user_id)
              except:
                  await msg.edit("use userID only.")
              user = await bot.get_users(user_id)
              if user.id in (await RANK_USERS()):
                    await msg.edit("This person is my rankuser.")
              elif user.id in (await get_gbaned_users()):
                    await msg.edit("This user already 𝗚𝗕𝗔𝗡𝗡𝗘𝗗.")
              else:
                  try:
                     await gban_user(user.id)
                     await msg.edit("Successfully 𝗚𝗕𝗔𝗡𝗡𝗘𝗗!")
                     await bot.send_message(config.GROUP_ID, text="`the rank user gbanned {}`".format(user.mention))
                  except Exception as e:
                      await msg.edit(str(e))

@Nandha.on_message(filters.group):
async def gbanning(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    bot_id = (await Nandha.get_me()).id
    if user_id in get_gbanned_users():
       check = await message.chat.get_member(bot_id)
       if check.privileges:
             await Nandha.ban_chat_member(chat_id, user_id)
             await message.reply_text("done!")



