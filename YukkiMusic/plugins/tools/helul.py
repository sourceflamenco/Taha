import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر    
@app.on_message(
    filters.command(["المطور","مطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b56b90ec8ae744c01048e.jpg",
        caption=f"""- معلومات المطور الاساسي""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("『.𝗟𝗜𝗘𝗡˹.🇮🇹", url=f"https://t.me/llL_67o"),
                ],[
                InlineKeyboardButton(
                        "« تحـديثات لينـدا »", url=f"https://t.me/FH_KP"),
                ]
            ]
        ),
    )