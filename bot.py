# bot.py
from config import Config
import openai
import os

# Load environment variables
openai.api_key = Config.OPENAI_API_KEY
api_hash = Config.API_HASH
api_id = Config.API_ID
bot_token = Config.BOT_TOKEN

# ... rest of your code ...
