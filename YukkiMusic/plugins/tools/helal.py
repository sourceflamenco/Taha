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
    filters.command(["منشن","تك عام","@all"],""))
async def tag_all(client, message):
    global stopProcess
    try:
        has_permissions = True
        if has_permissions:
            if len(chatQueue) > 5:
                await message.reply(
                    "⛔️ | I'm already working on my maximum number of 5 chats at the moment. Please try again shortly.")
            else:
                if message.chat.id in chatQueue:
                    await message.reply(
                        "🚫 | There's already an ongoing process in this chat. Please /stop to start a new one.")
                else:
                    chatQueue.append(message.chat.id)
                    if len(message.command) > 1:
                        inputText = message.command[1]
                    elif len(message.command) == 1:
                        inputText = ""
                    membersList = []
                    async for _, v in a.enumerate(await client.get_chat_members(message.chat.id)):
                        if v.user.is_bot == True:
                            pass
                        elif v.user.is_deleted == True:
                            pass
                        else:
                            membersList.append(v.user)
                    i = 0
                    lenMembersList = len(membersList)
                    if stopProcess: stopProcess = False
                    while len(membersList) > 0 and not stopProcess:
                        j = 0
                        text1 = f"{inputText}\n\n"
                        try:
                            while j < 10:
                                user = membersList.pop(0)
                                if user.username == None:
                                    text1 += f"{user.mention} "
                                    j += 1
                                else:
                                    text1 += f"@{user.username} "
                                    j += 1
                            try:
                                await app.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            await asyncio.sleep(10)
                            i += 10
                        except IndexError:
                            try:
                                await app.send_message(message.chat.id, text1)
                            except Exception:
                                pass
                            i = i + j
                    if i == lenMembersList:
                        await message.reply(f"✅ | تم عمل التاك **عدد الاعضاء {i} **.")
                    else:
                        await message.reply(
                            f"✅ | Successfully mentioned **{i} members.**\n❌ | Bots and deleted accounts were rejected.")
                    chatQueue.remove(message.chat.id)
        else:
            await message.reply("👮🏻 | Sorry, **only admins** can execute this command.")
    except FloodWait as e:
        await asyncio.sleep(e.value)


@app.on_message(command(TAG_COMMAND_STOP)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS)
async def tag_all_stop(client, message):
    global stopProcess
    try:
        has_permissions = True
        if has_permissions:
            if not message.chat.id in chatQueue:
                await message.reply("🤷🏻‍♀️ | There is no ongoing process to stop.")
            else:
                stopProcess = True
                await message.reply("🛑 | تم الايقاف بنجاح.")
        else:
            await message.reply("👮🏻 | Sorry, **only admins** can execute this command.")
    except FloodWait as e:
        await asyncio.sleep(e.value)

