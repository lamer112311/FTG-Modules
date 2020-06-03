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

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import io
from os import remove as DelFile
import urllib.request
from PIL import Image
from asyncio import sleep
from telethon.tl.types import InputStickerSetShortName
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.errors import StickersetInvalidError
import math

logger = logging.getLogger(__name__)


def register(cb):
    cb(KangMod())


@loader.tds
class KangMod(loader.Module):
    """🏳️‍🌈Будь крутым! Имей свой анал со стикерами, блэкджеком и шлюхами🏳️‍🌈"""
    strings = {
        "name": "🏳️‍🌈Пизделка стикеров🏳️‍🌈",
        "silent_mode_cfg_doc": "Если этот параметр отключен, ваш пользовательский бот будет редактировать 🏳️‍🌈гейское🏳️‍🌈 сообщение на каждом шаге (недавние изменения) (вкл / выкл)",
        "pack_name_cfg_doc": "Userbot pack name.\n%username% - your username\n%packNumber% - number of pack.",
        "preparing_msg": "<code>🏳️‍🌈Готовимся в ебле🏳️‍🌈...</code>",
        "unsupported_err": "<b>🏳️‍🌈Такой ебли не существует🏳️‍🌈!</b>",
        "reply_err": "<b>🏳️‍🌈Харкни на фото/стикер/документ🏳️‍🌈</b>",
        "gettingType_msg": "<code>🏳️‍🌈Получение типа стикера🏳️‍🌈...</code>",
        "image_kanging_msg": "<code>🏳️‍🌈 Наклейка с изображением анала друга🏳️‍🌈...</code>",
        "animated_kanging_msg": "<code>🏳️‍🌈Забрасываем в живое очко🏳️‍🌈...</code>",
        "pack_notExist": "🏳️‍🌈Стикер пак doesn\'t exist, делая новый🏳️‍🌈...",
        "switching_msg": "<code>Switching to Pack {} due to insufficient space...</code>"
        "added_to_different_msg": "🏳️‍🌈Стикер добавлен в другой пакет🏳️‍🌈!" +
            "This Pack is Newly created! Your pack can be found <a href=\"{}\">here</a> \n " +  # noqa: E131
            "<b>🏳️‍🌈Это сообщение должно быть уничтожено за 5 секунд🏳️‍🌈.</b>",
        "added_msg": "Sticker added! Your pack can be found <a href=\"{}\">here</a> \n" +
            "<b>🏳️‍🌈Это сообщение должно быть уничтожено за 5 секунд🏳️‍🌈.</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig("silent_mode", "off", lambda: self.strings["silent_mode_cfg_doc"],
                                          "pack_name", '%username%\'s 🏳️‍🌈 %packNumber%',
                                          lambda: self.strings["pack_name_cfg_doc"])

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def kangcmd(self, message):
        """🏳️‍🌈Забрасывай в анал свой крючок🏳️‍🌈!
        использовать: .kang ответить на стикер/документ/фото и можно выбрать эмодзи для стикера
        🏳️‍🌈Если анал doesn\'t он будет создан автоматически🏳️‍🌈.
        """
        user = await self.client.get_me()
        if not user.username:
            user.username = user.first_name
        reply = await message.get_reply_message()
        photo = None
        emojibypass = False
        is_anim = False
        emoji = ""
        silent_mode = self.config['silent_mode']
        if silent_mode != "on":
            await utils.answer(message, self.strings('preparing_msg',
                                                     message))
        if reply and reply.media:
            try:
                if reply.photo:
                    photo = io.BytesIO()
                    photo = await self.client.download_media(reply.photo, photo)
                elif reply.file:
                    if reply.file.mime_type == "application/x-tgsticker":
                        await self.client.download_file(reply.media.document, 'AnimatedSticker.tgs')
                        try:
                            emoji = reply.media.document.attributes[0].alt
                        except AttributeError:
                            emoji = reply.media.document.attributes[1].alt
                        emojibypass = True
                        is_anim = True
                        photo = 1
                    else:
                        photo = io.BytesIO()
                        await self.client.download_file(reply.media.document, photo)

                    # For kanging other sticker
                        if reply.sticker:
                            emoji = reply.file.emoji
                            emojibypass = True
                else:
                    await utils.answer(message, self.strings('unsupported_err',
                                                             message))
                    return
            except AttributeError:
                photo = io.BytesIO()
                photo = await self.client.download_media(reply.photo, photo)
                try:
                    emoji = reply.media.document.attributes[1].alt
                    emojibypass = True
                except AttributeError:
                    emojibypass = False
        else:
            await utils.answer(message, self.strings('reply_err',
                                                     message))
            return

        if silent_mode != "on":
            await utils.answer(message, self.strings('gettingType_msg',
                                                     message))

        if photo:
            splat = message.text.split()
            if not emojibypass or not emoji:
                emoji = "🤔"
            pack = 1
            if len(splat) == 3:
                pack = splat[2]  # User sent both
                emoji = splat[1]
            elif len(splat) == 2:
                if splat[1].isnumeric():
                    pack = int(splat[1])
                else:
                    emoji = splat[1]

            packname = f"a{user.id}_by_{user.username}_{pack}"
            packnick = self.config['pack_name'].replace('%username%',
                                                        f'@{user.username}').replace("%packNumber%",
                                                                                     str(pack))
            cmd = '/newpack'
            file = io.BytesIO()

            if not is_anim:
                image = await resize_photo(photo)
                file.name = "sticker.png"
                image.save(file, "PNG")
                if silent_mode != "on":
                    await utils.answer(message, self.strings('image_kanging_msg',
                                                             message))
            else:
                packname += "_anim"
                packnick += " animated"
                cmd = '/newanimated'
                if silent_mode != "on":
                    await utils.answer(message, self.strings('animated_kanging_msg',
                                                             message))
            try:
                response = await self.client(GetStickerSetRequest(
                    stickerset=InputStickerSetShortName(
                        short_name = packname
                    )
                ))
            except StickersetInvalidError:
                response = None

            if response is not None:
                async with self.client.conversation('Stickers') as conv:
                    await conv.send_message('/addsticker')
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message(packname)
                    x = await conv.get_response()
                    mtext = x.text
                    while '120' in mtext:
                        pack += 1
                        packname = f"a{user.id}_by_{user.username}_{pack}"
                        packnick = self.config['pack_name'].replace('%username%',
                                                                    f'@{user.username}').replace("%packNumber%",  # noqa: E128
                                                                                                str(pack))
                        if silent_mode != "on":
                            await utils.answer(message, self.strings('switching_msg', message)\
                                .format(str(pack)))
                        await conv.send_message(packname)
                        x = await conv.get_response()
                        mtext = x.text
                        if x.text == "Invalid pack selected." or x.text == "Не выбран набор стикеров.":
                            await conv.send_message(cmd)
                            await conv.get_response()
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await conv.send_message(packnick)
                            await conv.get_response()
                            await self.client.send_read_acknowledge(conv.chat_id)
                            if is_anim:
                                await conv.send_file('AnimatedSticker.tgs', force_document=True)
                                DelFile('AnimatedSticker.tgs')
                            else:
                                file.seek(0)
                                await conv.send_file(file, force_document=True)
                            await conv.get_response()
                            await conv.send_message(emoji)
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            await conv.send_message("/publish")
                            if is_anim:
                                await conv.get_response()
                                await conv.send_message(f"<{packnick}>")
                            await conv.get_response()
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await conv.send_message("/skip")
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            await conv.send_message(packname)
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            await self.client.send_read_acknowledge(conv.chat_id)
                            await utils.answer(message,
                                        self.strings('added_to_different_msg', message)\
                                            .format(  # noqa: E127
                                            f"t.me/addstickers/{packname}"
                                        ))
                            await sleep(5)
                            await message.delete()
                            return
                    if is_anim:
                        await conv.send_file('AnimatedSticker.tgs',
                                            force_document=True)  # noqa: E128
                        DelFile('AnimatedSticker.tgs')
                    else:
                        file.seek(0)
                        await conv.send_file(file, force_document=True)
                    await conv.get_response()
                    await conv.send_message(emoji)
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message('/done')
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
            else:
                if silent_mode != "on":
                    await utils.answer(message, self.strings('pack_notExist',
                                                             message))
                async with self.client.conversation('Stickers') as conv:
                    await conv.send_message(cmd)
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message(packnick)
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
                    if is_anim:
                        await conv.send_file('AnimatedSticker.tgs',
                                            force_document=True)  # noqa: E128
                        DelFile('AnimatedSticker.tgs')
                    else:
                        file.seek(0)
                        await conv.send_file(file, force_document=True)
                    await conv.get_response()
                    await conv.send_message(emoji)
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message("/publish")
                    if is_anim:
                        await conv.get_response()
                        await conv.send_message(f"<{packnick}>")
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message("/skip")
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message(packname)
                    await self.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await self.client.send_read_acknowledge(conv.chat_id)
            await utils.answer(message,
                                self.strings('added_msg', message)\
                                    .format(  # noqa: E127
                                    f"t.me/addstickers/{packname}"
                                ))
            await sleep(5)
            await message.delete()


async def resize_photo(photo):
    """ 🏳️‍🌈Изменение размера анала на 512x512 🏳️‍🌈"""
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image
