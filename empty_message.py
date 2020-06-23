#by @laciamemeframe
from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.empty", outgoing=True))
async def _(event):
    await event.edit("&NoBreak;\n"*2000)