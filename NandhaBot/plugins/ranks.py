import os
import io
import traceback
import sys
import config

from contextlib import redirect_stdout
from requests import post
from subprocess import getoutput as run
from NandhaBot import bot
from pyrogram.types import *
from pyrogram import filters
from NandhaBot import rank
from NandhaBot.rank import RANK_USERS
from NandhaBot.helpers.paste import batbin
from NandhaBot.helpers.ranksdb import (
get_rankusers, add_rank , remove_rank)

RANK_ADDED_TEXT = """
new rank user arrived on bot
it's {}
"""
RANK_REMOVED_TEXT = """
the rank user remove on bot
it's {}
"""

@bot.on_message(filters.command("addrank"))
async def addrank(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing adding..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("my rank user can add another rank user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if user.id in (await RANK_USERS()):
               await msg.edit("`your trying add someone that person already a rank user`")
           else:
              await add_rank(user.id)
              await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if user.id in (await RANK_USERS()):
                   await msg.edit("`your trying add someone that person already a rank user`")
              else:
                 await add_rank(user.id)
                 await msg.edit_text(RANK_ADDED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))

@bot.on_message(filters.command("removerank"))
async def removerank(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      msg = await message.reply_text("processing removeing..")
      if not message.from_user.id in (await RANK_USERS()):
           await msg.edit_text("my rank user can remove another rank user!")
      elif not reply:
         try:
           user_id_text = int(message.text.split(" ")[1])
           user = await bot.get_users(user_id_text)
           if not user.id in (await RANK_USERS()):
               await msg.edit("`your trying remove someone that person is not a rank user`")
           else:
              await remove_rank(user.id)
              await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
         except Exception as e:
             await msg.edit_text(str(e))
         
      else:
            try:
              user_id = reply.from_user.id
              user = await bot.get_users(user_id)
              if not user.id in (await RANK_USERS()):
                   await msg.edit("`your trying remove someone that person is not a rank user`")
              else:
                 await remove_rank(user.id)
                 await msg.edit_text(RANK_REMOVED_TEXT.format(user.mention))
            except Exception as e:
                  await msg.edit_text(str(e))


@bot.on_message(filters.command("rankusers"))
async def rankuser(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       msg = await message.reply_text("`getting rankusers list!`")
       if not user_id in (await RANK_USERS()):
            await msg.edit_text("`sorry you can't collect rankusers list.`")
       elif user_id in (await RANK_USERS()):
           RANK_USER_TEXT = "𝗥𝗔𝗡𝗞𝗨𝗦𝗘𝗥 𝗟𝗜𝗦𝗧:\n\n"
           try:
              for rankuser in (await get_rankusers()):
                   mention = (await bot.get_users(rankuser)).mention
                   RANK_USER_TEXT += f"• {mention}\n"
                   await msg.edit(RANK_USER_TEXT)
           except Exception as e:
                  await msg.edit(str(e))
              
@bot.on_message(filters.command("sh",config.COMMANDS))
def sh(_, m):
    if m.from_user.id in rank.RANK_A_USER:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        msg = m.reply(
            f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
        if len(m.command) <2:
           msg.edit_text("`Give A Code Run`")    
    else:
        m.reply("only Rank User can access this command!")
            
@bot.on_message(filters.user(rank.RANK_A_USER) & filters.command("eval",config.COMMANDS))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    if len(message.command) <2:
        return await status_message.edit("`GIVE CODE TO RUN..`")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@bot.on_message(filters.command("logs",config.COMMANDS) & filters.user(rank.RANK_USERS))
async def logs(_, message):
    system = run("tail logs.txt")
    link = await batbin(system)
    msg= await message.reply_text("`sending logs...`")
    await message.reply_document(document="logs.txt",caption=f"here the [paste]({link})")
    await msg.delete()

 


@bot.on_message(filters.command("leave",config.COMMANDS) & filters.user(rank.RANK_USERS))
async def leave_chat(_, message):
     if len(message.command) <2:
         return await message.reply_text("Give Me ChatID.")
     chat_id = message.text.split(None,1)[1]
     await bot.send_message(chat_id, "I'm gonna leaves here because my rank user request me!")
     try:
       chat = (await bot.get_chat(chat_id))
       await bot.leave_chat(chat.id)
       
       await message.reply_text(f"Successfully left from {chat.title}")
     except Exception as e:
        return await message.reply_text(str(e))
     
    
    
    
                             


