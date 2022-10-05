"Rank Users for Special Access"

from NandhaBot.helpers.ranksdb import get_rankusers




async def RANK_USERS() ->list:
     list = await get_rankusers()
     return list

RANK_A_USER = [1491497760,5696053228]
RANK_B_USER = []
RANK_C_USER = []


RANK_AB_USER = (RANK_A_USER+RANK_B_USER)
