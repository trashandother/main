from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix
from utils.db import db

import requests
import re

status = db.get("autoshort", "status", True)
is_runned = filters.create(lambda _, __, ___: status)

url_pattern = (
    r"^(?:http|https)://"
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
    r"localhost|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$"
)

@Client.on_message(is_runned  & filters.me)
async def autoshort_handler(_: Client, message: Message):
    links = re.findall(pattern, message.text)
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
        
        text = message.text.replace(link, r.text)
        
    await message.edit(text)

@Client.on_message(filters.command(["autoshort", "aush", "ah"], prefix) & filters.me)
async def autoshort_cmd(_: Client, message: Message):
    await message.edit(f"<b>[AutoShort] Your links are safe now!</b>")
    db.set("autoshort", "status", True)
    
@Client.on_message(filters.command(["unautoshort", "unaush", "unah"], prefix) & filters.me)
async def unautoshort_cmd(_: Client, message: Message):
    await message.edit(f"<b>[AutoShort] I'm disabled ;((</b>")
    db.set("autoshort", "status", False)

modules_help["AutoShort"] = {
    "autoshort": "enable autoshort",
    "unautoshort": "disable autoshort"
}
