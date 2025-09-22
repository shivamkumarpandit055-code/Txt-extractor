import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22448724"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "4dcc0e5b700ad50b1f878e6f1e44c172")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8250884972:AAEuKfSaIX5B9NyfFjSFi-BkveD5-2k6JTA")

OWNER_ID = int(os.environ.get("OWNER_ID", "7276272743"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7276272743 7276272743").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://shivamkumar055gram:JkInylriCfgItXqd@cluster0.tnjashu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002838326478"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002838326478")  # Optional here you'll get all logs
