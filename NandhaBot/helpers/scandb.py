from NandhaBot import pymongodb

scandb = pymongodb.SCANDB



async def add_scan_user_details(user_id, reason, proof):
          details = {"user_id": user_id,
                     "reason": reason,
                     "proof": proof}
          return scandb.insert_one({user_id: details})

async def get_scan_user_details(user_id):
         user_details = []
         for scan_user in scandb.find():
              return user_details.append(scan_user[f"{user_id}"])
         return user_details
