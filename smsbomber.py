#смс бомбер работающий на боте t.me/mha0flood_bot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def refister(cb):
    cb(Smsbomber())
 

class Smsbomber(loader.Module):
    """Вдохновлялся русской смекалкой"""
    strings = {'name': 'Смс бомбер'}
    
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelomit = {}
    
    async def client_ready(self, client, db):
        self._db =db
        self._ratelimit = []
