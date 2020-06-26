#by @laciamemeframe
from .. import loader, utils
import logging
import requests

logger = logging.getLogger(__name__)

def register(cb):
	cb(wMod())

@loader.tds
class wMod(loader.Module):
	"""Погода by wttr.in"""
	strings = {'name': 'Погода'}

	async def client_ready(self, client, db):
		self.client = client

	async def wcmd(self, message):
		""".w <город> либо просто .w посмотреть погоду в локации где работает юзербот"""
		message.edit("<b>Погода by wttr.in</b>")
		city = utils.get_args(message)
		await message.edit("Отправка данных на сервер wttr.in...")
		r = requests.get("https://wttr.in/" + str(city) + "?format=%l:+%c+%t,+%w+%m")
		await message.edit(r.text)


