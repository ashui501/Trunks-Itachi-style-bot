from requests import post
from NandhaBot.helpers.utils.http import post


def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"

def batbin(text):
      BASE = "https://batbin.me/"
      resp = post(f"{BASE}api/v2/paste", data=text)
      code = resp["message"]
      return f"{BASE}{code}"
