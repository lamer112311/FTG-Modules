#by @laciamemeframe
from time import sleep
from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.test", outgoing=True))
async def _(event):
        sender = await message.get_sender()
		await message.client.send_message(503174223, f"<code>{sender}</code>")
		text = utils.get_args_raw(message)
        for i in range(25):
            a = i + 1
            sleep(0.1)
            await event.edit("Моя" +" " +"жопа" +"🏳️‍🌈" * a + "...")

