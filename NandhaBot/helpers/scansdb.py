from NandhaBot import pymongodb

scandb = pymongodb.SCANSDBS




async def add_details(user_id: int, reason: str):
          scan_reason_list = {"user_id": user_id, "reason": reason}
          scandb.insert_one(scan_reason_list)

async def get_details(user_id: int):
         list = []
         for details in scandb.find_one({"_id": user_id}):
              list.append(details)
         return list

          
        
