#test
import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InputMediaPhoto, InputMediaVideo
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


@app.on_callback_query(filters.regex("tt"))
async def gtt(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك !", show_alert=True)


    await query.edit_message_text(
       f"""\n\n╔═══• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •═══╗\n\n 
» /channelplay \n لربط القناه بالجروب اڪتب مع معرف قناتك لازم تكون المالك
» /cplay \n لتشغيـل في القناه اڪتب
» /cstop \n لايقاف التشغيـل في القناه اڪتب 
» /cpause \n لايقاف الاغنيه مؤقت اكتب 
» /cresume \nلتكملة الاغنيه من الايقاف المؤقت اكتب
» /cskip \n لتخطي الاغنيه اكتب
» /cmute \n لكتم البوت في المحادثه اكتب
» /cunmute \n لألغاء كتم البوت في المحادثه اڪتب
» لاستفسار تـواصل مـع مطـورالبـوت المطـور"

╚═══• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •═══╝""",
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
                        "اغلاق", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft")


               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("am"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/04820d03273635030fb5b.jpg",None,
           "**✧ اهلين فيك في اوامر بوت لندا**\n\n- عندك خمس ازرار وبعدها بتعرف تستخدم البوت ان شاء الله\n\n• مطور البوت -› @FH_KN\n• قناة البوت -› @FH_KP"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),
                        
                    InlineKeyboardButton(
                        "تحديثات لندا 🥢", url=f"https://t.me/FH_KP"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("amm"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/04820d03273635030fb5b.jpg",None,
           "✧ اهلين فيك في اوامر بوت لندا (:\n\n- **كل اوامر البوت عندك بالازرار تحت استكشفهم بنفسك**\n\n• Developer -› [ᴋɪʙʀɪᴀ](t.me/FH_KN)\n• Channel -› [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP)"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),
                   

                    InlineKeyboardButton(
                        "تحديثات لندا 🥢", url=f"https://t.me/FH_KP"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("cha"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("للأسف الطلب مو لك !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/04820d03273635030fb5b.jpg",
           "- هلا والله\n◌**تريد تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **/channelplay + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**.."
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامر التشغيل بالقنوات", callback_data=f"tt"),

                ],
            ]
        ),
    )


