import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["التشغيل بالقنوات"])
    & filters.group
    & ~filters.edited
)
async def khlop(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/04820d03273635030fb5b.jpg",
        caption=f"""• **اضغط الزر الي تحت عشان تشوف شرح التشغيل بالقنوات** •""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/LANDHLBOT"),
                ],[
                    InlineKeyboardButton(
                        "شرح التشغيل بالقنوات", callback_data=f"cha"),
                ],
            ]
        ),
    )
