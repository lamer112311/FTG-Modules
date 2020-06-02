# made with love by justsayoriska
import logging
import requests
from .. import loader

logger = logging.getLogger(__name__)


def register(cb):
    cb(KittyMod())


class KittyMod(loader.Module):
    """justsayoriska`s & demenkop kitties module"""
    strings = {'name': 'Киски'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def kittycmd(self, e):
        """this coommand will send a random kitty picture using API"""
        url = 'https://api.thecatapi.com/v1/images/search'
        r = requests.get(url, allow_redirects=True)
        r.headers['x-api-key'] = '97037ecc-6b34-4ca2-a072-adf1e4c74ace'
        json = r.json()
        for j in json:
            kittyurl = j['url']
            rs = requests.get(kittyurl, allow_redirects=True)
            open('kotik.png', 'wb').write(rs.content)
            await e.client.send_file(entity=await e.client.get_input_entity(e.chat_id),
                                     file='kotik.png')
            await e.delete()
