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
    filters.command(["سورس","السورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1975238af57c2c8621348.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
         [⌞ 𝐬𝐨𝐮𝐫𝐜𝐞 𝐥𝐢𝐧𝐝𝐚 ⌝](https://t.me/FH_KP)
         [⌞ ᴘɪᴄᴀssᴏ ⌝](https://t.me/CR_7_L)
         [⌞ ᴋɪʙʀɪᴀ ⌝](https://t.me/FH_KN)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "« أضغـط لاضـافتـي لمجموعتك »", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["الاوامر","/start"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/acc59bd6e3af1579bd40b.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
        
« اليك قائـمة الاوامــر »

          [⌞ 𝙻𝙾𝚂𝚃 𝚆𝙾𝚁𝙳𝚂 ⌝](https://t.me/FH_KP) 

- لتشغيل اغنيه اكتب : تشغيل او شغل او /play
- لأنهاء الاغنيه اكتب : ايقاف او انهاء او /stop
- لايقاف الاغنيه مؤقت اكتب : قف او /pause
- لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او /resume
- لتخطي الاغنيه اكتب : تخطي او /skip
- لكتم البوت في المحادثه اكتب : ڪتم او /mute
- لألغاء كتم البوت في المحادثه اكتب : اتكلم او /unmute
- لاعادة تشغيل البوت اكتب : /restart""

          [⌞ 𝙻𝙾𝚂𝚃 𝚆𝙾𝚁𝙳𝚂 ⌝](https://t.me/FH_KP) 
1 ← اوامـر التشغيـل.""",
      reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "« َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 »", url=f"https://t.me/FH_KP"),

                ],

            ]

        ),

    )  
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""لا تناديني لي بوت معـي اسم ترا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""اسـمي لندا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""عيـوني ›𓌗⋆🥺›🌸›""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""خيــر ياطيـر 🙂..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""يالبيـه ›𓌗⋆🥺›🌸›""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""لا تناديني لي بوت معـي اسم ترا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7e51929d9635e47097113.jpg",
        caption=f"""لا تناديني لي بوت معـي اسم ترا""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ],[
                InlineKeyboardButton(
                        "ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼 َِ𝙈َِ𝙐َِ𝙎َِ𝙄َِ𝘾", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ]
            ]
        ),
    )    
    
    