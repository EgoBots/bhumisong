from pyrogram import Client, filters
import random
from SONALI_MUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "❍ ʟᴏᴠᴇ ɪs ɪɴ ᴛʜᴇ ᴧɪʀ ʙᴜᴛ ɴᴇᴇᴅs to ᴧ ʟɪᴛᴛʟᴇ sᴘᴧʀᴋ.",
            "❍ ᴧ ɢᴏᴏᴅ sᴛᴧʀᴛ ʙᴜᴛ ᴛʜᴇʀᴇ's ʀᴏᴏᴍ ᴛᴏ ɢʀᴏᴡ.",
            "❍ ɪᴛ's ᴊᴜsᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ sᴏᴍᴇᴛʜɪɴɢ ʙᴇᴧᴜᴛɪғᴜʟ."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "❍ ᴧ sᴛʀᴏɴɢ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ɪs ᴛʜᴇʀᴇ. ᴋᴇᴇᴘ ɴᴜʀᴛᴜʀɪɴɢ ɪᴛ.",
            "❍ ʏᴏᴜ'ʜᴠ ɢᴏᴛ ᴧ ɢᴏᴏᴅ ᴄʜᴧɴᴄᴇ. ᴡᴏʀᴋ ᴏɴ ɪᴛ.",
            "❍ ʟᴏᴠᴇ ɪs ʙʟᴏssᴏᴍɪɴɢ, ᴋᴇᴇᴘ ɢᴏɪɴɢ."
        ])
    else:
        return random.choice([
            "❍ ᴡᴏᴡ ! ɪᴛ's ᴧ ᴍᴧᴛᴄʜ ᴍᴧᴅᴇ ɪɴ ʜᴇᴧᴠᴇɴ!",
            "❍ ᴘᴇʀғᴇᴄᴛ ᴍᴧᴛᴄʜ ! ᴄʜᴇʀɪsʜ ᴛʜɪs ʙᴏɴᴅ.",
            "❍ ᴅᴇsᴛɪɴᴇᴅ ᴛᴏ ʙᴇ ᴛᴏɢᴇᴛʜᴇʀ. ᴄᴏɴɢʀᴧᴛᴜʟᴧᴛɪᴏɴs!"
        ])


EVAA = [
    [
        InlineKeyboardButton(text="⊚ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ⊚", url="https://t.me/AarumiSongBot?startgroup=true"),
    ],
]


@app.on_message(filters.command("love"))
async def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = (
            f"⦿ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟᴏᴠᴇ ᴘᴇʀᴄᴇɴᴛᴧɢᴇ ⏤͟͟͞͞★ \n\n"
            f"❅ {name1} ♥️ + {name2} ♥️ = {love_percentage}%\n\n{love_message}"
        )
        await client.send_message(
            message.chat.id,
            response,
            reply_markup=InlineKeyboardMarkup(EVAA),
        )
    else:
        await client.send_message(
            message.chat.id,
            "⦿ ᴘʟᴇᴧsᴇ ᴇɴᴛᴇʀ ᴛᴡᴏ ɴᴧᴍᴇs ᴧꜰᴛᴇʀ /love ᴄᴏᴍᴍᴧɴᴅ.",
            reply_markup=InlineKeyboardMarkup(EVAA),
        )
            
