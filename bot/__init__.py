import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import yt_dlp

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🎵 Welcome! Send me a YouTube link!")

def download_audio(update, context):
    url = update.message.text
    if 'youtube.com' not in url and 'youtu.be' not in url:
        update.message.reply_text("Please send a YouTube link!")
        return
    msg = update.message.reply_text("Downloading... Please wait!")
    try:
        ydl_opts = {'format': 'bestaudio/best', 'outtmpl': '/tmp/%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        with open(filename, 'rb') as audio:
            context.bot.send_audio(chat_id=update.effective_chat.id, audio=audio, title=info.get('title', 'Song'))
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg.message_id)
        os.remove(filename)
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)[:100]}")

def main():
    print("Bot starting...")
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_audio))
    print("Bot running!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()