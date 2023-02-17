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
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10dfb95793ff3d40e0a90.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᴋɪʙʀɪᴀ¹](t.me/FH_KN) \n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝚁𝙰𝚂𝙺𝙾²](t.me/AA969622) \n• ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/A1122ll)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات لندا", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["اوامرلندا","الاوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/15ab2ecef4cc16d95be30.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
        
« اليك قائـمة الاوامــر »
          

» لتشغيل اغنيه اكتب : تشغيل او شغل
» لأنهاء الاغنيه اكتب : ايقاف او انهاء 
» لايقاف الاغنيه مؤقت اكتب : قف 
» لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر
» لتخطي الاغنيه اكتب : تخطي او التالي
» لكتم البوت في المحادثه اكتب : ڪتم او اسكتي
» لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي
» لتحميـل الاغانـي اڪتب : بحث او تحميل
» لاعادة تشغيل البوت اكتب : /restart""

اوامـر التشغيـل.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
                ]
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
                        "تحديثات لنـدا", url=f"https://t.me/FH_KP"),
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
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
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
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
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
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )    
@app.on_message(
    filters.command(["مطور","المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cda29519fd4604624777b.jpg",
        caption=f"""ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ
        

•ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᴋɪʙʀɪᴀ¹](https://t.me/FH_KN)

•ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝚁𝙰𝚂𝙺𝙾²‌](https://t.me/AA969622)
 
•ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/A1122ll)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
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
                InlineKeyboardButton("تحديثات لندا ♪", url=f"https://t.me/FH_KP")
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
    
