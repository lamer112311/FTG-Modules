import requests
from .. import loader, utils
import io
def register(cb):
    cb(TikTokDownMod())
class TikTokDownMod(loader.Module):
    """ты еблан да?"""
    strings = {'name': 'ТикТок даунлодер'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
    async def tikcmd(self, event):
        args = utils.get_args_raw(event)
        reply = await event.get_reply_message()
        if not args:
            if not reply:
                await event.edit("где ссылка, клоун.")
                return
            else:
                args = reply.raw_text
        await event.edit("делается делается.")
        data = {'url': args}
        response = requests.post('https://tik.fail/api/geturl', data=data).json()
        tik = requests.get(response['direct'])
        file = io.BytesIO(tik.content)
        file.name = response['direct']
        file.seek(0)
        await event.client.send_file(event.to_id, file)