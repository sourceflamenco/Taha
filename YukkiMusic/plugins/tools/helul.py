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
async def aboutd5ev(client: Client, message: Message):

    usr = await client.get_chat(5820455440)

    name = usr.first_name

    bio = (await client.get_chat(5820455440)).bio

    async for photo in client.iter_profile_photos(5820455440, limit=1):

                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑻𝒐 𝑩𝒐𝒕 𝑴𝒊𝒓𝒂 ♪ -› @llL_67o\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝒔 𝑩𝒊𝒐 -› {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=5820455440)

                ],

            ]
