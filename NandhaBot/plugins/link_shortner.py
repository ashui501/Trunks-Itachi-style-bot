from NandhaBot import aiohttpsession, bot
from pyrogram import filters

API_KEY = "d74c43163dfe65f0bcc7538d952c448f66a65404"


async def get_shortlink(link):
    url = 'https://playdisk.xyz/api'
    params = {'api': API_KEY, 'url': link}

    async with aiohttpsession as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]


@bot.on_message(filters.command("short"))
def short(_, message):
    if len(message.command) <2:
         return message.reply_text("Give Some URL to Short")
    link = message.text.replace("/short", "")
    msg = message.reply_text("processing...")
    try:
        short_link = get_shortlink(link)
        msg.edit_text(f"Shortlink: {short_link}")
    except Exception as e:
        message.reply_text(str(e))
