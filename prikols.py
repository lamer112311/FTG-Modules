#код спиздила с модуля который сколько раз я тебе повторял автор не ругайся пожалуйста ты крутой а я люблю вареники с творогом и вишней
import telethon
from .. import loader, utils
import os
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
import io
from io import BytesIO
from textwrap import wrap
import random

def register(cb):
    cb(PrikolMod())

class PrikolMod(loader.Module):
    """приколы"""
    strings = {'name': 'приколы'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def akcmd(self, message):
        """.ak и реплай на картинку. акушерка сбежала помогите найти"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem(pic)
            await message.client.send_file(message.to_id, what)


    async def ebcmd(self, message):
        """.eb и реплай на картинку.  муж ебет меня чето там"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media1(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem1(pic)
            await message.client.send_file(message.to_id, what)


    async def intcmd(self, message):
        """.int и реплай на картинку. интересноо я один блаблаблабда"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media1(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem2(pic)
            await message.client.send_file(message.to_id, what)


    async def smcmd(self, message):
        """.sm и реплай на картинку. смешные картинки в понедельник"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem3(pic)
            await message.client.send_file(message.to_id, what)
            
            
    async def moskcmd(self, message):
        """.mosk и реплай на картинку. виноваты москали"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem4(pic)
            await message.client.send_file(message.to_id, what)
           

    async def aktcmd(self, message):
        """.akt и реплай на картинку. убийца актер"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem5(pic)
            await message.client.send_file(message.to_id, what)
            


    async def zpmcmd(self, message):
        """.zpm и реплай на картинку. запомните твари"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem6(pic)
            await message.client.send_file(message.to_id, what)
            
            
    async def zbtcmd(self, message):
        """.zbt и реплай на картинку.  забудьте твари"""
        await message.delete()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("реплай на картиночку, пожалуйста")
        else:
            pic = await check_media1(message, reply)
            if not pic:
                await utils.answer(message, 'это не картиночка')
                return
            what = mem7(pic)
            await message.client.send_file(message.to_id, what)
            
def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem(image):
    pics = requests.get("https://0x0.st/i6m3.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 410)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None
            

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem1(image):
    pics = requests.get("https://0x0.st/i6df.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 160)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media1(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None
            

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem2(image):
    pics = requests.get("https://0x0.st/iI1p.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 650)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media2(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None            


def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem3(image):
    pics = requests.get("https://0x0.st/iIvc.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 580)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media3(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem4(image):
    pics = requests.get("https://0x0.st/iIvA.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (1, 1), 580)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media4(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None            
            
            
def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 4, size * 1))
    background.paste(overlay, cords)


def mem5(image):
    pics = requests.get("https://0x0.st/iIgT.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (105, 1), 440)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media5(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None            
            
            
def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem6(image):
    pics = requests.get("https://0x0.st/iIgy.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (160, 200), 90)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media6(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None            


def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 2, size * 1))
    background.paste(overlay, cords)


def mem7(image):
    pics = requests.get("https://0x0.st/iIgt.jpg" )
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGB")
    lol(img, image, (160, 200), 90)

    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out, format="png")
    return out.getvalue()

async def check_media7(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_file(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None            