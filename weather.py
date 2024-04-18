from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(filters.command(["w", "aw"], prefix) & filters.me)
async def weather_cmd(_: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("<b>City?</b>")
        return
    
    city = message.command[1].lower().replace(" ", "%20")
    r = requests.get(f"https://wttr.in/{city}?0?q?T")
    
    await message.edit(f"<b>City: {r.text}</b>")

modules_help["weather"] = {
    "w [city]": "Print ASCII weather in your city.",
}
