<div align="center">

# 🎵 Matthew's Music Bot

### *A powerful Telegram music bot that plays any song you want — instantly, free, forever.*

[![Telegram Bot](https://img.shields.io/badge/Telegram-@MusicBot-blue?style=for-the-badge&logo=telegram)](https://t.me/)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Made With](https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge)]()

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Deploy](#-deploy-your-own) • [Credits](#-credits)

</div>

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

## 🎬 Preview

┌─────────────────────────────────────┐
│  🎵 Matthew's Music Bot             │
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
- Click [here](https://t.me/) to add the bot to your group
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
git clone https://github.com/YOUR_USERNAME/music-bot.git
cd music-bot

# Install dependencies
pip install -r requirements.txt

# Set your bot t…