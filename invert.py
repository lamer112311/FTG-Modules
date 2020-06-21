#by @laciamemeframe
from telethon import events
import asyncio
from time import sleep


@borg.on(events.NewMessage(pattern=r"\.invert", outgoing=True))
async def _(event):
    await event.edit("Начинаем полчение данных из этого аккаунта: Операция завершится через 60 секунд")
    sleep(60)
    await event.edit("Сверяем с базой данных зоны-51: Операция завершится через 300 секунд")
    sleep(300)
    await event.edit("Отправка данных.... через 20.1 секунд")
    sleep(20.1)
    await event.edit(str(event.sender))