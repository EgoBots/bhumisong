from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡєʟᴄᴏϻє ᴛᴏ ᴛєᴧϻ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀєᴘσs ❃</u>
 
✼ ʀєᴘᴏ ᴛᴏ ηʜɪ ϻɪʟєɢᴧ ʙʜᴧɪ ʏʜᴧ
 
❉ ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ

✼ || [ㅤㅤ- к ᴧ ʀ м ᴧ › ᴏᴘ ⇢](https://t.me/Swagger_Soul) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("⌯ ᴜᴘᴅᴧᴛᴇ ⌯", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("⌯ sᴜᴘᴘᴏʀᴛ ⌯", url="https://t.me/AarumiChat"),
          ],
[
InlineKeyboardButton("⌯ ϻᴧɪη ʙσᴛ ⌯", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kbi6t5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
