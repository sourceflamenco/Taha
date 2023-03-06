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

@app.on_message(filters.regex("^تعطيل الايدي$") & filters.group)
async def descut(client, message):
      a = await app.get_chat_member(message.chat.id, message.from_user.id)
      id = message.from_user.id
      cid = message.chat.id
      if cid in disable_cut:
        return await message.reply_text("")

      if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")

          
      if a.can_manage_chat:
        disable_cut.append(cid)
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تعطيل الايدي")
        
@app.on_message(filters.regex("^تفعيل الايدي$") & filters.group)
async def enacut(client, message):
      a = await app.get_chat_member(message.chat.id, message.from_user.id)
      id = message.from_user.id
      cid = message.chat.id
      if cid not in disable_cut:
        return await message.reply_text("")
        

      if not a.can_manage_chat:
         await message.reply_text("**- هذا الأمر يخص المشرفين بس !**")
      
      if a.can_manage_chat:
        disable_cut.remove(cid)
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تفعيل ايدي")        
        
        
@app.on_message(
    filters.command(["ايدي","ا","id"],""))
async def vambir(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""◂ 𝙸𝙳 : ⇨  `{message.from_user.id}`\n\n◂ 𝙸𝙳 𝙶𝚁𝙾𝚄𝙿 : ⇨ `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝙼𝙸𝚂𝚂𝙸𝙽𝙶 𝚆𝙾𝚁𝙳𝚂", url=f"https://t.me/FH_KP"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
