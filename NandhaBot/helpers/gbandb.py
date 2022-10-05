import config

from NandhaBot import mongodb
collection = mongodb.GBAN

from pyrogram import filters
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
           query.message.edit(UNGBAN_TEXT.format(user.first_name))
         except Exception as e:
             query.message.edit(str(e))
      else:
          query.answer("only rank user can acces!", show_alret=True)
 


