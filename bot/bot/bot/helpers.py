from pyrogram.types import Message


async def is_group(message: Message) -> bool:
    return message.chat.type in ("group", "supergroup")


def format_duration(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def format_views(views: int) -> str:
    if views >= 1_000_000:
        return f"{views / 1_000_000:.1f}M"
    if views >= 1_000:
        return f"{views / 1_000:.1f}K"
    return str(views)


async def send_error(message: Message, text: str):
    await message.reply_text(f"❌ {text}")


async def send_success(message: Message, text: str):
    await message.reply_text(f"✅ {text}")