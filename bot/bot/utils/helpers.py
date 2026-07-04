import asyncio
from pyrogram.types import Message


async def edit_or_reply(message: Message, text: str):
    """
    Edit the message if possible, otherwise reply.
    """
    try:
        return await message.edit_text(text)
    except Exception:
        return await message.reply_text(text)


async def delete_after(message: Message, seconds: int = 10):
    """
    Delete a message after the specified number of seconds.
    """
    await asyncio.sleep(seconds)
    try:
        await message.delete()
    except Exception:
        pass


def format_duration(seconds: int) -> str:
    """
    Convert seconds into HH:MM:SS format.
    """
    hours, remainder = divmod(int(seconds), 3600)
    minutes, secs = divmod(remainder, 60)

    if hours:
        return f"{hours:02}:{minutes:02}:{secs:02}"
    return f"{minutes:02}:{secs:02}"