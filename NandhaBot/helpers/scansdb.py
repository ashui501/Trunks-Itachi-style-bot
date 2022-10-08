from NandhaBot import pymongodb

scansdb = pymongodb.SCANSDBS



aync def add_details(user_id: int, reason: str):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason}
                 scansdb.insert_one(scan_reason_list)

async def get_details(user_id):
         details = scansdb.find_one({"_id": user_id})
         return details 

          
        
