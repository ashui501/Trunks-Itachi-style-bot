import requests
from NandhaBot import bot

@bot.on_message(filters.command("logo"))
def logo(_, message):
    if len(message.command) <2:
       return message.reply_text("Give Me logo name.")
    logo_name = message.text.replace("/logo","")
    msg = message.reply_text("logo generating...")
    try:
       API = f"https://api.sdbots.tk/anime-logo?name={logo_name}"
       req = requests.get(API).url
       bot.send_photo(
            message.chat.id,
            photo=req,
            caption="here the telegraph link: {req} Successfully Generated by Trunks",
            reply_to_message_id=message.id)
    except Exception as e:
        msg.edit_text(str(e))
  
     
