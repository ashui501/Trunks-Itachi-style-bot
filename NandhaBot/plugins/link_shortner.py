from NandhaBot import aiohttpsession, bot
from pyrogram import filters

API_KEY = "d74c43163dfe65f0bcc7538d952c448f66a65404&"


async def get_shortlink(link):
    url = 'https://playdisk.xyz/api?api='
    params = {'api': API_KEY, 'url': link}

    async with aiohttpsession as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


@bot.on_message(filters.command("short"))
async def short(_, message):
    if len(message.command) <2:
         return await message.reply_text("Give Some URL to Short")
    link = await message.text.replace("/short", "")
    msg = await message.reply_text("processing...")
    try:
        short_link = await get_shortlink(link)
        await msg.edit_text(f"Shortlink: {short_link}")
    except Exception as e:
        await msg.edit_text(str(e))
