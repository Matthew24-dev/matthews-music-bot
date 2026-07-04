import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls

from bot.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

bot = Client(
    "MatthewsMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

assistant = Client(
    "MatthewsAssistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
)

call_py = PyTgCalls(assistant)


async def main():
    await bot.start()
    print("✅ Bot Started")

    await assistant.start()
    print("✅ Assistant Started")

    await call_py.start()
    print("✅ Voice Chat Client Started")

    me = await bot.get_me()
    print(f"Logged in as @{me.username}")

    await idle()

    await bot.stop()
    await assistant.stop()


if __name__ == "__main__":
    asyncio.run(main()