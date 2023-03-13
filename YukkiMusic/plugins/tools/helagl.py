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
    filters.command([".","ماري"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/588d70e34b51710ae8dce.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 🎶\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᯓ• 𝒎𝒂𝒓𝒍𝒆𝒚 ،⚚˹𝐕𝒑𝒏⸥](t.me/Oi_90_7)\n• ᴄʜᴀɴɴᴇʟ » [『.𝗟𝗜𝗘𝗡˹.🇮🇹](t.me/FH_KN)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", user_id=5667443252)
                ],[
                    InlineKeyboardButton(
                       "تحديثات لينـدا", url=f"https://t.me/FH_KP")
                
                 ],

            ]

        ),

    )
