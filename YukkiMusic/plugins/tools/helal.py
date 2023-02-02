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
    filters.command(["مطور","المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""✅ مرحبا بك عزيزي {message.from_user.mention}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓", url=f"https://t.me/MIDO_Jr"),
                ],[
                InlineKeyboardButton(
                        "𝑺𝒐𝒖𝒓𝒄𝒆", url=f"https://t.me/Just_Ghosst"),
                ]
            ]
        ),
    )
    
    
