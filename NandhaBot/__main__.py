import importlib
import time
from NandhaBot.plugins import ALL_MODULES
from NandhaBot import bot
from NandhaBot.utils.misc import paginate_modules
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import re

BOT_NAME = "TrunksRobot"

HELPABLE = {}

def get_helps():
    global HELPABLE
    for module in ALL_MODULES:
        imported_module = importlib.import_module("Mio.plugins." + module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module

get_helps()


async def help_parser(name, keyboard=None):
  if not keyboard:
    keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return ("**Hey There {}**, `I'm {} A Sweet And Cheerful Bot`\n`I Have A Lots Of Fun And Helpfull Features`\n\n`All Features/Commands Can Be Used With` `mio` `or` `Mio` `Prefix`\n\n**For Any Queries Contact Us At On @Jjk_Tech**".format(name, BOT_NAME), keyboard)



@bot.on_message(get_command("help"))
async def _help(_, message):
  text, keyboard = await help_parser(message.from_user.first_name)
  return await message.reply_photo(
      photo="https://telegra.ph/file/1048492109861f51e6a99.jpg",
      caption=text,
      reply_markup=keyboard
    )


@bot.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, query):
  text, keyboard = await help_parser(query.from_user.first_name)
  await query.message.edit_media(
    media=InputMediaPhoto(
      "https://telegra.ph/file/1048492109861f51e6a99.jpg",
      caption=text
    ),
    reply_markup=keyboard
  )
  return await bot.answer_callback_query(query.id)




@bot.on_callback_query(filters.regex("aboutmio"))
async def about_callnack(_, query):
  cap = "**Hey There, I'm Up Since:** `{}` \n`This Is Some Info About Me (◡ ω ◡)`".format(get_readable_time(time.time() - START_TIME))
  keyboard= InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton(
          text="SUPPORT",
          url="https://t.me/Jjk_Tech"
        )
      ],
      [
        InlineKeyboardButton(
          text="Ryu Senpai",
          user_id=5544740697
        ),
        InlineKeyboardButton(
          text="Cursed Aura",
          user_id=5365575465
        )
      ],
      [
        InlineKeyboardButton(
          text="𝗔𝗮𝘀𝗳𝗖𝘆𝗯𝗲𝗿𝗞𝗶𝗻𝗴",
          user_id=5446914371
        )
      ],
      [
        InlineKeyboardButton(
          text="Back",
          callback_data="help_home(1.0)"
        )
      ]
    ]
  )
  await query.message.edit_caption(caption=cap, reply_markup=keyboard)
  return await bot.answer_callback_query(query.id)


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
  home_match = re.match(r"help_home\((.+?)\)", query.data)
  mod_match = re.match(r"help_module\((.+?)\)", query.data)
  prev_match = re.match(r"help_prev\((.+?)\)", query.data)
  next_match = re.match(r"help_next\((.+?)\)", query.data)
  back_match = re.match(r"help_back", query.data)
  create_match = re.match(r"help_create", query.data)
  top_text = "**Hey There {}**, `I'm {} A Sweet And Cheerful Bot`\n`I Have A Lots Of Fun And Helpfull Features`\n\n`All Features/Commands Can Be Used With` `mio` `or` `Mio` `Prefix`\n\n**For Any Queries Contact Us At On @Jjk_Tech**".format(query.from_user.first_name, BOT_NAME)
  if mod_match:
    module = (mod_match.group(1)).replace(" ", "_")
    text = (
        "**{}** `{}`:\n".format(
          "Here Is The Help For The", HELPABLE[module].__MODULE__
        )
        + HELPABLE[module].__HELP__
    )

    await query.message.edit_caption(
      caption=text,
      reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("back", callback_data="help_back")]]
      )
    )
  elif home_match:
    await query.message.edit_media(
      media=InputMediaPhoto(PM_MIO_PIC, caption=PM_MIO_TEXT),
      reply_markup=START_KEYBOARD
    )
  elif prev_match:
    curr_page = int(prev_match.group(1))
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(curr_page - 1, HELPABLE, "help")
      )
    )

  elif next_match:
    next_page = int(next_match.group(1))
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(next_page + 1, HELPABLE, "help")
      )
    )

  elif back_match:
    await query.message.edit_caption(
      caption=top_text,
      reply_markup=InlineKeyboardMarkup(
        paginate_modules(0, HELPABLE, "help")
      )
    )

  elif create_match:
    text, keyboard = await help_parser(query.from_user.first_name)
    await query.message.edit_caption(
      caption=text,
      reply_markup=keyboard
    )

  return await bot.answer_callback_query(query.id)
