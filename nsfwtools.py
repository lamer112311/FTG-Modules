#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils

from telethon.errors.rpcerrorlist import MessageNotModifiedError

import logging
import asyncio

logger = logging.getLogger(__name__)


@loader.tds
class TickerMod(loader.Module):
    """Делает сообщение с анимацией бегущей строки"""
    strings = {"name": "Ticker",
               "no_message": "<b>...🏳️‍🌈Нихуя🏳️‍🌈!</b>",
               "type_char_cfg_doc": "Персонаж для гей оргии🏳️‍🌈",
               "delay_typer_cfg_doc": "Как долго будет длиться гей-оргия🏳️‍🌈",
               "delay_text_cfg_doc": "Как долго будет длиться оргазм🏳️‍🌈"}

    def __init__(self):
        self.config = loader.ModuleConfig("DELAY_TYPER", 0.04, lambda m: self.strings("delay_typer_cfg_doc", m),
                                          "DELAY_TEXT", 0.02, lambda m: self.strings("delay_text_cfg_doc", m))

    @loader.ratelimit
    async def adscmd(self, message):
        """.ticker <message>"""
        a = utils.get_args_raw(message)
        if not a:
            await utils.answer(message, self.strings("no_message", message))
            return
        for c in a:
            a = a[-1]+a[0:-1]
            message = await utils.answer(message, "⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠"+a+"⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠")
            await asyncio.sleep(0.02)


