import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

@Client.on_message(filters.command("cat", prefix) & filters.me)
async def cat_cmd(_: Client, message: Message):
    url = "https://aws.random.cat/meow"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        image_url = data["file"]
        await client.send_photo(message.chat.id, image_url)
    else:
        await message.edit("Failed to fetch cat picture. Please try again later.")

modules_help["cat"] = {
    "cat": "Send a random cat picture",
}
