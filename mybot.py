import os
from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler


class MyBot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def _run(self):
        await self.start()

        self.me = await self.get_me()
        self.my_session = await self.export_session_string()

        await idle()
        await self.stop()

    def run_now(self):
        self.run(self._run())



app = MyBot(
        api_id = os.getenv("API_ID"),
        api_hash = os.getenv("API_HASH"),
        workdir = os.getenv("WORKDIR"),
        name = "My Bot",
        device_model = "Linux",
        app_version = "0.0.1",
        plugins = dict(root="plugins")
)


print("Let's go!")
app.run_now()
