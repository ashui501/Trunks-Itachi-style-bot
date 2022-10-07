from NandhaBot import mongodb

chatsdb = mongodb.groupsdb

async def is_chats(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def get_chats() -> list:
    chats_list = []
    async for chat in chatssdb.find({"chat_id": {"$gt": 0}}):
        chats_list.append(chat)
    return chats_list

async def add_chats(chat_id: int):
    is_already_in_chatdb = await is_chats(chat_id)
    if is_already_in_chatdb:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})
