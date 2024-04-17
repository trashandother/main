import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

@Client.on_message(filters.command("rndquote", prefix) & filters.me)
async def randomquote_cmd(_: Client, message: Message):
    url = "https://api.quotable.io/random"
    
    response = requests.get(url)
    data = response.json()
    
    content = data["content"]
    author = data["author"]
    
    await message.edit(f"\"{content}\" - {author}")

modules_help["randomquote"] = {
    "rndquote": "Display a random quote",
}
