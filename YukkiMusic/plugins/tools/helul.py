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
    filters.command(["كبريا","كبرياء"],""))
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5471782092)
    name = usr.first_name
    user = await client.get_chat(5471782092)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5471782092, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/PW_BOB) 🕷
                        
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @PW_BOB 🕷
                           
ႦᎥ᥆ | - {Bio} 🕷           
                          
Ꭵժ | - 5471782092 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/PW_BOB")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    zoharyus = "@PW_BOB"
                    message_link = await Telegram.get_linok(message)
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5471782092, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                           return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",)
