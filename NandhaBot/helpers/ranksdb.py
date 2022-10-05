from NandhaBot import mongodb

ranksdb = mongodb.ranksdb


async def get_rankusers(user_id: int):
    rank_users = await ranksdb.find_one({"user_id": "user_id"})
    if not rank_users:
        return []
    return rank_users["rank_users"]

async def add_rank(user_id: int):
      rank_users = await get_rankusers()
      ranks_users.append(user_id)
      await ranksdb.update_one(
        {"user_id": "user_id"}, {"$set": {"rank_users": rank_users}}, upsert=True)
      return True  

async def remove_rank(user_id: int):
       rank_users = await get_rankusers()
       rank_users.remove(user_id)
       await ranksdb.update_one(
        {"user_id": "user_id"}, {"$set": {"rank_users": rank_users}}, upsert=True)
       return True
