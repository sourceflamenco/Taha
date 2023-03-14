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
        photo=f"https://telegra.ph/file/73b3ca72688de7dfaa42e.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 🎶\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᯓ• 𝒎𝒂𝒓𝒍𝒆𝒚 ،⚚˹𝐕𝒑𝒏⸥](t.me/Oi_90_7)\n• ᴄʜᴀɴɴᴇʟ » [𝖫𝗂𝗇𝖪 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .](t.me/FH_KN)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", url=f"https://t.me/Oi_90_7")
                ],[
                    InlineKeyboardButton(
                       "تحديثات فلامنكو", url=f"https://t.me/o_xox")
                
                 ],

            ]

        ),

    )
