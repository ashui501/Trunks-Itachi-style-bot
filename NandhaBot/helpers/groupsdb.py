from NandhaBot import pymongodb

chatsdb = pymongodb.CHATSDB




async def get_chats():
    chats_list = []
    for chats in chatsdb.find():
        chats_list.append(chats["chat_id"])
    return chats_list

async def add_chats(chat_id: int):
     if not chat_id in (await get_chats()):
           return chatsdb.insert_one({"chat_id": chat_id})


async def is_chats(chat_id: int):
     if chat_id in (await get_chats()):
          return True
     return False
