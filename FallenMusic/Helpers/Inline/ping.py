import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    url="https://te.legra.ph/file/21fff815368bc57386c27.jpg"
                )
            ]
        ]
    )
