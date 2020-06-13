from telethon import events, functions, types
from .. import loader, utils


def register(cb):
	cb(ReverseMod())


class ReverseMod(loader.Module):
	"""Reverse text"""

	strings = {'name': 'Reverse'}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()

	async def reversecmd(self, message):
		""".reverse text"""
		sender = await message.get_sender()
		text = utils.get_args_raw(message)
		if not text:
			await message.delete()
		await message.edit(text[::-1])