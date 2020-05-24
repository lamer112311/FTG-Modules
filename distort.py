# -*- coding: utf-8 -*-

#   Quotes module for Friendly-Telegram
#   Copyright (C) 2020 rfoxed (rf0x1d)

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
import requests

from .. import loader, utils
from PIL import Image
import requests
from datetime import datetime
from asyncio import sleep
import os
from os import remove as RemFile
from urllib.request import urlretrieve
from telethon.tl.types import DocumentAttributeFilename
import json
from requests.exceptions import ConnectionError

logger = logging.getLogger(__name__)


def register(cb):
    cb(DistortMod())


class DistortMod(loader.Module):
    """Distort a picture for fun"""

    strings = {
        "name": "Дисторт",
        "no_reply": "<code>You didn\'t reply to a message.</code>",
        "cant_distort": "<b>I can't distort that!</b>",
        "help": "<b>Reply to an image or sticker to distort it!</b>",
        "processing": "<code>Processing...</code>",
        "api_down": "<b>API Host is unreachable now. Please try again later.</b>",
        "api_error": "<b>API Error occured :)</b>",
        "invalid_token": "<b>Wrong API Token.</b>",
        "quota_expired": "<code>Your account quota has been ended *shrug*</code>",
        "no_image": "<code>Lel no image provided maaan</code>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig("API_TOKEN", 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx',
                                          "API Token for distortion.")

        self.name = self.strings['name']

    async def client_ready(self, client, db):
        self.client = client
    
    async def distortcmd(self, message):
        """Usage: .distort (optional: file/force_file/sticker)
        Sends as sticker by default
        Needs an API Token."""
        args = utils.get_args(message)
        reply = await message.get_reply_message()
        if not reply:
            return await message.edit(self.strings['no_reply'])
        
        if reply.media:
            data = await check_media(reply)
            if isinstance(data, bool):
                await message.edit(self.strings['cant_distort'])
                return
        else:
            return await message.edit(self.strings['help'])
        await message.edit(self.strings['processing'])
        path_img = await self.client.download_media(
                    reply,
                    progress_callback=progress,
        )
        image = upload_to_0x0st(path_img)
        token = self.config["API_TOKEN"]
        try:
            requested = requests.post('http://rsdev.ml/dev/distort', data={
                "token": str(token).encode("utf-8"),
                "picture": image.encode('utf-8')
            })
        except ConnectionError:
            return await message.edit(self.strings['api_down']) 
        if requested.status_code == 500:
            return await message.edit(self.strings['api_error'])
        else:
            requested = requested.json()

        try:
            urlretrieve(requested['success']['file'], 'file.png')
            await message.delete()
            if len(args) < 1 or args[0].lower() == 'sticker':
                Image.open('file.png').save('file.webp', 'webp')
                async with self.client.action(message.chat_id, 'document') as action:
                    await sleep(2)
                    await self.client.send_file(message.chat_id, 'file.webp', reply_to=reply.id, progress_callback=action.progress)
                RemFile('file.webp')
                RemFile('file.png')
                try:
                    RemFile(path_img)
                except:
                    pass
            else:
                test = args[0].lower()
                if test == 'file':
                    async with self.client.action(message.chat_id, 'document') as action:
                        await self.client.send_file(message.chat_id, 'file.png', reply_to=reply.id, progress_callback=action.progress)
                    RemFile('file.png')
                    try:
                        RemFile(path_img)
                    except:
                        pass
                elif test == 'force_file':
                    async with self.client.action(message.chat_id, 'document') as action:
                        await sleep(2)
                        await self.client.send_file(message.chat_id, 'file.png', reply_to=reply.id,
                                                force_document=True, progress_callback=action.progress)
                    RemFile('file.png')
                    try:
                        RemFile(path_img)
                    except:
                        pass
        except KeyError:
            if requested['202']:
                if requested['202'] == 'INVALID TOKEN':
                    return await message.edit(self.strings['invalid_token'])
            elif requested['403']:
                if requested['403'] == 'NO_IMAGE_PROVIDED':
                    return await message.edit(self.strings['no_image'])
            elif requested['228']:
                if requested['228'] == "NO_MORE_QUOTA":
                    return await message.edit(self.strings['quota_expired'])


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

def upload_to_0x0st(path):
    req = requests.post('https://0x0.st', files={'file': open(path, 'rb')})
    os.remove(path)
    return req.text

def progress(current, total):
	""" Logs the download progress """
	logger.info("Downloaded %s of %s\nCompleted %s", current, total,
			  (current / total) * 100)