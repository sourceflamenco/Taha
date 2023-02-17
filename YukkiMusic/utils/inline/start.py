import asyncio
import re
import os
import random
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app

def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"",
            ),
            InlineKeyboardButton(
                text=_["S_B_S"], callback_data="amm"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(

                    text=_["S_B_9"], url=f"https://t.me/so_alfaa"

                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], url=f"https://t.me/FH_KP"
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_12"], url=f"https://t.me/FH_KN"

                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_10"], url=f"https://t.me/so_alfaa"

                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons





  
  
REPLY_MESSAGE = "- مرحـبا حبـي عندك الازرار تحت استمتع"

REPLY_MESSAGE_BUTTONS = [
         [
             ("طريقة تشغيل لندا"),                   
             ("اوامر لندا")

          ],
          [
             ("المطور"),
             ("السورس")
          ],
          [
             ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & filters.command("commands"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.regex("اخفاء الازرار") & filters.private)
async def down(client, message):
          m = await message.reply("**- ابشر حبـي تم اخفاء الازرار بنجاح\n- لو تريـد تطلعها مرة ثانية ارسل**» /commands", reply_markup= ReplyKeyboardRemove(selective=True))
########رسائل الستارت########

@app.on_message(filters.private & command("طريقة تشغيل"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **اهلـين حبـي عشان تفعل بوت لندا اتبع الخطوات الي بالاسفل**

1 • ضيف البوت لقروبك 
2 • ارفعه مشرف بكل الصلاحيات 
3 • لو تريـد تشوف الاوامر اكتب [ لاوامر ] ولو تريـد تشغل على طول اكتب لندا شغلي + اسم المقطع الصوتي

• مثال : لندا شغلي واتنسيت

- لو واجهت مشكله او ما فهمت خطوة كلم مطور البوت ~ @FH_KN""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- مرحـبا فيك بسورس لندا ياحلو
• عندك استفسار بخصوص البوت تواصل مع مطور البوت**

مطور السورس » [𝒌𝒊𝒃𝒓𝒊𝒂](t.me/FH_KN)
قناة السورس » [𝑠𝑜𝑢𝑟𝑐𝑒 𝑙𝑖𝑛𝑑𝑎](t.me/FH_KP)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

###################new lian#############

REPLY_MESSAGEE = "- هلا فيك في قسم الاوامر"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.private & command("اوامر لندا"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.private & command("رجوع"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("شرح التشغيل بمنصات الاغاني"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** مرحـبا فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓

• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify

- بتلقى شرح لكل هالمنصات في المجموعة اكتب فقط م الاوامر**

- [𝑠𝑜𝑢𝑟𝑐𝑒 𝑙𝑖𝑛𝑑𝑎](t.me/FH_KP)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("اوامر المجموعة"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n
  ╔═════• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •════╗

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
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("اوامر القنوات"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n
╔═══• [𝐥𝐢𝐧𝐝𝐚 𝐦𝐮𝐬𝐢𝐜](t.me/FH_KP) •═══╗\n\n 
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
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("طريقة البحث"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""مرحـبا فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓

[ بحث + اسم المطلوب ..]

مثال » بحث بحبك وحشتني

- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
@app.on_message(filters.private & command("حفظ التشغيل"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **مرحـبا فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر » ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر » ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر » ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر » ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 » تدخل البوت قناتك وترفعه مشرف\n2 » ترجع للقروب وتكتب { **/channelplay + يوزر القناة** }\n3 » مثل {**/channelplay@FH_KP**}\n4 »**اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/UUUOLC"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/LANDHLBOT?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
