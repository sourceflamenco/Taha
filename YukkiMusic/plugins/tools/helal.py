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
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**
»**لاعادة تشغيل البوت اكتب** : /restart.""",
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
    filters.command(["مطور","المطور"],""))
async def aboutd5ev(client: Client, message: Message):

    usr = await client.get_chat(5468131406)

    name = usr.first_name

    bio = (await client.get_chat(5468131406)).bio

    async for photo in client.iter_profile_photos(5468131406, limit=1):

                    await message.reply_photo(photo.file_id, caption=f"""- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝒊𝒅 ⇨  [『.𝗟𝗜𝗘𝗡˹.](t.me/llL_67o)\n\n- 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓'𝒔 𝑩𝒊𝒐 ⇨ {bio}""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, user_id=5468131406)

                ],

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
    filters.command(["الرابط"],""))
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    
