from pyrogram import Client
from bot.config import *

app = Client(
    "MatthewsMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message()
async def alive(_, message):
    if message.text == "/alive":
        await message.reply_text(
            "🎵 Matthew's Music Bot is running successfully!"
        )

print("Starting Matthew's Music Bot...")

app.run()