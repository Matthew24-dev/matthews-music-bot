import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# Validation
if not API_ID:
    raise ValueError("API_ID is missing!")

if not API_HASH:
    raise ValueError("API_HASH is missing!")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

if not STRING_SESSION:
    raise ValueError("STRING_SESSION is missing!")