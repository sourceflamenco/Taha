import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic import settingsApp
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^المطور$") & filters.group)
async def descut(client, message):
    usr = await client.get_users(5818384418)
    name = usr.first_name
    user = await client.get_chat(5818384418)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5818384418, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/Batlstuta) 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @Batlstuta 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5818384418 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/Batlstuta")
            ],             
          ]                 
       )                     
    )