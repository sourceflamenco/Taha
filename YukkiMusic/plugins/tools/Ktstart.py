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
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5648523284)
    name = usr.first_name
    user = await client.get_chat(5648523284)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5648523284, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""- معلومات المطور الاساسي
                    
ɴᴀᴍᴇ » [{usr.first_name}](https://t.me/MF_K2)
                        
ᴜsᴇʀ » @MF_K2 
                           
bio » {Bio}""", 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/MF_K2")
            ],               
          ]              
       )              
    )                     
                    
