import random
from pyrogram import Client, filters
from pyrogram.types import Message
from PratikBots import PratikBots

# List of reactions (only valid Telegram reactions)
reactions = ["🥰", "❤️", "😁", "💋", "😱", "🤣", "😘", "❤️‍🔥", "👌", "🫡", "😍"]


@PratikBots.on_message(filters.text)
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    await message.react(emoji)

