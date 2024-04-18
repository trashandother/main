from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.db import db

import requests
import re

status = db.get("custom.autoshort", "status", False)
is_runned = filters.create(lambda _, __, ___: status)

pattern = r'(?:https?://)?(?:www\.)?(?:[\w-]+\.)*[\w-]+\.[\w/.]+'

@Client.on_message(is_runned & filters.me)
async def autoshort_handler(_: Client, message: Message):
    links = re.findall(pattern, message.text)
    text = message.text
    print(links)
    for link in links:
        short = requests.post(
            "https://gg.gg/create",
            data={
                "custom_path": None,
                "use_norefs": 0,
                "long_url": link,
                "app": "site",
                "version": "0.1",
            },
        )
        print(short.text)
        text = text.replace(link, short.text)
    if text != message.text:
        await message.edit(text)


@Client.on_message(filters.command(["autoshort", "aush", "ah"], prefix) & filters.me)
async def autoshort(_: Client, message: Message):
    await message.edit(f"<b>[AutoShort] Your links are safe now!</b>")
    db.set("custom.autoshort", "status", True)
    
@Client.on_message(filters.command(["unautoshort", "unaush", "unah"], prefix) & filters.me)
async def unautoshort(_: Client, message: Message):
    await message.edit(f"<b>[AutoShort] I'm disabled ;((</b>")
    db.set("custom.autoshort", "status", False)

modules_help["autoshort"] = {
    "autoshort": "enable autoshort",
    "unautoshort": "disable autoshort",
}
