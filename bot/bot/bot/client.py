from pyrogram import Client
from pyrogram.enums import ParseMode

from bot.config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
)

app = Client(
    "MatthewMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
)