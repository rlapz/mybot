#!/bin/env python3


import os
from pyrogram import Client, filters, idle
import config


class MyBot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.run(self._run())

    async def _run(self):
        await self.start()

        self.me = await self.get_me()
        self.my_session = await self.export_session_string()

        await idle()
        await self.stop()


if __name__ == "__main__":
    print("Let's go!")
    MyBot(
        api_id = config.api_id,
        api_hash = config.api_hash,
        workdir = config.workdir,
        name = "My Bot",
        device_model = "Linux",
        app_version = "0.0.1",
        plugins = dict(root="plugins")
    )
