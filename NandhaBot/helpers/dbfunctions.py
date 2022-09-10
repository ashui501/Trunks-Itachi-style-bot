from NandhaBot import mongodb


usersdb = mongodb.users

async def is_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True

async def get_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list
    
async def add_user(user_id: int):
    is_served = await is_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})   
