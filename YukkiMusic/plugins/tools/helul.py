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
    filters.command(["المطور","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/flamencoSource/2",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 & 𝗌𝗈𝗎𝗋𝖼𝖾 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𓏺 𝖳𝖺𝗁𝖺 𝖺𝗅 𝖪𝗂𝗅𝖺𝗇𝗂 .", url=f"https://t.me/GBBBBB"),
                ],[
                InlineKeyboardButton(
                        "𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 𓏺", url=f"https://t.me/o_xox"),
                ]
            ]
        ),
    )
