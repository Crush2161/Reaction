from config import OWNER_USERNAME, SUPPORT_GRP
from PratikBots import PratikBots
from pyrogram import Client, filters


START = """**✦ » ʜᴇʟʟᴏ ʙᴀʙʏ 🥀**\n\n**✦ » 𝐈 ᴀᴍ ᴀᴜᴛᴏ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ ғᴏʀ ᴄʜᴀɴɴᴇʟ, ᴘʀɪᴠᴀᴛᴇ ᴀɴᴅ ɢʀᴏᴜᴘ.**\n\n**✦ » 𝖶ɪᴛʜ /clone ᴀɴᴅ ʙʀᴏᴀᴅᴄᴀsᴛ ғᴇᴀᴛᴜʀᴇs.**\n\n**✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [𝐅𝐎𝐑𝐄𝐕𝐄𝐑 𝐂𝐑𝐔𝐒𝐇](t.me/FOREVER_CRUSH)**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/CRUSH_FOREVER).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
❖ 𝖢ᴏᴍᴍᴀɴᴅs ғᴏʀ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ:

➻ /start sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ !
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /stats - ɢᴇᴛ ʙᴏᴛ ꜱᴛᴀᴛꜱ
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [ᴄʀᴜsʜ ʙᴏᴛs](t.me/CRUSH_FOREVER)**
"""

CHATBOT_READ = f"""**
❖ 𝖢ᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs :

➻ /clone [ ʙᴏᴛ ᴛᴏᴋᴇɴ ] - ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.
──────────────
➻ /cloned - sᴇᴇ ᴄʟᴏɴᴇᴅ ʙᴏᴛs.
──────────────
➻ /delclone - ʀᴇᴍᴏᴠᴇ ʏᴏᴜʀ ʙᴏᴛ ᴄʟᴏɴᴇ.
──────────────
➻ /delallclone - ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴄʟᴏɴᴇᴅ ʙᴏᴛs ᴏɴʟʏ ᴏᴡɴᴇʀ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.
──────────────
✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [ᴄʀᴜsʜ ʙᴏᴛs](t.me/CRUSH_FOREVER)**
"""

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{PratikBots.name}](https://t.me/{PratikBots.username}) ʀᴇᴀᴄᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴍᴇssᴇᴀɢᴇ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴍᴀᴋᴇ ʀᴇᴀᴄᴛɪᴏɴ sᴛᴀᴛs ɢʀᴏᴜᴘs / ᴄʜᴀɴɴᴇʟ.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{PratikBots.name}](https://t.me/{PratikBots.username})**
"""
