# Copyright 2024 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
Hello. Send media here or add me as an admin with delete-message permission in a group, and I will moderate NSFW media.

Use /help to see the minimum permissions I need..
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="UPDATE",url="https://t.me/shona_updatesss")
                ]
            ]
        )
    )
