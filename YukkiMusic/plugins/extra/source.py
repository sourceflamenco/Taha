import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USER = getenv("BOT_USER")

@app.on_message(
    command(["سورس مين","سورس","السورس","يا سورس","تايجر"])
    & ~filters.edited
)
async def taiger(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6513d3be5b9df9d8b2781.jpg",
        caption=f"""╭──★──[ƚᎥᘜᥱᖇ](https://t.me/UY_X6)──★──╮\n么 [𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓](https://t.me/UY_X6)  \n么 [Aُᥣꪔᥲꪀꪗ](http://t.me/almany_basha) \n么 [ꫀُᥣُρُ᥆ُρ](http://t.me/PW_BOB) \n么 [𝐙𝐎𝐇𝐑𝐲](http://t.me/Z0HARY) \n么[𝑀𝐸𝐷𝑜](http://t.me/JY_X6) \n╰──★──[ƚᎥᘜᥱᖇ](https://t.me/UY_X6)──★──╯ \n[𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓](https://t.me/UY_X6)""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                    InlineKeyboardButton(
                        "𝑺𝑶𝑼𝑹𝑪𝒆 𝑻𝑨𝑰𝑮𝑬𝒓", url=f"https://t.me/UY_X6")
                 ],   
                 [    
                    InlineKeyboardButton(
                        "اضف البوت ف جروبك ✨️", url=f"https://t.me/{BOT_USER}?startgroup=true")
                 ],
             ]
            ),
    )
  
