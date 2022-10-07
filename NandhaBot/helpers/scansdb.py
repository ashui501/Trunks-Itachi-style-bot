from NandhaBot import pymongodb

scandb = pymongodb.SCANSDBS



async def add_scan_user_details(user_id: str, reason):
          scan_reason_list = { "user_id": user_id, "reason": reason}
          x = scandb.insert_one(scan_reason_list)
          id = x.inserted_id
          return id
        
