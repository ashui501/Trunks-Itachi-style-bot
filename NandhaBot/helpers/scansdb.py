from NandhaBot import pymongodb

scansdb = pymongodb.SCANSDBS



async def add_details(user_id: int, reason: str, proof: str):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason, "proof": proof}
                 scansdb.insert_one(scan_reason_list)

async def get_details(user_id: int):
         details = scansdb.find_one({"_id": user_id})
         _id = details["_id"]
         user_id = _id["user_id"]
         reason = ["reason"]
         proof = ["proof"]
         return f"userID: {user_id}\nreason: {reason}\n\n proof: {proof}"

          
        
