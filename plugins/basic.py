from pyrogram import Client as c, filters as f


@c.on_message(f.command("test", prefixes="~") & f.me)
async def test(app, msg):
    await msg.reply("Hello world")

@c.on_message(f.command("getsession", prefixes="~") & f.me & f.private)
async def get_session(app, msg):
    await msg.reply(app.my_session)
