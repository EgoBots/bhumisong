from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀᴇᴘᴏs ❃</u>
 
✼ ʀᴇᴘᴏ ᴛᴏ ɴʜɪ ᴍɪʟᴇɢᴧ ʙʜᴧɪ ʏʜᴧ
 
❉ ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ

✼ || ᴄᴏɴᴛᴧᴄᴛ : [ㅤㅤ- к ᴧ ʀ м ᴧ › ᴏᴘ ⇢](https://t.me/Swagger_Soul) ||
 
❊ ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⊚  ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ  ⊚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("⌯ ᴜᴘᴅᴧᴛᴇ ⌯", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("⌯ sᴜᴘᴘᴏʀᴛ ⌯", url="https://t.me/AarumiChat"),
          ],
[
InlineKeyboardButton("⌯ ᴍᴧɪɴ ʙᴏᴛ ⌯", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/5fck1b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
