# bot.py
from telethon.sync import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN

class TelegramBot:
    def __init__(self):
        self.client = TelegramClient('bot_session', API_ID, API_HASH)
        self.bot_token = BOT_TOKEN

    def run(self):
        with self.client:
            print("Telegram Bot is running!")

if __name__ == "__main__":
    bot = TelegramBot()
    bot.run()
