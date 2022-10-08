from NandhaBot import pymongodb

scansdb = pymongodb.SCANNER



async def add_scan_user(user_id: int, reason: str):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason, "proof: "something"}
                 scansdb.insert_one(scan_reason_list)

async def get_scan_user(user_id: int):
         details = scansdb.find_one({"_id": user_id})
         return details

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
