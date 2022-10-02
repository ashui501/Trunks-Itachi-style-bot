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
from NandhaBot.helpers.paste import spacebin

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


@bot.on_message(filters.command("logs",config.COMMANDS) & filters.user(rank.RANK_A_USER))
def logs(_, message):
    system = run("tail logs.txt")
    link = spacebin(system)
    msg= message.reply_text("`sending logs...`")
    message.reply_document(document="logs.txt",caption=f"here the [paste]({link})")
    msg.delete()

 

RANK_USERS = (rank.RANK_A_USER+rank.RANK_B_USER)   
@bot.on_message(filters.command("leave"))
async def leave_chat(_, message):
     if not message.from_user.id in RANK_USER:
          await message.reply_text("Only Rank User Can Acces.")
     elif len(message.command) <2:
         return await message.reply_text("Give Me ChatID.")
     chat_id = message.text.replace("/leave", "")
     try:
       await bot.leave_chat(chat_id)
     except Exception as e:
        return await message.reply_text(str(e))
     
    
    
    
                             


