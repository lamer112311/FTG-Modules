# Russian tts for Friendly-telegram: .rtts

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
    cb(uttsMod())


class uttsMod(loader.Module):
    """ттс с мовой"""

    strings = {'name': 'ТекстТуВойсУкр'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def ukcmd(self, event):
        """.uk {текст}"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        global reply_and_text
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                await event.edit('<code>Вы должны или написать шото </code>')
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
            if not reply_message.text:
                await event.edit('<code>Группа поддержки @memeframe</code>')
                return
        chat = '@playcraftbot'
        await event.edit('<code> Обработка...</code>')
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,
                                                             from_users=380570427))
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply('<code>Разблокируй @playcraftbot</code>')
                return
            await event.delete()
            if reply_and_text:
                await event.client.send_file(event.chat_id, response.voice,
                                                reply_to=reply_message.id)
            else:
                await event.client.send_file(event.chat_id, response.voice)