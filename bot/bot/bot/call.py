from pytgcalls import PyTgCalls
from pyrogram import Client

from bot.client import app


call_py = PyTgCalls(app)


async def start():
    await call_py.start()


async def stop():
    await call_py.stop()