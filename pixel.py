# -*- coding: utf-8 -*-

#   Friendly Telegram (telegram userbot)
#   Copyright (C) 2018-2020 The Authors

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#   если не подписан на t.me/keyzend
#   твоя мама шлюха
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import io
from PIL import Image, ImageOps
from telethon.tl.types import DocumentAttributeFilename
import logging
import random

logger = logging.getLogger(__name__)

def register(cb):
	cb(pixelerMod())


@loader.tds
class pixelerMod(loader.Module):
	"""Гавно залупное"""
	strings = {
		"name": "pixeling"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def pixelcmd(self, message):
		""".pixel <reply to photo>"""
		pixel = 3
		a = utils.get_args(message)
		if a:
			if a[0].isdigit():
				pixel = int(a[0])
				if pixel <= 0:
					pixel = 3
		
		if message.is_reply:
			reply_message = await message.get_reply_message()
			data = await check_media(reply_message)
			if isinstance(data, bool):
				await utils.answer(message, "<code>Reply to pic or stick!</code>")
				return
		else:
			await utils.answer(message, "<code>Reply to pic or stick!</code>")
			return
		
		await message.edit("pixeling...")
		file = await self.client.download_media(data, bytes)
		media = await pixeling(file, pixel)
		await message.delete()
		
		await message.client.send_file(message.to_id, media)
		
	
		

async def pixeling(file, pixel):
	img = Image.open(io.BytesIO(file))
	(x, y) = img.size
	img = img.resize((x//pixel, y//pixel), Image.BOX)
	img = img.resize((x, y), Image.BOX)
	pixel_io = io.BytesIO()
	pixel_io.name = "image.jpeg"
	img = img.convert("RGB")
	img.save(pixel_io, "JPEG", quality=100)
	pixel_io.seek(0)
	return pixel_io
	

async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.gif or reply_message.video or reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False

	if not data or data is None:
		return False
	else:
		return data