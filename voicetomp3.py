# by @laciamemeframe

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
	cb(Mp3Mod())
class Mp3Mod(loader.Module):
	"""Конвертирование голосовых сообщений в mp3"""

	strings = {'name': 'ВойсТуМп3'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def mp3cmd(self, message):
		""".mp3 <Ответить на голосовое сообщение>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Ответь на голосовое сообщение")
			return
		try:
			voice = reply.voice
		except:
			await message.edit("Ответить нужно на голосовое сообщение!")
		chat = '@mp3toolsbot'
		await message.edit('@mp3toolsbot <code>in обработка...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=257113201))
				blank = conv.wait_event(events.NewMessage(incoming=True, from_users=257113201))
				await message.client.send_file(chat, voice)
				blank = await blank
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй</code> @mp3toolsbot')
				return
			await message.delete()
			await message.client.send_file(message.to_id, response.media)
	
	async def infomp3cmd(self, message):
		""".infomp3 ответить на файл mp3"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Ответь на файл mp3")
			return
		try:
			media = reply.media
		except:
			await message.edit("Показывает информацию только mp3 файлов")
			return
		chat = '@mp3toolsbot'
		await message.edit('@mp3toolsbot <code>обработка...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=257113201))
				blank = conv.wait_event(events.NewMessage(incoming=True, from_users=257113201))
				await message.client.send_file(chat, media)
				blank = await blank
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй бота</code> @mp3toolsbot')
				return
			await message.delete()
			await message.client.send_message(message.to_id, response.text)	

	async def mp3voicecmd(self, message):
		""".mp3voice ответить на файл mp3"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Ответь на файл mp3")
			return
		try:
			media = reply.media
		except:
			await message.edit("Конвертирует mp3 в голосовое сообщение")
			return
		chat = '@convertkonbot'
		await message.edit('@convertkonbot <code>обработка...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=503828089))
				await message.client.send_file(chat, media)
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй бота</code> @convertkonbot')
				return
			await message.delete()
			await message.client.send_file(message.to_id, response.voice)			