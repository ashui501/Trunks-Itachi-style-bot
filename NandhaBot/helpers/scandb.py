from NandhaBot import pymongodb

scandb = pymongodb.SCANNEDDB



async def add_scan_user_details(user_id: str, reason, proof):
          details = {"user_id": (user_id),
                     "reason": reason,
                     "proof": proof}
          return scandb.insert_one({user_id: details})


async def get_scan_user_details(user_id: str):
    users_list = []
    for user in scandb.find({user_id: {"$gt": 0}}):
        users_list.append(user)
    return users_list
