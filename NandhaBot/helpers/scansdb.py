from NandhaBot import pymongodb

scansdb = pymongodb.SCANNER



async def add_scan_user(user_id: int, reason: str, date: int):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason, "date": date}
                 scansdb.insert_one(scan_reason_list)

async def get_scan_user(user_id: int):
         details = scansdb.find_one({"_id": user_id})
         return details


async def update_scan_proof(user_id: int, proof: str, date: str):
       scansdb.update_one({"user_id": user_id}, {"$set":{"proof":proof,"date": date}})

async def update_scan_reason(user_id: int, reason: str, date: str):
       scansdb.update_one({"user_id": user_id}, {"$set":{"reason": reason,"date": date}})

async def get_scan_users():
      list = []
      for user_ids in scansdb.find():
          list.append(user_ids["_id"])
      return list

async def is_scan_user(user_id: int):
      scan_user_list = (await get_scan_users())
      if not user_id in scan_user_list:
           return False
      return True

async def remove_scan_user(user_id: int):
   scan_user = scansdb.find_one({"_id": user_id})
   scansdb.delete_one(scan_user)
