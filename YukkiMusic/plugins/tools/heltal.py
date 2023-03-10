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
    filters.command(["ليان"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/588d70e34b51710ae8dce.jpg",
        caption=f"""**𝑾𝒆𝒍𝒄𝒐𝒎𝒆**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton (name, url=f"https://t.me/MF_K2")
                ],[
                    InlineKeyboardButton("تحديثات لندا", url=f"https://t.me/FH_KP")
                
                 ],

            ]

        ),

    )
