import logging
import os
import sys
import shutil
import asyncio
from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
import config
from pyrogram.types import BotCommand
from config import API_HASH, API_ID, OWNER_ID
from PratikBots import CLONE_OWNERS
from PratikBots import PratikBots as app, save_clonebot_owner
from PratikBots import db as mongodb

CLONES = set()
cloneownerdb = mongodb.cloneownerdb
clonebotdb = mongodb.clonebotdb

# Clone Command Handler
@app.on_message(filters.command(["clone", "host", "deploy"]))
async def clone_txt(client, message):
    if len(message.command) <= 1:
        return await message.reply_text(
            "**Provide Bot Token after /clone Command from @Botfather.**\n\n"
            "**Example:** `/clone bot_token_here`"
        )

    bot_token = message.text.split("/clone", 1)[1].strip()
    mi = await message.reply_text("🔄 **Checking bot token... Please wait!**")

    try:
        ai = Client(bot_token, API_ID, API_HASH, bot_token=bot_token, plugins=dict(root="PratikBots/mplugin"))
        await ai.start()
        bot = await ai.get_me()
        bot_id = bot.id
        user_id = message.from_user.id
        
        await save_clonebot_owner(bot_id, user_id)

        await ai.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("clone", "Make your own reaction bot"),
            BotCommand("ping", "Check if the bot is alive or dead"),
            BotCommand("id", "Get user's ID"),
            BotCommand("stats", "Check bot stats"),
            BotCommand("gcast", "Broadcast any message to groups/users"),
        ])

    except (AccessTokenExpired, AccessTokenInvalid):
        return await mi.edit_text("❌ **Invalid bot token. Please provide a valid one.**")

    except Exception:
        cloned_bot = await clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            return await mi.edit_text("**🤖 Your bot is already cloned ✅**")

    await mi.edit_text("**Cloning process started. Please wait for the bot to start.**")

    try:
        details = {
            "bot_id": bot.id,
            "is_bot": True,
            "user_id": user_id,
            "name": bot.first_name,
            "token": bot_token,
            "username": bot.username,
        }
        cloned_bots = clonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)
        total_clones = len(cloned_bots_list)

        await clonebotdb.insert_one(details)
        CLONES.add(bot.id)

        await app.send_message(
            int(OWNER_ID),
            f"**#New_Clone**\n\n"
            f"**Bot:- @{bot.username}**\n\n"
            f"**Details:-**\n{details}\n\n"
            f"**Total Cloned:-** {total_clones}"
        )

        await mi.edit_text(
            f"✅ **Bot @{bot.username} has been successfully cloned and started.**\n\n"
            f"❌ **Remove clone:** `/delclone`\n"
            f"📜 **Check all cloned bots:** `/cloned`"
        )

    except PeerIdInvalid:
        await mi.edit_text(
            f"✅ **Your bot has been successfully cloned!**\n"
            f"🚀 **Start the bot from owner ID before using it.**\n\n"
            f"📜 **Check cloned bots:** `/cloned`"
        )

    except Exception as e:
        logging.exception("Error while cloning bot.")
        await mi.edit_text(
            f"⚠️ <b>Error:</b>\n\n<code>{e}</code>\n\n"
            f"📩 **Forward this message to @ll_ALPHA_BABY_lll for assistance.**"
        )   

@app.on_message(filters.command("cloned"))
async def list_cloned_bots(client, message):
    try:
        cloned_bots = clonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)

        if not cloned_bots_list:
            await message.reply_text("No bots have been cloned yet.")
            return

        total_clones = len(cloned_bots_list)
        text = f"**Total Cloned Bots:** {total_clones}\n\n"
        messages = []  # Store message chunks
        chunk_size = 4000  # Telegram message limit (safe side)

        for bot in cloned_bots_list:
            bot_info = (
                f"**Bot ID:** `{bot['bot_id']}`\n"
                f"**Bot Name:** {bot['name']}\n"
                f"**Bot Username:** @{bot['username']}\n\n"
            )

            if len(text) + len(bot_info) > chunk_size:
                messages.append(text)  # Save current chunk
                text = ""  # Reset for new chunk

            text += bot_info  # Add bot info to current chunk

        if text:
            messages.append(text)  # Add last chunk

        for msg in messages:
            await message.reply_text(msg)

    except Exception as e:
        logging.exception(e)
        await message.reply_text("**An error occurred while listing cloned bots.**")

@app.on_message(
    filters.command(["deletecloned", "delcloned", "delclone", "deleteclone", "removeclone", "cancelclone"])
)
async def delete_cloned_bot(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the bot token after the command.**")
            return

        bot_token = " ".join(message.command[1:])
        ok = await message.reply_text("**Checking the bot token...**")

        cloned_bot = await clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            await clonebotdb.delete_one({"token": bot_token})
            CLONES.remove(cloned_bot["bot_id"])

            await ok.edit_text(
                f"**🤖 your cloned bot has been removed from my database ✅**\n**🔄 Kindly revoke your bot token from @botfather otherwise your bot will stop when @{app.username} will restart ☠️**"
            )
        else:
            await message.reply_text("**Provide Bot Token after /delclone Command from @Botfather.**\n\n**Example:** `/delclone bot token paste here`")
    except Exception as e:
        await message.reply_text(f"**An error occurred while deleting the cloned bot:** {e}")
        logging.exception(e)

async def restart_bots():
    global CLONES
    try:
        logging.info("Restarting all cloned bots...")
        bots = [bot async for bot in clonebotdb.find()]
        
        async def restart_bot(bot):
            bot_token = bot["token"]
            ai = Client(bot_token, API_ID, API_HASH, bot_token=bot_token, plugins=dict(root="PratikBots/mplugin"))
            try:
                await ai.start()
                bot_info = await ai.get_me()
                await ai.set_bot_commands([
                    BotCommand("start", "Start the bot"),
                    BotCommand("clone", "Make your own reaction bot"),
                    BotCommand("ping", "Check if the bot is alive or dead"),
                    BotCommand("id", "Get users user_id"),
                    BotCommand("stats", "Check bot stats"),
                    BotCommand("gcast", "Broadcast any message to groups/users"),
                ])

                if bot_info.id not in CLONES:
                    CLONES.add(bot_info.id)
                    
            except (AccessTokenExpired, AccessTokenInvalid):
                await clonebotdb.delete_one({"token": bot_token})
                logging.info(f"Removed expired or invalid token for bot ID: {bot['bot_id']}")
            except Exception as e:
                logging.exception(f"Error while restarting bot with token {bot_token}: {e}")
            
        await asyncio.gather(*(restart_bot(bot) for bot in bots))
        
    except Exception as e:
        logging.exception("Error while restarting bots.")


@app.on_message(filters.command("delallclone") & filters.user(int(OWNER_ID)))
async def delete_all_cloned_bots(client, message):
    try:
        a = await message.reply_text("**Deleting all cloned bots...**")
        await clonebotdb.delete_many({})
        CLONES.clear()
        await a.edit_text("**All cloned bots have been deleted successfully ✅**")
        os.system(f"kill -9 {os.getpid()} && bash start")
    except Exception as e:
        await a.edit_text(f"**An error occurred while deleting all cloned bots.** {e}")
        logging.exception(e)
        
