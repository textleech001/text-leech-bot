from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserDeactivated, UserDeactivatedBan, ChatWriteForbidden
from info import info
from info import BOT_TOKEN, BOT_USERNAME, API_ID, API_HASH
from utils import temp
from database import Database

db = Database("database.db")
db.create_table()
#Insert a user (commented out or removed)
db.insert_user(1, "username")
user = db.get_user(1)
print(user)
db.close()

app2 = Client(
    "Text-Leech-Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

@app2.on_message(filters.command("start") & filters.private)
async def start_command(_, message: Message):
    await message.reply_text(
        text=f"Hi {message.from_user.mention}!\nI'm a text leech bot.\n\n"
        f"Send me any message/file and I'll send you the text.\n\n"
        f"Made with ❤️ by @KingProject24",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source Code", url="https://github.com/textleech001/text-leech-bot"),
                    InlineKeyboardButton("Developer", url="https://t.me/KingProject24")
                ]
            ]
        )
    )

@app2.on_message(filters.text & filters.private)
async def leech_text(_, message: Message):
    await message.reply_text(text=message.text)

@app2.on_message(filters.document & filters.private)
async def leech_doc(_, message: Message):
    await message.reply_text(text=message.document.file_id)

@app2.on_message(filters.audio & filters.private)
async def leech_audio(_, message: Message):
    await message.reply_text(text=message.audio.file_id)

app2.start()
app2.idle()
