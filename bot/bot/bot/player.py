from pyrogram import Client
from pyrogram.types import Message

from bot.queue import queues


class MusicPlayer:
    def __init__(self):
        self.active_chats = set()

    async def start_stream(self, chat_id: int, stream_url: str):
        self.active_chats.add(chat_id)
        if chat_id not in queues:
            queues[chat_id] = []
        return True

    async def stop_stream(self, chat_id: int):
        self.active_chats.discard(chat_id)
        queues.pop(chat_id, None)
        return True

    async def pause_stream(self, chat_id: int):
        return True

    async def resume_stream(self, chat_id: int):
        return True

    async def skip_stream(self, chat_id: int):
        if chat_id not in queues:
            return False

        if len(queues[chat_id]) > 0:
            queues[chat_id].pop(0)

        return True


player = MusicPlayer()