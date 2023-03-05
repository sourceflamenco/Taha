import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^المطور$") & filters.group & ~filters.edited)
async def aboutd5ev(client: Client, message: Message):
    usr = await client.get_chat(5468131406)
    name = usr.first_name
    bio = (await client.get_chat(5468131406)).bio
    async for photo in client.iter_profile_photos(5468131406, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑻𝒐 𝑩𝒐𝒕 𝒍𝒊𝒏𝒅𝒂 ♪ -› @llL_67o\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓'𝒔 𝑩𝒊𝒐 -› {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=5468131406)
                ],
            ]
        ),
    )
