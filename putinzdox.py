from telethon import functions, types, events
from .. import loader, utils
from telethon.errors.rpcerrorlist import YouBlockedUserError
import datetime
import random
from asyncio import sleep
def register(cb):
    cb(PutinZdoxMod())
class PutinZdoxMod(loader.Module):
    """Рандомные мемы из @PutinZdox"""
    strings = {'name': 'ПутинЗдох'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def putinripcmd(self, message):
        """
        Рандомные мемы из @PutinZdox
        """
        await message.edit("<b>ПУТИН СДОХ!!!!!!!!</b>")
        chat = '@PutinZdox'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101]),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_file(message.to_id, result.messages[0].media)

    async def repomemcmd(self, message):
        """
        Рандомные мемы из @repomem 
        """
        await message.edit("<b>Репуем</b>")
        chat = '@repomem'
        result = await message.client(functions.messages.GetHistoryRequest(
        peer=chat,
        offset_id=0,
        offset_date=datetime.datetime.now(),
        add_offset=random.choice([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99,101]),
        limit=1,
        max_id=0,
        min_id=0,
        hash=0
        ))
        await message.delete()
        await message.client.send_file(message.to_id, result.messages[0].media)
    
            
