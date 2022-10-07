from NandhaBot import pymongodb

scandb = pymongodb.SCANDB



async def add_scan_user_details(user_id, reason, proof):
          details = {"user_id": user_id,
                     "reason": reason,
                     "proof": proof}
          return details.insert_one({"{user_id}": details})

