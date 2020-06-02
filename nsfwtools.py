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
import ast

logger = logging.getLogger(__name__)


def register(cb):
    cb(NSFWMod())


class NSFWMod(loader.Module):
    """NSFW Tools for detect and censore nsfw"""

    strings = {
        "name": "NSFW Tools",
        "no_reply": "<code>You didn\'t reply to a message.</code>",
        "cant_censore": "<b>I can't censore that!</b>",
        "help": "<b>Reply to an image or sticker to censore it!</b>",
        "processing": "<code>Processing...</code>",
        "api_down": "<b>API Host is unreachable now. Please try again later.</b>",
        "api_error": "<b>API Error occured :)</b>",
        "invalid_token": "<b>Wrong API Token.</b>",
        "quota_expired": "<code>Your account quota has been ended *shrug*</code>",
        "no_image": "<code>Lel no image provided maaan</code>",
        "no_nsfw": "No NSFW has been found on image",
        "cannot_resolve_error": "<b>Cannot resovle an error.\nServer returned:</b> <code>{}</code>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig("API_TOKEN", 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx',
                                          "API Token for NSFW API.")

        self.name = self.strings['name']

    async def client_ready(self, client, db):
        self.client = client
    
    async def nsfwdetectcmd(self, message):
        """Usage: .nsfwdetect
        Needs an API Token."""
        reply = await message.get_reply_message()
        if not reply:
            return await message.edit(self.strings['no_reply'])
        
        if reply.media:
            data = await check_media(reply)
            if isinstance(data, bool):
                await message.edit(self.strings['cant_censore'])
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
            requested = requests.post('http://rsdev.ml/dev/nude', data={
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
            data = requested['success']['result']
            if data["label"] == "NO_NSFW":
                return await utils.answer(message, self.strings["no_nsfw"])
            msg = ""
            score = "Low"
            if data["score"] < 0.2:
            	score = "Very low"
            elif data["score"] > 0.5:
                score = "Medium"
            elif data["score"] > 0.7:
            	score = "High"
            elif data["score"] > 0.9:
            	score = "Very high"
            
            if data["label"] == "BELLY":
            	label = "Exposed belly"
            elif data["label"] == "BUTTOCKS":
            	label = "Exposed buttocks"
            elif data["label"] == "F_BREAST":
            	label = "Exposed female breast"
            elif data["label"] == "M_BREAST":
            	label = "Exposed male breast"
            elif data["label"] == "F_GENITALIA":
            	label = "Exposed female genitalia"
            elif data["label"] == "M_GENITALIA":
            	label = "Exposed male genitalia"
            
            msg += "NSFW Tools\n\n"
            msg += "Score: {}({})\n".format(score, data["score"])
            msg += "Label: {}\n".format(label)
            msg += "Bounding box: {}".format(str(data["box"]))
            await utils.answer(message, msg)
        except KeyError:
            if requested.get('202'):
                if requested['202'] == 'INVALID TOKEN':
                    return await utils.answer(message, self.strings['invalid_token'])
            elif requested.get('403'):
                if requested['403'] == 'NO_IMAGE_PROVIDED':
                    return await utils.answer(message, self.strings['no_image'])
            elif requested.get('228'):
                if requested['228'] == "NO_MORE_QUOTA":
                    return await utils.answer(message, self.strings['quota_expired'])


    async def nsfwcensorecmd(self, message):
            """Usage: .nsfwcensore
            Needs an API Token."""
            reply = await message.get_reply_message()
            if not reply:
                return await message.edit(self.strings['no_reply'])
            
            if reply.media:
                data = await check_media(reply)
                if isinstance(data, bool):
                    await message.edit(self.strings['cant_censore'])
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
                requested = requests.post('http://rsdev.ml/dev/nude/censore', data={
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
                with open("file.png", "rb") as file:
                    await utils.answer(message, file)
                RemFile("file.png")
            except KeyError:
                if requested.get('202'):
                    if requested['202'] == 'INVALID TOKEN':
                        return await message.edit(self.strings['invalid_token'])
                elif requested.get('403'):
                    if requested['403'] == 'NO_IMAGE_PROVIDED':
                        return await message.edit(self.strings['no_image'])
                elif requested.get('228'):
                    if requested['228'] == "NO_MORE_QUOTA":
                        return await message.edit(self.strings['quota_expired'])
                else:
                    err = self.strings['cannot_resolve_error'].format(str(requested))
                    return await utils.answer(message, err)


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
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