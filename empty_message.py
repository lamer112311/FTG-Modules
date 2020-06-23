#by @laciamemeframe
from telethon import events
import asyncio
from time import sleep


@borg.on(events.NewMessage(pattern=r"\.empty", outgoing=True))
async def _(event):
    await event.delete()
    sleep(0.1)
    await event.respond("&NoBreak;\n"*2000)