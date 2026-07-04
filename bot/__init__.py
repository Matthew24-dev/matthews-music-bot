import os
import logging
from telegram.ext import Updater, CommandHandler
import yt_dlp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def check_is_group(update):
    return update.effective_chat.type in ['group', 'supergroup']

def check_bot_is_admin(update, context):
    try:
        bot_member = context.bot.get_chat_member(
            chat_id=update.effective_chat.id,
            user_id=context.bot.id
        )
        return bot_member.status in ['administrator', 'creator']
    except Exception as e:
        logger.error(f"Error: {e}")
        return False

def start(update, context):
    if not check_is_group(update):
        update.message.reply_text(
            "🚫 *This bot only works in group chats!*\n"
            "Add me to a group! 🎵",
            parse_mode='Markdown'
        )
        return
    
    if not check_bot_is_admin(update, context):
        update.message.reply_text(
            "⚠️ *I need admin rights!*\n"
            "Please make me an admin!",
            parse_mode='Markdown'
        )
        return
    
    user = update.effective_user.first_name
    chat = update.effective_chat.title
    
    update.message.reply_text(
        f"🎵 *Hey {user}!*\n\n"
        f"*Matthew's Music Bot!* 🎶\n\n"
        f"*Group:* {chat}\n\n"
        f"Type: `/play <song name>`\n"
        f"Example: `/play despacito`",
        parse_mode='Markdown'
    )

def help_command(update, context):
    if not check_is_group(update):
        update.message.reply_text("🚫 Group chats only!")
        return
    
    update.message.reply_text(
        "📖 *Commands:*\n\n"
        "🎵 `/play <song>` - Play a song\n"
        "❓ `/help` - This message\n\n"
        "*Examples:*\n"
        "`/play despacito`\n"
        "`/play eminem`",
        parse_mode='Markdown'
    )

def play(update, context):
    chat_id = update.effective_chat.id
    
    if not check_is_group(update):
        update.message.reply_text("🚫 Group chats only!")
        return
    
    if not check_bot_is_admin(update, context):
        update.message.reply_text("⚠️ I need admin rights!")
        return
    
    if not context.args:
        update.message.reply_text(
            "❌ *Please provide a song name!*\n"
            "Example: `/play despacito`",
            parse_mode='Markdown'
        )
        return
    
    query = " ".join(context.args)
    
    if 'youtube.com' in query or 'youtu.be' in query:
        search_query = query
    else:
        search_query = f"ytsearch:{query}"
    
    status_msg = update.message.reply_text(
        f"🔍 *Searching:* `{query}`\n⏳ Please wait...",
        parse_mode='Markdown'
    )
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '/tmp/%(id)s.%(ext)s',
            'noplaylist': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if search_query.startswith('ytsearch:'):
                info = ydl.extract_info(search_query, download=False)
                if 'entries' in info and len(info['entries']) > 0:
                    video_info = info['entries'][0]
                else:
                    context.bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=status_msg.message_id,
                        text="❌ No results found!"
                    )
                    return
            else:
                video_info = ydl.extract_info(search_query, download=False)
            
            title = video_info.get('title', 'Unknown')
            duration = video_info.get('duration', 0)
            uploader = video_info.get('uploader', 'Unknown')
            video_id = video_info.get('id', '')
            webpage_url = video_info.get('webpage_url', '')
            
            if duration:
                mins = duration // 60
                secs = duration % 60
                duration_str = f"{mins}:{secs:02d}"
            else:
                duration_str = "Unknown"
            
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"⬇️ *Downloading:*\n`{title}`",
                parse_mode='Markdown'
            )
            
            download_opts = ydl_opts.copy()
            download_opts['outtmpl'] = f'/tmp/{video_id}.%(ext)s'
            with yt_dlp.YoutubeDL(download_opts) as ydl:
                ydl.download([webpage_url])
            
            audio_file = None
            for ext in ['mp3', 'm4a', 'webm', 'opus', 'ogg']:
                test_file = f"/tmp/{video_id}.{ext}"
                if os.path.exists(test_file):
                    audio_file = test_file
                    break
            
            if not audio_file:
                raise Exception("Download failed")
            
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"📤 *Uploading:*\n`{title}`",
                parse_mode='Markdown'
            )
            
            with open(audio_file, 'rb') as audio:
                context.bot.send_audio(
                    chat_id=chat_id,
                    audio=audio,
                    title=title,
                    performer=uploader,
                    duration=duration,
                    caption=(
                        f"🎵 *{title}*\n"
                        f"👤 {uploader}\n"
                        f"⏱️ {duration_str}\n\n"
                        f"By {update.effective_user.first_name} 🎧"
                    ),
                    parse_mode='Markdown',
                    reply_to_message_id=update.message.message_id
                )
            
            try:
                context.bot.delete_message(
                    chat_id=chat_id,
                    message_id=status_msg.message_id
                )
            except:
                pass
            
            if os.path.exists(audio_file):
                os.remove(audio_file)
    
    except Exception as e:
        error_msg = str(e)[:200]
        try:
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"❌ *Error:*\n`{error_msg}`",
                parse_mode='Markdown'
            )
        except:
            update.message.reply_text(
                f"❌ *Error:*\n`{error_msg}`",
                parse_mode='Markdown'
            )

def error_handler(update, context):
    logger.error(f"Update {update} caused error {context.error}")

def main():
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN not set!")
        return
    
    print("🎵 Starting Matthew's Music Bot...")
    print("🔒 GROUP CHATS ONLY!")
    print("⚠️ Bot must be GROUP ADMIN!")
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("play", play))
    dp.add_error_handler(error_handler)
    
    print("✅ Bot is running!")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()