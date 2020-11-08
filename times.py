# Целую в попку 😘 by @laciamemeframe
import requests
from .. import loader, utils
def register(cb):
    cb(TimesMod())
class TimesMod(loader.Module):
    """https://www.amdoren.com"""
    strings = {'name': 'Время'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
    async def timescmd(self, event):
        user_msg = """{}""".format(utils.get_args_raw(event))
        key = "eYeqKkdKGpatUfCgQmk8LqTU3MTjCW"
        url = f"https://www.amdoren.com/api/timezone.php?api_key={key}&loc={user_msg}"
        if not user_msg:
            await event.edit("<b>Где время будем смотреть?</b>", parse_mode='HTML')
            return
        await event.edit("<b>Получаем айпи твоей матери.</b>", parse_mode='HTML')
        data = {'url': user_msg}
        response = requests.post(url, data=data).json()
        user_msg = response['time']
        await event.edit(f'<b>{user_msg}</b>', parse_mode='HTML')