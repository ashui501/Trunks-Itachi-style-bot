import config
import play_scraper

from pyrogram import filters
from pyrogram.types import *
from NandhaBot import bot

@bot.on_message(filters.command(["ps","playstore"],config.COMMANDS))
def playstore(_, message):
    if len(message.command) <2:
         return message.reply_text("Give App Name.")
    app_name = message.text.split(None,1)[1]
    results = play_scraper.search(app_name)
    for result in results:
        details = "**Title:** `{}`".format(result["title"]) + "\n" \
        "**Description:** `{}`".format(result["description"]) + "\n" \
        "**App ID:** `{}`".format(result["app_id"]) + "\n" \
        "**Developer:** `{}`".format(result["developer"]) + "\n" \
        "**Developer ID:** `{}`".format(result["developer_id"]) + "\n" \
        "**Score:** `{}`".format(result["score"]) + "\n" \
        "**Price:** `{}`".format(result["price"]) + "\n" \
        "**Full Price:** `{}`".format(result["full_price"]) + "\n" \
        "**Free:** `{}`".format(result["free"]) + "\n" \
        "\n" + "Made by @TrunksRobot"
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Play Store", url="https://play.google.com"+result["url"])]]
        )
        message.reply_text(text=(details),reply_markup=reply_markup)
          
