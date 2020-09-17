#by @laciamemeframe
from telethon import events
from .. import loader, utils


def register(cb):
	cb(welcomeMod())


class welcomeMod(loader.Module):
    """welcome"""

    strings = {'name': 'Приветствие'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def wait_event(self, event):
        """ хуйня"""

        welcome = await event.get_user_joined()
        if not welcome:
            return
        try:
           await event.client.send_message(event.to_id, 'Привет', reply_to=await message.get_reply_message())
        except:
            return           