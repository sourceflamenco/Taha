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
    filters.command(["كبرياء","كبريا"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/588d70e34b51710ae8dce.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝑴𝒊𝒓𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ -› @llL_67o\n• ᴄʜᴀɴɴᴇʟ ᴍɪʀᴀ -› @NvvvC\n\n**- للتنصيب او للاستفسار تواصل مع مطور السورس**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور السورس", user_id=5820455440)
                ],[
                    InlineKeyboardButton(
                       "تحديثات ميرا", url=f"https://t.me/NvvvC")
                
                 ],

            ]

        ),

    )