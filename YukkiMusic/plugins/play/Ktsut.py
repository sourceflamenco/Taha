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
async def descut(client, message):
    usr = await client.get_chat(5468131406)
    name = usr.first_name
    bio = (await client.get_chat(5468131406)).bio
    async for photo in client.iter_profile_photos(5468131406, limit=1):
                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝑻𝒐 𝑩𝒐𝒕 𝒍𝒊𝒏𝒅𝒂  ♪ » @llL_67o\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓'𝒔 𝑩𝒊𝒐 » {bio}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=5468131406)
                ],
            ]
        ),
    )
@app.on_message(filters.regex("^كبرياء$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""• 𝒊𝒏 𝒕𝒉𝒆 𝒆𝒏𝒅, 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒃𝒂𝒅, 𝒂𝒏𝒅 𝒕𝒉𝒆𝒚 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒊𝒏𝒏𝒐𝒄𝒆𝒏𝒕\n\n• 𝑵𝒂𝒎𝒆 » {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 » @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 » ʟɪɴᴅᴀ ᴅᴇᴠᴇʟᴏᴘᴇʀ\n• 𝑩𝒊𝒐 » {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=5820455440)

                ],

            ]

        ),

    )

@app.on_message(filters.regex("^ماري$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    bio = usr.bio
    await message.reply_video(
        video=f"https://graph.org/file/e578fe00ad718b7e42626.jpg",
        caption=f"""• 𝒊𝒏 𝒕𝒉𝒆 𝒆𝒏𝒅, 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒃𝒂𝒅, 𝒂𝒏𝒅 𝒕𝒉𝒆𝒚 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒊𝒏𝒏𝒐𝒄𝒆𝒏𝒕\n\n• 𝑵𝒂𝒎𝒆 » {message.from_user.mention}\n• 𝑼𝒔𝒆𝒓 » @{message.from_user.username}\n• 𝑺𝒕𝒂𝒕𝒔 » ʟɪɴᴅᴀ ᴅᴇᴠᴇʟᴏᴘᴇʀ\n• 𝑩𝒊𝒐 » {bio}""",
        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=5566744652)

                ],

            ]

        ),

    )    
