import config

from NandhaBot import mongodb
collection = mongodb.GBAN

from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot
from NandhaBot.rank import RANK_USERS

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

@bot.on_message(group=200)
async def gbans(_, message):
   chat = message.chat
   chat_id = message.chat.id
   user_id = message.from_user.id
   name = message.from_user.first_name
   if message.from_user.id in (await get_gbaned_users()):
       await chat.ban_member(message.from_user.id)
       await bot.send_message(config.LOG_CHANNEL_ID, text=GBAN_TEXT.format(name,chat.title), 
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝗨𝗡𝗚𝗕𝗔𝗡",callback_data=f"ungban:{user_id}")]]))

@bot.on_callback_query(filters.regex("ungban"))
async def ungban_btn(_, query):
      user_id = int(query.data.split(":")[1])
      if query.from_user.id in (await RANK_USERS()):
         try:
           await ungban_user(user_id)
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
               await msg.edit("`This user already gbanned`.")
           else:
              try:
                 await gban_user(user_id)
                 await msg.edit("Successfully 𝗚𝗕𝗔𝗡𝗡𝗘𝗗!")
                 await bot.send_message(config.GROUP_ID, text=ADD_GBANNED_TEXT = "`the rank user gbanned {}`".format(reply.from_user.first_name), reply_to_message_id=message.id)
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
                    await msg.edit("This user already gabnned.")
              else:
                  try:
                     await gban_user(user.id)
                     await msg.edit("Successfully 𝗚𝗕𝗔𝗡𝗡𝗘𝗗!")
                     await bot.send_message(config.GROUP_ID, text=ADD_GBANNED_TEXT = "`the rank user gbanned {}`".format(user.first_name), reply_to_message_id=message.id)
                  except Exception as e:
                      await msg.edit(str(e))
