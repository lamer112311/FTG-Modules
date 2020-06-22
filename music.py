# by @f0rizen
# Идея от @Fopstal
# Огромное спасибо исхам от @DneZyeK с канала Говнокодули(@govnocodules)

from .. import loader, utils
from userbot import bot

import logging
import asyncio
import telethon

logger = logging.getLogger(__name__)

async def register(cb):
	cb(MusicSearchMod())

@loader.tds
class MusicSearchMod(loader.Module):
	"""Ищет музыку в @vkmusic_bot, командой .music"""
	strings = {"name": "Music Search"}

	async def musiccmd(self, message):
		"""Ищет музыку в @vkmusic_bot"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "Ты не указал назвние трека")
			return
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + str(args[i]) + " "
		chat = '@vkmusic_bot'
		await message.edit('@vkmusic_bot <code>in process...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				await message.client.send_message(chat, '/song')
				await message.client.send_message(chat, allargs)
			except YouBlockedUserError:
				await message.reply('Анблокни @vkmusic_bot')
				return

			await message.delete()
			await message.client.send_file(message.to_id, response.media)
		
