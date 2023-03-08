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

@app.on_message(filters.regex("^تعطيل صراحه$") & filters.group)
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
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تعطيل صراحه")
        
@app.on_message(filters.regex("^تفعيل صراحه$") & filters.group)
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
        await message.reply_text(f"- بواسطة {message.from_user.mention}\n- تم تفعيل صراحه")        
        
        
@app.on_message(filters.regex("^صراحه$") & filters.group)
def searchMusic(c: Client, m: Message):
        ch = m.chat.id
        if ch in disable_cut:
          return
        txt = [
            "**صراحه «» صوتك حلوة؟",
"صراحه «» التقيت الناس مع وجوهين ⦁ ",
"صراحه «» شيء وكنت تحقق اللسان ⦁ ",
"صراحه «» أنا شخص ضعيف عندما ⦁ ",
"صراحه «» هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف ⦁ ",
"صراحه «» يدل على أن الكذب مرات تكون ضرورية شي ⦁ ",
"صراحه «» أشعر بالوحدة على الرغم من أنني تحيط بك كثيرا ⦁ ",
"صراحه «» كيفية الكشف عن من يكمن عليك ⦁ ",
"صراحه «» إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة ⦁ ",
"صراحه «» أشجع شيء حلو في حياتك ⦁ ",
"صراحه «» طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة توافق ⦁ ",
"صراحه «» كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض ⦁ ",
"صراحه «» التغيير العادي عندما يكون الشخص الذي يحبه ⦁ ",
"صراحه «» المواقف الصعبة تضعف لك ولا ترفع ⦁ ",
"صراحه «» نظرة و يفسد الصداقة ⦁ ",
"صراحه «» ‏‏إذا أحد قالك كلام سيء بالغالب وش تكون ردة فعلك ⦁ ",
"صراحه «» شخص معك بالحلوه والمُره ⦁ ",
"صراحه «» ‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف ⦁ ",
"صراحه «» تأخذ بكلام اللي ينصحك ولا تسوي اللي تبي ⦁ ",
"صراحه «» وش تتمنى الناس تعرف عليك ⦁ ",
"صراحه «» ابيع المجرة عشان ⦁ ",
"صراحه «» أحيانا احس ان الناس ، كمل ⦁ ",
"صراحه «» مع مين ودك تنام اليوم ⦁ ",
"صراحه «» صدفة العمر الحلوة هي اني ⦁ ",
"صراحه «» الكُره العظيم دايم يجي بعد حُب قوي تتفق ⦁ ",
"صراحه «» صفة تحبها في نفسك ⦁ ",
"صراحه «» ‏الفقر فقر العقول ليس الجيوب  ، تتفق ⦁ ",
"صراحه «» تصلي صلواتك الخمس كلها ⦁ ",
"صراحه «» ‏تجامل أحد على راحتك ⦁ ",
"صراحه «» اشجع شيء سويتة بحياتك ⦁ ",
"صراحه «» وش ناوي تسوي اليوم ⦁ ",
"صراحه «» وش شعورك لما تشوف المطر ⦁ ",
"صراحه «» غيرتك هاديه ولا تسوي مشاكل ⦁ ",
"صراحه «» ما اكثر شي ندمن عليه ⦁ ",
"صراحه «» اي الدول تتمنى ان تزورها ⦁ ",
"صراحه «» متى اخر مره بكيت ⦁ ",
"صراحه «» تقيم حظك من عشره ⦁ ",
"صراحه «» هل تعتقد ان حظك سيئ ⦁ ",
"صراحه «» شـخــص تتمنــي الإنتقــام منـــه ⦁ ",
"صراحه «» كلمة تود سماعها كل يوم ⦁ ",
"صراحه «» *هل تُتقن عملك أم تشعر بالممل ⦁ ",
"صراحه «» هل قمت بانتحال أحد الشخصيات لتكذب على من حولك ⦁ ",
"صراحه «» متى اخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر ⦁ ",
"صراحه «» ما هو اسوأ خبر سمعته بحياتك ⦁ ",
"‏صراحه «» هل جرحت شخص تحبه من قبل  ⦁ ",
"صراحه «» ما هي العادة التي تُحب أن تبتعد عنها ⦁ ",
"‏صراحه «» هل تحب عائلتك ام تكرههم ⦁ ",
"‏صراحه «» من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم ⦁ ",
"‏صراحه «» هل خجلت من نفسك من قبل ⦁ ",
"‏صراحه «» ما هو ا الحلم  الذي لم تستطيع ان تحققه ⦁ ",
"‏صراحه «» ما هو الشخص الذي تحلم به كل ليلة ⦁ ",
"‏صراحه «» هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ ⦁ ",
"‏صراحه «» هل قمت بالبكاء أمام من تُحب ⦁ ",
"‏صراحه «» ماذا تختار حبيبك أم صديقك ⦁ ",
"‏صراحه «» هل حياتك سعيدة أم حزينة ⦁ ",
"صراحه «» ما هي أجمل سنة عشتها بحياتك ⦁ ",
"‏صراحه «» ما هو عمرك الحقيقي ⦁ ",
"‏صراحه «» ما اكثر شي ندمن عليه ⦁ ",
"صراحه    ما هي أمنياتك المُستقبلية ⦁ ‏",
"صراحه «» هل قبلت فتاه ⦁ ",
        ]
        word = random.choice(txt)
        m.reply_text(f"- {m.from_user.mention}\n{word}")
