from pyrogram import Client as c, filters as f


def command(cmd):
    return f.command(cmd, prefixes="~")


@c.on_message(command("test") & f.me)
async def test(app, msg):
    await msg.reply("Hello world")

@c.on_message(command("getsession") & f.me & f.private)
async def get_session(app, msg):
    await msg.reply(app.my_session)

@c.on_message(f.mentioned)
async def mentioned(app, msg):
    if not app.afk["status"]:
        return

    if app.afk["chat_id"] != msg.chat.id:
        return

    _msg = "```AFK!```"
    if len(app.afk["message"]) > 0:
        _msg = f"```AFK: {app.afk['message']}```"

    await msg.reply(_msg)

@c.on_message(command("afk") & f.me)
async def set_afk(app, msg):
    if msg.chat.id == app.me.id:
        return

    _msg = " ".join(msg.command[1:])
    app.set_afk(True, msg.chat.id, _msg)

    await app.edit_message_text(msg.chat.id, msg.id, "```AFK!```")

@c.on_message(f.me)
def hears(app, msg):
    if app.afk["status"] and app.afk["chat_id"] == msg.chat.id:
        app.set_afk()
