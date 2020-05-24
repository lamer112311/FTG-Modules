#made by @VadimSap & KeyZenD
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.nl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Ща как загрузим...`")
	sleep(1)
	await typew.edit("`Уничтожение логов: `0%")
	number = 1
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(("`Уничтожение логов: `") +str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Уничтожение логов....`")
	sleep(1)
	await typew.edit("`Логов больше нет!`")






