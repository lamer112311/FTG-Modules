from telethon import events, functions, types
from .. import loader, utils
import asyncio

def register(cb):
	cb(UpdownMod())


class UpdownMod(loader.Module):
	""".updown текст."""

	strings = {'name': 'UpDown txt'}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client

	async def updowncmd(self, e):
		text = utils.get_args_raw(e)
		text = text.replace("а", "ɐ")
		text = text.replace("б", "ƍ")
		text = text.replace("в", "ʚ")
		text = text.replace("г", "ɹ")
		text = text.replace("д", "ɓ")
		text = text.replace("е", "ǝ")
		text = text.replace("ё", "ǝ̤")
		text = text.replace("з", "ε")
		text = text.replace("й", "n̯")
		text = text.replace("к", "ʞ")
		text = text.replace("л", "v")
		text = text.replace("м", "w")
		text = text.replace("п", "u")
		text = text.replace("р", "d")
		text = text.replace("с", "ɔ")
		text = text.replace("т", "ɯ")
		text = text.replace("у", "ʎ")
		text = text.replace("ф", "ȸ")
		text = text.replace("ц", "ǹ")
		text = text.replace("ч", "Һ")
		text = text.replace("ш", "m")
		text = text.replace("щ", "m")
		text = text.replace("ъ", "q")
		text = text.replace("ы", "ıq")
		text = text.replace("ь", "q")
		text = text.replace("э", "є")
		text = text.replace("ю", "oı")
		text = text.replace("я", "ʁ")

		text = text.replace("А", "ɐ")
		text = text.replace("Б", "ƍ")
		text = text.replace("В", "ʚ")
		text = text.replace("Г", "ɹ")
		text = text.replace("Д", "ɓ")
		text = text.replace("Е", "ǝ")
		text = text.replace("Ё", "ǝ̤")
		text = text.replace("З", "ε")
		text = text.replace("Й", "n̯")
		text = text.replace("К", "ʞ")
		text = text.replace("Л", "v")
		text = text.replace("М", "w")
		text = text.replace("П", "u")
		text = text.replace("Р", "d")
		text = text.replace("С", "ɔ")
		text = text.replace("Т", "ɯ")
		text = text.replace("У", "ʎ")
		text = text.replace("Ф", "ȸ")
		text = text.replace("Ц", "ǹ")
		text = text.replace("Ч", "Һ")
		text = text.replace("Ш", "m")
		text = text.replace("Щ", "m")
		text = text.replace("Ъ", "q")
		text = text.replace("Ы", "ıq")
		text = text.replace("Ь", "q")
		text = text.replace("Э", "є")
		text = text.replace("Ю", "oı")
		text = text.replace("Я", "ʁ")

		await e.edit(text[::-1])
