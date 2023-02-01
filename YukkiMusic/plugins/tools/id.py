from pyrogram import Client, filters
from pyrogram.types import Message
from strings.filters import command
from YukkiMusic import app

def get_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "contact",
            "dice",
            "poll",
            "location",
            "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_message(command(["ايدي","ستكر","/id"]))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>آيدي الدردشة</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b>تم الرد على معرف المستخدم</b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_id(message.reply_to_message)
        else:
            _id += "<b>آيدي المستخدم</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)

@app.on_message(filters.command('mute'))
def writemuted(app,msg):
    command = msg.command
    chat_id = msg.chat.id
    print(command[0])
    if command[0] == 'mute':
        desk.sadd('mutedata',chat_id)
        msg.reply('nuted')
        
@app.on_message(filters.command('unmute'))
def writemuted(app,msg):
    command = msg.command
    chat_id = msg.chat.id
    if command[0] == 'unmute':
        desk.srem('mutedata',chat_id)
        msg.reply('unmuted')
@app.on_message(filters.text)
def delet_message(app,msg):
    chat_id = msg.chat.id
    message_id = msg.id
    if str(chat_id) in desk.smembers('mutedata'):
        app.delete_messages(chat_id,message_ids=message_id)
    words= ['desk','deskram','rico','ali','ali atia']
    filll = msg.text
    if filll in words:
        app.delete_messages(chat_id,message_ids=message_id)
