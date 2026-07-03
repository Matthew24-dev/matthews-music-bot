import os
import logging
import yt_dlp
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ChatAction

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(message)s'
)
log = logging.getLogger("matthews_music")

BOT_TOKEN = os.environ["BOT_TOKEN"]

YDL_OPTIONS = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'noplaylist': True,
    'nocheckcertificate': True,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0',
    'outtmpl': '/tmp/%(id)s.%(ext)s',
}

SEARCH_RESULTS = {}

def format_duration(seconds):
    if not seconds:
        return "Live"
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    if hours > 0:
        return f"{hours}:{mins:02d}:{secs:02d}"
    return f"{mins}:{secs:02d}"

async def search_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'default_search': f'ytsearch5:{query}',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch5:{query}", download=False)
            if 'entries' in info:
                results = []
                for entry in info['entries'][:5]:
                    if entry:
                        results.append({
                            'title': entry.get('title', 'Unknown'),
                            'url': entry.get('webpage_url', ''),
                            'duration': entry.get('duration', 0),
                            'thumbnail': entry.get('thumbnail', ''),
                            'channel': entry.get('channel', 'Unknown'),
                        })
                return results
    except Exception as e:
        log.error(f"Search error: {e}")
    return []

async def download_audio(url):
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=True)
            if info:
                filename = ydl.prepare_filename(info)
                if not os.path.exists(filename):
                    base = os.path.splitext(filename)[0]
                    for ext in ['m4a', 'mp3', 'webm', 'opus', 'wav']:
                        if os.path.exists(f"{base}.{ext}"):
                            filename = f"{base}.{ext}"
                            break
                return {
                    'file': filename,
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'thumbnail': info.get('thumbnail', ''),
                    'channel': info.get('channel', 'Unknown'),
                    'url': info.get('webpage_url', url)
                }
    except Exception as e:
        log.error(f"Download error: {e}")
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎵 How to Use", callback_data="help")],
        [InlineKeyboardButton("➕ Add to Group", url=f"https://t.me/{context.bot.username}?startgroup=true")],
    ]
    await update.message.reply_text(
        f"🎵 **Hey {update.effective_user.first_name}!**\n\n"
        "I'm **Matthew's Music Bot**! 🎶\n\n"
        "**Quick Start:**\n"
        "• `/play <song name>` - Play any song\n"
        "• `/play <youtube link>` - Play from link\n"
        "• `/search <query>` - Search songs\n"
        "• `/lyrics <song>` - Get lyrics\n\n"
        "Let's play some music! 🎧",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 **Matthew's Music Bot**\n\n"
        "**Playback:**\n"
        "• `/play <song>` - Play a song\n"
        "• `/play <youtube link>` - Play from link\n"
        "• `/search <query>` - Search songs\n\n"
        "**Info:**\n"
        "• `/nowplaying` - Current song\n"
        "• `/lyrics <song>` - Get lyrics\n"
        "• `/ping` - Check status\n\n"
        "**Examples:**\n"
        "`/play Shape of You`\n"
        "`/play https://youtu.be/JGwWNGJdvx8`",
        parse_mode='Markdown'
    )

async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong! Music bot is alive! 🎵")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ **Please provide a song name or link!**\n\n"
            "**Examples:**\n"
            "`/play Shape of You`\n"
            "`/play https://youtu.be/JGwWNGJdvx8`",
            parse_mode='Markdown'
        )
        return
    
    query = ' '.join(context.args)
    
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
    
    if 'youtube.com' in query or 'youtu.be' in query or 'http' in query:
        status_msg = await update.message.reply_text("🔍 Processing link...")
        return await download_and_send(update, context, query, status_msg)
    
    status_msg = await update.message.reply_text(f"🔍 Searching for: **{query}**...", parse_mode='Markdown')
    
    results = await search_youtube(query)
    
    if not results:
        await status_msg.edit_text("❌ No results found! Try a different search.")
        return
    
    if len(results) == 1:
        await status_msg.edit_text(f"✅ Found: **{results[0]['title']}**\n⏬ Downloading...", parse_mode='Markdown')
        return await download_and_send(update, context, results[0]['url'], status_msg)
    
    SEARCH_RESULTS[update.effective_user.id] = results
    
    keyboard = []
    for i, song in enumerate(results):
        duration = format_duration(song['duration'])
        keyboard.append([
            InlineKeyboardButton(
                f"🎵 {i+1}. {song['title'][:40]}... ({duration})",
                callback_data=f"play_{i}"
            )
        ])
    keyboard.append([InlineKeyboardButton("❌ Cancel", callback_data="cancel")])
    
    text = f"🎵 **Search results for:** `{query}`\n\n**Click a song to download:**\n"
    
    await status_msg.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def search_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: `/search <query>`", parse_mode='Markdown')
        return
    
    query = ' '.join(context.args)
    status_msg = await update.message.reply_text(f"🔍 Searching: **{query}**...", parse_mode='Markdown')
    
    results = await search_youtube(query)
    
    if not results:
        await status_msg.edit_text("❌ No results found!")
        return
    
    SEARCH_RESULTS[update.effective_user.id] = results
    
    keyboard = []
    for i, song in enumerate(results):
        duration = format_duration(song['duration'])
        keyboard.append([
            InlineKeyboardButton(
                f"🎵 {i+1}. {song['title'][:40]} ({duration})",
                callback_data=f"play_{i}"
            )
        ])
    
    await status_msg.edit_text(
        f"🔍 **Results for:** `{query}`\n\nClick to play:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def download_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str, status_msg):
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.UPLOAD_VOICE
    )
    
    await status_msg.edit_text("⏬ Downloading audio...")
    
    song_info = await download_audio(url)
    
    if not song_info or not os.path.exists(song_info['file']):
        await status_msg.edit_text("❌ Download failed! Try another song.")
        return
    
    file_size_mb = os.path.getsize(song_info['file']) / (1024 * 1024)
    
    if file_size_mb > 50:
        await status_msg.edit_text(
            f"❌ **File too large!** ({file_size_mb:.1f} MB)\n"
            f"Telegram limit is 50 MB. Try a shorter song."
        )
        try:
            os.remove(song_info['file'])
        except:
            pass
        return
    
    duration = format_duration(song_info['duration'])
    
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.UPLOAD_VOICE
    )
    
    try:
        with open(song_info['file'], 'rb') as audio:
            caption = (
                f"🎵 **{song_info['title']}**\n"
                f"⏱ Duration: {duration}\n"
                f"🎤 {song_info['channel']}\n"
                f"📥 Downloaded via @{context.bot.username}"
            )
            
            await update.message.reply_audio(
                audio=audio,
                caption=caption,
                title=song_info['title'],
                performer=song_info['channel'],
                duration=int(song_info['duration']) if song_info['duration'] else 0,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔗 YouTube", url=song_info['url'])],
                ]),
                read_timeout=120,
                write_timeout=120
            )
        
        await status_msg.delete()
    
    except Exception as e:
        log.error(f"Send error: {e}")
        await status_msg.edit_text(f"❌ Failed to send: {str(e)[:100]}")
    
    finally:
        try:
            os.remove(song_info['file'])
        except:
            pass

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "help":
        await query.edit_message_text(
            "🎵 **How to use Matthew's Music:**\n\n"
            "1️⃣ Type `/play <song name>`\n"
            "2️⃣ Pick a song from the list\n"
            "3️⃣ I'll send the audio!\n\n"
            "**Tips:**\n"
            "• Use `/search` to browse without auto-download\n"
            "• Send YouTube links directly\n"
            "• Songs under 50 MB work best",
            parse_mode='Markdown'
        )
    
    elif data == "cancel":
        await query.edit_message_text("❌ Cancelled.")
    
    elif data.startswith("play_"):
        user_id = query.from_user.id
        if user_id not in SEARCH_RESULTS:
            await query.edit_message_text("❌ Search expired! Please search again.")
            return
        
        idx = int(data.split("_")[1])
        results = SEARCH_RESULTS[user_id]
        
        if idx >= len(results):
            await query.edit_message_text("❌ Invalid selection!")
            return
        
        song = results[idx]
        await query.edit_message_text(f"⏬ Downloading: **{song['title']}**...", parse_mode='Markdown')
        
        song_info = await download_audio(song['url'])
        
        if not song_info or not os.path.exists(song_info['file']):
            await query.edit_message_text("❌ Download failed!")
            return
        
        file_size_mb = os.path.getsize(song_info['file']) / (1024 * 1024)
        
        if file_size_mb > 50:
            await query.edit_message_text(f"❌ File too large ({file_size_mb:.1f} MB). Try another song.")
            try:
                os.remove(song_info['file'])
            except:
                pass
            return
        
        try:
            with open(song_info['file'], 'rb') as audio:
                await query.message.reply_audio(
                    audio=audio,
                    caption=f"🎵 **{song_info['title']}**\n⏱ {format_duration(song_info['duration'])}\n🎤 {song_info['channel']}",
                    title=song_info['title'],
                    performer=song_info['channel'],
                    duration=int(song_info['duration']) if song_info['duration'] else 0,
                    parse_mode='Markdown',
                    read_timeout=120,
                    write_timeout=120
                )
            await query.delete_message()
        except Exception as e:
            await query.edit_message_text(f"❌ Send failed: {str(e)[:100]}")
        finally:
            try:
                os.remove(song_info['file'])
            except:
                pass

async def lyrics_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: `/lyrics <song name>`", parse_mode='Markdown')
        return
    
    query = ' '.join(context.args)
    status = await update.message.reply_text(f"📝 Finding lyrics for: **{query}**...", parse_mode='Markdown')
    
    try:
        parts = query.split(' ', 1)
        artist = parts[0]
        title = parts[1] if len(parts) > 1 else parts[0]
        
        url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            lyrics = data.get('lyrics', '')
            if lyrics:
                if len(lyrics) > 4000:
                    lyrics = lyrics[:4000] + "..."
                
                await status.edit_text(
                    f"📝 **Lyrics for:** {query}\n\n```\n{lyrics}\n```",
                    parse_mode='Markdown'
                )
            else:
                await status.edit_text("❌ Lyrics not found!")
        else:
            await status.edit_text("❌ Lyrics not found! Try `/lyrics artist song`")
    except Exception as e:
        await status.edit_text(f"❌ Error: {str(e)[:100]}")

async def nowplaying(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'current_song' in context.user_data:
        song = context.user_data['current_song']
        await update.message.reply_text(
            f"🎵 **Now Playing:**\n"
            f"**{song['title']}**\n"
            f"⏱ {format_duration(song['duration'])}\n"
            f"🎤 {song['channel']}",
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text("❌ No song playing! Use `/play` to start.")

def main():
    log.info("🎵 Starting Matthew's Music Bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("search", search_cmd))
    app.add_handler(CommandHandler("lyrics", lyrics_cmd))
    app.add_handler(CommandHandler("nowplaying", nowplaying))
    
    app.add_handler(CallbackQueryHandler(button_handler))
    
    log.info("✅ Matthew's Music Bot is online!")
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()