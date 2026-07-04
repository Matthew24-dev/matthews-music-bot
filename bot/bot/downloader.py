import os
import yt_dlp

DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_audio(query: str):
    """
    Downloads the best quality audio from YouTube.
    Returns:
        {
            "title": str,
            "duration": int,
            "filepath": str,
            "webpage_url": str
        }
    """

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "default_search": "ytsearch1",
        "extractaudio": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=True)

        if "entries" in info:
            info = info["entries"][0]

        filepath = ydl.prepare_filename(info)
        filepath = os.path.splitext(filepath)[0] + ".mp3"

        return {
            "title": info.get("title", "Unknown"),
            "duration": info.get("duration", 0),
            "filepath": filepath,
            "webpage_url": info.get("webpage_url", ""),
        }