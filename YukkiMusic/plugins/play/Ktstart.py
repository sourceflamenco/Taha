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

@app.on_message(filters.regex("^المطور$") & filters.group)
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
                    
