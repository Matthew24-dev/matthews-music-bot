from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
🎵 **Matthew's Music Bot**

Hello {mention}!

I'm a Telegram Music Bot that streams songs directly into Voice Chats.

✨ **Features**
• 🎶 Play music from YouTube
• 🔍 Search songs
• 📜 Lyrics
• ⏯ Pause / Resume
• ⏭ Skip
• ⏹ Stop
• 📋 Queue support

⚠️ **This bot only works in Telegram Groups.**

Add me to your group and make me an administrator.

Type /help to see all available commands.
"""

HELP_TEXT = """
🎵 **Matthew's Music Bot Commands**

▶️ Music
/play <song name> - Play a song
/search <song> - Search YouTube
/lyrics <song> - Get song lyrics

⏯ Player
/pause - Pause music
/resume - Resume music
/skip - Skip current song
/stop - Stop playback
/queue - Show queue

ℹ️ Other
/start - Start the bot
/help - Show this help message
/alive - Check bot status
"""


@Client.on_message(filters.private & filters.command("start"))
async def start_private(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me To Group",
                    url=f"https://t.me/{client.me.username}?startgroup=true",
                )
            ]
        ]
    )

    await message.reply_text(
        START_TEXT.format(mention=message.from_user.mention),
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )


@Client.on_message(filters.group & filters.command("start"))
async def start_group(client, message):
    await message.reply_text(
        "✅ **Matthew's Music Bot is online!**\n\nUse `/play <song name>` to start playing music.",
        quote=True,
    )


@Client.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(
        HELP_TEXT,
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("alive"))
async def alive_command(client, message):
    await message.reply_text(
        "🟢 **Matthew's Music Bot is running successfully!**"
    )