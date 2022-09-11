import wikipedia
import config
from pyrogram import filters
from NandhaBot import bot
from pyrogram.enums import ParseMode

@bot.on_message(filters.command("wiki",config.COMMANDS))
async def wikipediasearch(_, message):
    reply = message.reply_to_message
    if len(message.command) < 2:
          await message.reply_text("example:\n`/wiki telegram`")
          return 
    query =  message.text.split(None, 1)[1] 
    if not query:
        await message.reply_text("Invalid Syntax see help menu to know how to use this command")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"> [{s}]({url}) \n"
        except BaseException:
            pass
    await message.reply_text(
        "**WikiPedia Search: {}** \n\n**Result:** \n\n{}".format(query, result), disable_web_page_preview=True)
                                 
      
