from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters , enums


@Client.on_message(filters.command('start'))
async def ai_generate_private(client, message):
  buttons = [[
    InlineKeyboardButton("Support", url="https://t.me/XBOTSUPPORTS")
  ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_text(text=f"Hey {message.from_user.mention}\n Iam Advance Awesome Chat Gpt Bot \n\n provide by @XBOTSUPPORTS", reply_markup=reply_markup)
