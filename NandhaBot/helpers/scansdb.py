from NandhaBot import pymongodb

scansdb = pymongodb.SCANNER



async def add_details(user_id: int, reason: str, proof: str):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason, "proof": proof}
                 scansdb.insert_one(scan_reason_list)

async def get_details(user_id: int):
         details = scansdb.find_one({"_id": user_id})
         return details

async def get_scan_users():
      for user_ids in scansdb.find():
          return [user_ids["_id"]]

async def is_scanned(user_id: int)
      scan_user_list = await get_scan_users()
      if not user_id in scan_user_list:
           return False
      return True
