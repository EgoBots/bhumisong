import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"❖ ᴇʀʀᴏʀ : {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "❖ ᴘʟᴇᴧsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴧ ᴍᴇᴅɪᴧ ᴛᴏ ᴜᴘʟᴏᴧᴅ ᴏɴ ᴄᴧᴛʙᴏx"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("ᴘʟᴇᴧsᴇ ᴘʀᴏᴠɪᴅᴇ ᴧ ᴍᴇᴅɪᴧ ғɪʟᴇ ᴜɴᴅᴇʀ 200 MB")

    try:
        text = await message.reply("❍ ᴘʀᴏᴄᴇssɪɴɢ...")

        async def progress(current, total):
            try:
                await text.edit_text(f"❍ ᴅᴏᴡɴʟᴏᴧᴅɪɴɢ... {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("❍ ᴜᴘʟᴏᴧᴅɪɴɢ ᴛᴏ ᴄᴧᴛʙᴏx...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"❖ | [ʏᴏᴜʀ ᴄᴧᴛʙᴏx ʟɪɴᴋ]({upload_path}) | ❖",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "ʏᴏᴜʀ ᴄᴧᴛʙᴏx ʟɪɴᴋ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"❖ ᴧɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴜᴘʟᴏᴧᴅɪɴɢ ʏᴏᴜʀ ғɪʟᴇ\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"❖ | ғɪʟᴇ ᴜᴘʟᴏᴧᴅ ғᴧɪʟᴇᴅ\n\n<i>❍ ʀᴇᴧsᴏɴ : {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass
