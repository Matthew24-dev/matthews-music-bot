import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update, ChatPermissions
import yt_dlp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def check_is_group(update: Update) -> bool:
    """Check if message is from a group chat."""
    return update.effective_chat.type in ['group', 'supergroup']

def check_bot_is_admin(update: Update, context) -> bool:
    """Check if bot is admin in the group with required permissions."""
    try:
        bot_member = context.bot.get_chat_member(
            chat_id=update.effective_chat.id,
            user_id=context.bot.id
        )
        
        # Must be admin or creator
        if bot_member.status not in ['administrator', 'creator']:
            return False
        
        # Check if bot has required permissions
        if bot_member.status == 'administrator':
            # Need these permissions for full functionality
            if not (bot_member.can_send_messages and 
                    bot_member.can_delete_messages and
                    bot_member.can_invite_users):
                return False
        
        return True
    except Exception as e:
        logger.error(f"Error checking admin status: {e}")
        return False

def start(update: Update, context):
    """Welcome message - GROUP ONLY."""
    # Reject DMs
    if not check_is_group(update):
        update.message.reply_text(
            "🚫 *This bot only works in group chats!*\n\n"
            "Please add me to a group and make me an admin! 🎵",
            parse_mode='Markdown'
        )
        return
    
    # Check if bot is admin
    if not check_bot_is_admin(update, context):
        update.message.reply_text(
            "⚠️ *I need admin rights!*\n\n"
            "Please make me an admin with these permissions:\n"
            "✅ Send Messages\n"
            "✅ Delete Messages\n"
            "✅ Invite Users\n\n"
            "Then try again! 🎵",
            parse_mode='Markdown'
        )
        return
    
    user = update.effective_user.first_name
    chat = update.effective_chat.title
    
    update.message.reply_text(
        f"🎵 *Hey {user}!*\n\n"
        f"*Welcome to Matthew's Music Bot!* 🎶\n\n"
        f"*Group:* {chat}\n\n"
        f"*How to use:*\n"
        f"Type: /play <song name>\n"
        f"Example: /play despacito\n\n"
        f"I'll search YouTube and play the song here! 🎧",
        parse_mode='Markdown'
    )

def help_command(update: Update, context):
    """Help message - GROUP ONLY."""
    if not check_is_group(update):
        update.message.reply_text(
            "🚫 *This bot only works in group chats!*\n"
            "Add me to a group to use me! 🎵",
            parse_mode='Markdown'
        )
        return
    
    if not check_bot_is_admin(update, context):
        update.message.reply_text(
            "⚠️ *I need admin rights to work!*\n"
            "Please make me an admin first!",
            parse_mode='Markdown'
        )
        return
    
    update.message.reply_text(
        "📖 *Music Bot Commands:*\n\n"
        "🎵 /play <song> - Play a song\n"
        "📋 /queue - Show queue (coming soon)\n"
        "⏭️ /skip - Skip current (coming soon)\n"
        "🛑 /stop - Stop music (coming soon)\n"
        "❓ /help - This message\n\n"
        "*Examples:*\n"
        "/play shape of you\n"
        "/play eminem lose yourself\n"
        "/play https://youtu.be/...\n\n"
        "🎧 Make sure I'm a group admin!",
        parse_mode='Markdown'
    )

def play(update: Update, context):
    """Play a song - GROUP ONLY, ADMIN ONLY."""
    chat_id = update.effective_chat.id
    
    # Reject DMs
    if not check_is_group(update):
        update.message.reply_text(
            "🚫 *This bot only works in group chats!*\n"
            "Add me to a group to use me! 🎵",
            parse_mode='Markdown'
        )
        return
    
    # Check if bot is admin
    if not check_bot_is_admin(update, context):
        update.message.reply_text(
            "⚠️ *I need admin rights!*\n\n"
            "Please make me an admin with:\n"
            "✅ Send Messages\n"
            "✅ Delete Messages\n"
            "✅ Invite Users",
            parse_mode='Markdown'
        )
        return
    
    # Check if user provided a song name
    if not context.args:
        update.message.reply_text(
            "❌ *Please provide a song name!*\n\n"
            "*Example:*\n"
            "/play despacito\n"
            "/play eminem lose yourself",
            parse_mode='Markdown'
        )
        return
    
    # Join all arguments into one search query
    query = " ".join(context.args)
    
    # Check if it's a URL
    if 'youtube.com' in query or 'youtu.be' in query:
        search_query = query
    else:
        search_query = f"ytsearch:{query}"
    
    # Send "searching" message
    status_msg = update.message.reply_text(
        f"🔍 *Searching for:* {query}\n⏳ Please wait...",
        parse_mode='Markdown'
    )
    
    try:
        # Configure yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '/tmp/%(id)s.%(ext)s',
            'noplaylist': True,
            'nocheckcertificate': True,
            'geo_bypass': True,
            'socket_timeout': 30,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # If it's a search query, get the first result
            if search_query.startswith('ytsearch:'):
                info = ydl.extract_info(search_query, download=False)
                if 'entries' in info and len(info['entries']) > 0:
                    video_info = info['entries'][0]
                else:
                    context.bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=status_msg.message_id,
                        text="❌ *No results found!*\nTry a different search term.",
                        parse_mode='Markdown'
                    )
                    return
            else:
                video_info = ydl.extract_info(search_query, download=False)
            
            # Get video details
            title = video_info.get('title', 'Unknown')
            duration = video_info.get('duration', 0)
            uploader = video_info.get('uploader', 'Unknown')
            video_id = video_info.get('id', '')
            webpage_url = video_info.get('webpage_url', '')
            
            # Format duration
            if duration:
                mins = duration // 60
                secs = duration % 60
                duration_str = f"{mins}:{secs:02d}"
            else:
                duration_str = "Unknown"
            
            # Update status: downloading
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"⬇️ *Downloading:*\n{title}\n⏳ Please wait...",
                parse_mode='Markdown'
            )
            
            # Download the audio
            download_opts = ydl_opts.copy()
            download_opts['outtmpl'] = f'/tmp/{video_id}.%(ext)s'
            with yt_dlp.YoutubeDL(download_opts) as ydl:
                ydl.download([webpage_url])
            
            # Find the downloaded file
            audio_file = None
            for ext in ['mp3', 'm4a', 'webm', 'opus', 'ogg', 'wav']:
                test_file = f"/tmp/{video_id}.{ext}"
                if os.path.exists(test_file):
                    audio_file = test_file
                    break
            
            if not audio_file:
                raise Exception("Download failed - file not found")
            
            # Update status: uploading
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"📤 *Uploading:*\n{title}\n⏳ Almost done...",
                parse_mode='Markdown'
            )
            
            # Send the audio to the group
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
                        f"Requested by {update.effective_user.first_name} 🎧"
                    ),
                    parse_mode='Markdown',
                    reply_to_message_id=update.message.message_id
                )
            
            # Delete the status message (requires delete permission)
            try:
                context.bot.delete_message(
                    chat_id=chat_id,
                    message_id=status_msg.message_id
                )
            except:
                pass
            
            # Clean up the file
            if os.path.exists(audio_file):
                os.remove(audio_file)
            
            logger.info(f"Played: {title} for user {update.effective_user.first_name} in {update.effective_chat.title}")
    
    except Exception as e:
        error_msg = str(e)[:200]
        logger.error(f"Error: {error_msg}")
        try:
            context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=status_msg.message_id,
                text=f"❌ *Error:*\n{error_msg}",
                parse_mode='Markdown'
            )
        except:
            update.message.reply_text(
                f"❌ *Error:*\n{error_msg}",
                parse_mode='Markdown'
            )

def error_handler(update: Update, context):
    """Log errors."""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot."""
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN not set!")
        print("Set it with: export BOT_TOKEN='your_token'")
        return
    
    print("🎵 Starting Matthew's Music Bot...")
    print("🔒 GROUP CHATS ONLY - DM messages will be rejected!")
    print("⚠️  Bot must be a GROUP ADMIN to work!")
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("play", play))
    
    # Add error handler
    dp.add_error_handler(error_handler)
    
    print("✅ Bot is running! Press Ctrl+C to stop.")
    print("📱 Add me to a group, make me admin, and type /play <song>")
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()