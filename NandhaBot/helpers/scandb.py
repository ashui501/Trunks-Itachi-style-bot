from NandhaBot import pymongodb

scandb = pymongodb.SCANNEDDB



async def add_scan_user_details(user_id: str, reason, proof):
          details = {"user_id": (user_id),
                     "reason": reason,
                     "proof": proof}
          return scandb.insert_one({user_id: details})


async def get_scan_user_details(user_id: str):
    user = await scandb.find_one({"user_id":  user_id})
    if user:
        return user[user_id]
