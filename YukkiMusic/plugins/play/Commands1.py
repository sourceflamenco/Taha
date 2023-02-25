import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from YukkiMusic import check_client


@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك  !!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n╔═════• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •════╗

 » لتشغيل اغنيه اكتب \n **تشغيل او شغل**
 » لأنهاء الاغنيه اكتب \n **ايقاف او انهاء* 
 » لايقاف الاغنيه مؤقت اكتب \n وقفي او قفي
 » لتكملة الاغنيه من الايقاف المؤقت اكتب \n **كملي او استمر**
 » لتخطي الاغنيه اكتب \n **تخطي او التالي**
 » لكتم البوت في المحادثه اكتب \n **ڪتم او اسكتي**
 » لألغاء كتم البوت في المحادثه اكتب \n **اتكلم او تكلمي**
 » لتحميـل الاغانـي اڪتب \n **بحث او تحميل**

  ╚════• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •═════╝""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/FH_KP")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂", callback_data="fft"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("sop"))
async def sop(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك  !!", show_alert=True)

    await query.edit_message_text(
       f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝒔𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂\n✧ 𝑱𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒍𝒊𝒏𝒅𝒂 𝑻𝒐 𝑺𝒆𝒆 𝑨𝒍𝒍 𝑼𝒑𝒅𝒂𝒕𝒆\n\n- 𝒌𝒊𝒃𝒓𝒊𝒂 -› @FH_KN\n- 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 -› @FH_KP""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/FH_KP)
                ],[
                    InlineKeyboardButton(
                        "◌sᴏᴜʀᴄᴇ ᴍɪʀᴀ◌", callback_data="am"),
                    InlineKeyboardButton(
                        "◌ᴅᴇᴠᴇʟᴏᴘᴇʀ◌", url=f"t.me/FH_KN")
                ],[

                    InlineKeyboardButton(
                        "رجوع", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )
