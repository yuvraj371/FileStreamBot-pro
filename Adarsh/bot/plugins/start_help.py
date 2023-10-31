# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

buttonz = ReplyKeyboardMarkup(
    [
        ["start⚡️", "help📚", "DC"],
        ["Subscribe ❤️", "ping📡", "status📊", "maintainers😎"]
    ],
    resize_keyboard=True
)

@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined:**\n\n__My New Friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Started Your Bot!!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="Sorry, you are banned from using me. Contact the Developer.",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/68259e3c723b935e22e69.jpg",
                caption="**Join UPDATES CHANNEL to use this Bot!**\n\n__Due to overload, only Channel Subscribers can use the Bot.__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="Something went wrong. Contact me [Support](https://t.me/Infinity_XBotz_support).",
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz)

@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined **\n\n__My New Friend__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sorry Sir, You are Banned from using me. Contact the Developer</i>",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                caption="**JOIN SUPPORT GROUP TO USE ME!**\n\n__Due to overload, only Channel Subscribers can use the Bot.__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Something went wrong. Contact my [Support](https://t.me/Infinity_XBotz_support).**",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="<b> Send me any file or video and I will provide you with a streamable link and a download link.</b>\n\n<b>I also support Channels. Add me to your Channel and send any media files to see the magic!</b>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                 InlineKeyboardButton("💁‍♂️ Owner", url="https://telegram.me/Madhuri_niranjan"),
                 InlineKeyboardButton("💥 Updates channel", url="https://Infinity_XBotz")
              ],[
                 Inlinekeyboardbutton("Support group", url="https://telegram.me/Infinity_XBotz_support"),
                 Inlinekeyboardbutton("Movie group", url="https://t.me/+Qn6fthcb7wI0ZTk1")
            ]
        )
                )
            
