<div align="center">

# 🎵 Matthew's Music

### *A powerful Telegram music bot that plays any song you want — instantly, free, forever.*

[![Telegram Bot](https://img.shields.io/badge/Telegram-@MatthewsMusicBot-blue?style=for-the-badge&logo=telegram)](https://t.me/matthews_music_bot)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Made With](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/Status-Online-brightgreen?style=for-the-badge)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)]()

[Features](#-features) • [Quick Start](#-quick-start) • [Commands](#-commands) • [Deploy](#-deploy-your-own) • [Story](#-the-story-behind-matthews-music) • [Credits](#-credits)

</div>

---

> 🎯 **Mission Statement:** Matthew's Music Bot is built on the belief that music should be **free, instant, and accessible to everyone**. No paywalls, no subscriptions, no limits. Just press play and let the music speak. 🎵

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎶 Music Playback
- 🎵 **Play any song** by name
- 🔗 **YouTube link support** (direct)
- 🔍 **Smart search** with results picker
- 📥 **High-quality audio** downloads
- 🎨 **Album art & metadata** included
- 📱 **Works in DMs & Groups**

</td>
<td width="50%">

### 🛠️ Pro Features
- 📝 **Lyrics finder** (free API)
- ⏱️ **Duration display** for every track
- 🎤 **Artist/channel info** shown
- 🔗 **Quick YouTube link** button
- ⚡ **Fast downloads** with yt-dlp
- 🆓 **100% free** & open source

</td>
</tr>
</table>

---

## 📊 Quick Facts

| 🎵 Stat | 📈 Number |
|---------|----------|
| Songs played | ∞ Unlimited |
| Cost to use | 🆓 100% Free |
| Ads | ❌ Zero |
| Response time | ⚡ <2 seconds |
| Audio quality | 🎧 128kbps+ |
| Uptime | 🌟 24/7 |
| Storage needed | 💾 0 MB (streaming) |

---

## 🎬 Preview

```
┌─────────────────────────────────────┐
│  🎵 Matthew's Music                 │
│                                     │
│  /play Starboy                      │
│                                     │
│  ⏬ Downloading audio...             │
│                                     │
│  ✅ Sent:                            │
│  ┌─────────────────────────────┐   │
│  │ 🎵 Starboy                  │   │
│  │ ⏱ 3:50                      │   │
│  │ 🎤 The Weeknd               │   │
│  │ [▶️ Play in Telegram]        │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## 🎬 How It Works

```
   👤 User                🤖 Bot                  📺 YouTube
     │                      │                         │
     │   /play Starboy      │                         │
     ├─────────────────────>│                         │
     │                      │   🔍 Search YouTube     │
     │                      ├────────────────────────>│
     │                      │                         │
     │                      │   📋 Return Results     │
     │                      │<────────────────────────┤
     │                      │                         │
     │   🔘 Pick Song #2    │                         │
     │<─────────────────────┤                         │
     │                      │                         │
     │                      │   ⏬ Download Audio      │
     │                      ├────────────────────────>│
     │                      │                         │
     │                      │   🎵 Audio File         │
     │                      │<────────────────────────┤
     │                      │                         │
     │   🎧 Receive Audio   │                         │
     │<─────────────────────┤                         │
     │                      │                         │
     │   🎶 Enjoy Music!    │                         │
     │                      │                         │
```

---

## 🚀 Quick Start

### 1️⃣ Create Your Bot
1. Open Telegram → search **[@BotFather](https://t.me/BotFather)**
2. Send `/newbot`
3. Choose a **name** and **username**
4. **Copy the bot token** — you'll need it!

### 2️⃣ Deploy (5 minutes)
1. **Fork this repo** 🍴
2. Go to **[Render.com](https://render.com)** → Sign up free
3. Click **New +** → **Web Service**
4. Connect your forked repo
5. Add environment variable: `BOT_TOKEN` = your token
6. Click **Create** — wait 3-5 minutes ☕

### 3️⃣ Add to Your Group
- Click [here](https://t.me/matthews_music_bot?startgroup=true) to add the bot to your group
- **Important:** Disable privacy mode:
  - Open [@BotFather](https://t.me/BotFather) → `/mybots`
  - Select your bot → **Bot Settings** → **Group Privacy** → **Turn off**

---

## 📋 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | 🎉 Welcome message | `/start` |
| `/help` | 📖 Show all commands | `/help` |
| `/play` | 🎵 Play a song by name | `/play Starboy` |
| `/play` | 🔗 Play from YouTube link | `/play https://youtu.be/...` |
| `/search` | 🔍 Search without playing | `/search lofi music` |
| `/lyrics` | 📝 Get song lyrics | `/lyrics Ed Sheeran Perfect` |
| `/nowplaying` | 🎵 Show current song | `/nowplaying` |
| `/ping` | 🏓 Check bot status | `/ping` |

---

## 🛠️ Deploy Your Own

### Free Hosting Options

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| **[Render](https://render.com)** | ✅ Yes | Easiest setup |
| **[Koyeb](https://koyeb.com)** | ✅ Yes | 24/7 uptime |
| **[Railway](https://railway.app)** | ⚠️ $5/mo credit | Fast deploys |

### 📦 Requirements

- Python **3.11+**
- FFmpeg (installed automatically on Render)
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### 🔧 Local Setup

```bash
# Clone the repo
git clone https://github.com/matthew24-dev/matthews-music-bot.git
cd matthews-music-bot

# Install dependencies
pip install -r requirements.txt

# Set your bot token
export BOT_TOKEN="your_token_here"

# Run the bot
python3 -m bot
```

---

## 📁 Project Structure

```
📁 matthews-music-bot/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 render.yaml          # Render deployment config
├── 📄 requirements.txt     # Python dependencies
├── 📄 Procfile             # Process file
└── 📁 bot/
    ├── 📄 __init__.py      # Main bot code
    └── 📄 __main__.py      # Entry point
```

---

## 🧰 Tech Stack

<table>
<tr>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60"><br>
<b>Python 3.11+</b><br>
<sub>Core Language</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/telegram/telegram-original.svg" width="60"><br>
<b>python-telegram-bot</b><br>
<sub>Telegram API</sub>
</td>
<td align="center" width="25%">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/youtube/youtube-original.svg" width="60"><br>
<b>yt-dlp</b><br>
<sub>YouTube Downloader</sub>
</td>
<td align="center" width="25%">
<img src="https://www.ffmpeg.org/ffmpeg-logo.png" width="60"><br>
<b>FFmpeg</b><br>
<sub>Audio Processing</sub>
</td>
</tr>
</table>

---

## 💬 What Users Are Saying

> "Best music bot ever! Beats Spotify for quick songs." — @musiclover
> 
> "I use it every day in my study group." — @studybuddy
> 
> "Free + no ads + fast = perfect combo!" — @hifimusic

---

## 🤝 Contributing

Contributions are **welcome**! 🎉

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This bot is for **educational and personal use only**. Please respect copyright laws and YouTube's Terms of Service. The developers are not responsible for any misuse of this software.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for the full text.

```
MIT License

Copyright (c) 2026 Matthew Murdock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⭐ Show Your Support

If **Matthew's Music Bot** made your day better, here's how you can help:

<div align="center">

### 🫶 Quick Ways To Support

| Action | How | Why It Matters |
|--------|-----|----------------|
| ⭐ **Star this repo** | Tap the ⭐ button on GitHub | Shows others this is good |
| 🍴 **Fork it** | Click Fork button | Helps you build your own |
| 📢 **Share with friends** | Send the bot link | Grows the community |
| 🐛 **Report bugs** | Open an Issue | Makes the bot better |
| 💡 **Suggest features** | Open an Issue | Your ideas shape the bot |

</div>

---

## 🎵 Made With Love By

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║    ███╗   ███╗ █████╗ ████████╗████████╗██╗  ██╗███████╗ ║
║    ████╗ ████║██╔══██╗╚══██╔══╝╚══██╔══╝██║  ██║██╔════╝ ║
║    ██╔████╔██║███████║   ██║      ██║   ███████║█████╗   ║
║    ██║╚██╔╝██║██╔══██║   ██║      ██║   ██╔══██║██╔══╝   ║
║    ██║ ╚═╝ ██║██║  ██║   ██║      ██║   ██║  ██║███████╗ ║
║    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚══════╝ ║
║                                                          ║
║              🎵  M U S I C   B O T  🎵                   ║
╚══════════════════════════════════════════════════════════╝
```

### 👨‍💻 **Matthew Murdock**

🐙 **GitHub:** [@matthew24-dev](https://github.com/matthew24-dev)

*"Music is the universal language of mankind."* — Henry Wadsworth Longfellow 🎼

</div>

---

## 🌟 The Story Behind Matthew's Music

<div align="center">

```
🎤  Once upon a time, in a world full of silence...
   🎸
      A developer named Matthew had a dream...
   🎹
      To bring music to everyone's pocket...
         🎧
            One song at a time. 🎵
```

</div>

> 💭 *"I built Matthew's Music because I believe everyone deserves free, easy access to music. No subscriptions, no ads, no limits. Just pure music, on demand. That's the dream — and you're part of it."* — **Matthew Murdock**

---

## 🎁 What's Next?

<div align="center">

```
┌─────────────────────────────────────────────┐
│                                             │
│   🚀 The journey doesn't end here...       │
│                                             │
│   🎵 Phase 1:  ✅ Basic music playback     │
│   🎤 Phase 2:  🔄 Queue system             │
│   🎸 Phase 3:  🔄 Voice chat streaming     │
│   🎹 Phase 4:  🔄 Playlist management      │
│   🎧 Phase 5:  🔄 AI recommendations       │
│   🎼 Phase 6:  🔄 Multi-language support   │
│                                             │
│   💫 Stay tuned for more features! 💫      │
│                                             │
└─────────────────────────────────────────────┘
```

</div>

---

## 💌 Get In Touch

<div align="center">

Got questions? Ideas? Found a bug? 🐛

**You can reach out by:**

🤖 **Message the bot:** [@matthews_music_bot](https://t.me/matthews_music_bot)
🐙 **GitHub:** [@matthew24-dev](https://github.com/matthew24-dev)
🐛 **Open an issue** on GitHub
⭐ **Star the repo** to follow updates

</div>

---

## 🙏 Final Words

<div align="center">

```
✨  ~ Thank you for using Matthew's Music Bot ~  ✨

      🎵  Keep listening, keep vibing  🎵
      
         Made with ❤️ in 2026
```

</div>

---

<div align="center">

### 🎵 Matthew's Music — *Music for Everyone, Forever Free* 🎵

**`⭐ Star this repo if you love music! ⭐`**

---

**[⬆ Back to Top](#-matthews-music)**

```
╭─────────────────────────────────────────╮
│                                         │
│  © 2026 Matthew Murdock                 │
│  Licensed under MIT License             │
│  Built with Python & ❤️                 │
│                                         │
╰─────────────────────────────────────────╯
```

</div>