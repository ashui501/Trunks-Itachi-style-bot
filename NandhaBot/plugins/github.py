import os
import config
from requests import get
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from NandhaBot import bot


@bot.on_message(filters.command("github",config.COMMANDS))
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("/github name")
    photo_url = "https://telegra.ph/file/464250261a5f8a8aaa8b3.jpg"
    msg = await message.reply_photo(photo_url,"**Result Gathering.....**")
    user = message.text.split(None, 1)[1]
    res = get(f'https://api.github.com/users/{user}').json()
    data = f"""**Name**: {res['name']}
**UserName**: {res['login']}
**Link**: [{res['login']}]({res['html_url']})
**Bio**: {res['bio']}
**Company**: {res['company']}
**Blog**: {res['blog']}
**Location**: {res['location']}
**Public Repos**: {res['public_repos']}
**Followers**: {res['followers']}
**Following**: {res['following']}
**Acc Created**: {res['created_at']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res['avatar_url']).content
        f.write(kek)

    await msg.edit_media(media=InputMediaPhoto(photo=f"{user}.jpg", caption=data))
    os.remove(f"{user}.jpg")
