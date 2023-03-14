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
        photo=f"https://telegra.ph/file/b56b90ec8ae744c01048e.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝖫𝗂𝗇𝖪 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .¹](t.me/FH_KN) \n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝖫𝗂𝗇𝖪 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .](t.me/llL_67o) \n• ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/o_xox)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("السورس", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["الاوامر"))
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
                InlineKeyboardButton("السورس", url=f"https://t.me/o_xox")
                ]
            ]
        ),
