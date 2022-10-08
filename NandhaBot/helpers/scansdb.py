from NandhaBot import pymongodb

scansdb = pymongodb.SCANSDBS




async def add_details(user_id, reason: str):
          scan_reason_list = {"user_id": user_id, "reason": reason}
          scansdb.insert_one(scan_reason_list)

async def get_details(user_id):
         details = await scansdb.find_one({"user_id": user_id})
         return details 

          
        
