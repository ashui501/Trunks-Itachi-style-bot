import wikipedia
import config
from pyrogram import filters
from NandhaBot import bot
from pyrogram.enums import ParseMode


@bot.on_message(filters.command("wiki",config.COMMANDS))
async def wikisearch(_, message):
      if len(message.command) < 2:
          return await message.reply_text("example:\n`/wiki telegram`")
      query = message.text.split(None, 1)[1]
      if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    ) 
      msg = await message.reply_text("**Searching in Wikipedia...**")                          
      results = wikipedia.search(query)
      result = ""
      
      for s in results:
            page = wikipedia.page(s)
            url = page.url
            result += f"> [{s}]({url}) \n"
      await msg.edit_text(
         "**WikiPedia Search: {}** \n\n**Search Result:** \n\n{}".format(query, result),parse_mode=ParseMode.MARKDOWN ,disable_web_page_preview=True)  
                                 
      
