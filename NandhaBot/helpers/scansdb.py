from NandhaBot import pymongodb

scansdb = pymongodb.SCANSDBS



async def add_details(user_id: int, reason: str, proof: str):
                 scan_reason_list = {"_id": user_id, "user_id": user_id, "reason": reason, "proof": proof}
                 scansdb.insert_one(scan_reason_list)

async def get_details(user_id: int):
         details = scansdb.find_one({"_id": user_id})
         return details
         

async def update_update(user_id: int, reason: str, proof: str):
        old_details = await get_details(user_id)
        new_details = { user_id: { user_id, "user_id": user_id, "reason": reason, "proof": proof}}
        scansdb.update_one(old_details, new_details)
        return "`Successfully Updated Details.`"
