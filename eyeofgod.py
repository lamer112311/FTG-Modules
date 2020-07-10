from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
def register(cb):
    cb(EyefGodMod())
class EyefGodMod(loader.Module):
    """Eye Of God"""
    strings = {'name': 'Eye Of God'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def tgcmd(self, message):
        """.tg <reply_to_message/reply_to_user/id/@nickname>
            Проверка на утечку телеграм
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                user = utils.get_args_raw(message)
            else:
                await message.edit("А кого искать?")
                return
        else:
            try:
                user = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>Получаем информацию...</b>")
        chat = '@EyeGodsBot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1014369089))
                m1 = await message.client.send_message(chat, "/tg {0}".format(user))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()
    async def namecmd(self, message):
        """.name <name/reply_to_message>
            Поиск телефона по базе «Возможных имен»
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                name = utils.get_args_raw(message)
            else:
                await message.edit("А кого искать?")
                return
        else:
            try:
                name = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>Получаем информацию...</b>")
        chat = '@EyeGodsBot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1014369089))
                m1 = await message.client.send_message(chat, "/name {0}".format(name))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()
    async def mailcmd(self, message):
        """.mail <mail/reply_to_message>
            Поиск информации по Email
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                mail = utils.get_args_raw(message)
            else:
                await message.edit("А кого искать?")
                return
        else:
            try:
                mail = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>Получаем информацию...</b>")
        chat = '@EyeGodsBot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1014369089))
                m1 = await message.client.send_message(chat, "{0}".format(mail))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()
    async def vkcmd(self, message):
        """.vk <vk_url/vk_id/vk_short_name/reply_to_url>
            Поиск телефона/почты по странице Вконтакте
        """
        vk = utils.get_args_raw(message)
        url = ""
        check = True
        try:
            int(vk)
            url = "https://vk.com/id" + vk
            check = false
        except:
            pass
        if(check):
            if(vk.startswith("https://vk.com/")):
                url = vk
            elif(vk.startswith("http://vk.com/")):
                url = vk.replace("http://", "https://")
            elif(vk.startswith("vk.com/")):
                url = "https://" + vk
            elif(vk.startswith("id")):
                url = "https://vk.com/" + vk
            else:
                url = "https://vk.com/" + vk
        await message.edit("<b>Получаем информацию...</b>")
        chat = '@EyeGodsBot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1014369089))
                m1 = await message.client.send_message(chat, "{0}".format(url))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()