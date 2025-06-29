from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.types import Message
from PratikBots import PratikBots
from PratikBots.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    #SOURCE_READ,
    START,
)

@PratikBots.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    reaction_bot = await client.get_me()
    buttons = [
        [InlineKeyboardButton("✙ ʌᴅᴅ ϻє ʙᴀʙу ✙", url=f"http://t.me/{reaction_bot.username}?startgroup=botstart")],
        [InlineKeyboardButton("⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", url="https://t.me/CRUSH_FOREVER"),
         InlineKeyboardButton("⌯ 𝖴ᴘᴅᴀᴛᴇs ⌯", url="https://t.me/+Rv1BIrd2MsgxMWVl")],
        [InlineKeyboardButton("⌯ 𝖧ᴇʟᴘ ᴧηᴅ 𝖢ᴏϻϻᴧηᴅs ⌯", callback_data="HELP")]
    ]
    photo_url = "https://files.catbox.moe/8vbfvp.jpg"
    await client.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=f"**✦ » ʜᴇʏ {message.from_user.mention}!**\n**✦ ɪ'ᴍ ʏᴏᴜʀ ᴀᴜᴛᴏ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ !!**\n\n**◆ ɪ'ᴍ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs, ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs ᴡɪᴛʜ ᴀ ʀᴀɴᴅᴏᴍ ᴇᴍᴏᴊɪ..!!**\n\n**✦ 𝖶ɪᴛʜ /clone ᴀɴᴅ /broadcast ғᴇᴀᴛᴜʀᴇs.**\n\n**✦ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [ғᴏʀᴇᴠᴇʀ ᴄʀᴜsʜ](t.me/FOREVER_CRUSH)**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    
