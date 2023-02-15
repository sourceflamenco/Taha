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
        caption=f"""ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ
        
         ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌯︙*[𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ‌](https://t.me/FH_KP)*

⌯︙*[َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼](َِhttps://t.me/FH_KP)*

⌯︙*[𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ‌](https://t.me/CR_7_L)*

         ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉""",
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
    filters.command(["بوت الحذف"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bc5810a111c94694e66a.jpg",
        caption=f"""فڪـر قبـل لا تحذف 🥺..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("بـوت الحـذف", url=f"https://t.me/DTeLebot"),
                ],[
                InlineKeyboardButton(
                        "𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 ِٚ𝙇َِ𝙄َِ𝙉َِ𝘿َِ𝘼", url=f"https://t.me/FH_KP"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""اي يقلبـي 🤍😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♥️َ♪✗⇣", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    ) 
@app.on_message(
    filters.command(["مين انا"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""انت قلبي ❤😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♥️َ♪✗⇣", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )       
@app.on_message(
    filters.command(["انا مين"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""ـ• ﺂٰنـُـٰٰت ﺂٰلـُُـٰ؏ـٖمـࢪَٰٰي َ،🤭♥️ ֆ ۦٰ،""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♥️َ♪✗⇣", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )    
@app.on_message(
    filters.command(["مطور","المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/694b785f09dca102bb320.jpg",
        caption=f"""ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ
        
╔════ ⋆★⋆ ═════
║
╠⌯︙» [𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ‌](https://t.me/FH_KP)
║
╠⌯︙» [𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍¹ ](https://t.me/FH_KN)
║
╠⌯︙» [𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍² ‌](https://t.me/CR_7_L)
║
╚════ ⋆★⋆ ═════""",
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
    filters.command(["لندا"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""اي يقلبي 🤍😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♥️َ♪✗⇣", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["ميديا", "/tm", "tgm"],""))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("الرد على ملف وسائط مدعوم ")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await message.reply("غير مدعوم !")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton("فتح الرابط 🔗", url=f"https://telegra.ph{response[0]}")]])
        await message.reply(f"**الرابط »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)          


@app.on_message(
    filters.command(["الرابط"],""))
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    