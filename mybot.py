import os
from pyrogram import Client, filters


app = Client(
        api_id = os.getenv("API_ID"),
        api_hash = os.getenv("API_HASH"),
        workdir = os.getenv("WORKDIR"),
        name = "My Bot",
        device_model = "Linux",
        app_version = "0.0.1"
)


@app.on_message(filters.command("test", prefixes="~") & filters.me)
async def test(_, msg):
    await msg.reply("Hello")


print("Let's go!")
app.run()

