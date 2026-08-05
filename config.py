import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Bot
BOT_NAME = "Maya"
BOT_NAME_BN = "মায়া"

TRIGGERS = [
    "maya",
    "Maya",
    "MAYA",
    "মায়া",
    "মায়া",
]

MAX_REPLY_LINES = 10
MODEL = "gemini-2.5-pro"