from NandhaBot import pymongodb

chatsdb = pymongodb.GROUPSDB




async def get_chats():
    chats_list = []
    for chats in groupsdb.find():
        chats_list.append(chats["chat_id"])
    return chats_list

async def add_chats(chat_id: int):
     if not chat_id in (await get_chats()):
           return chatsdb.insert_one({"chat_id": chat_id})


