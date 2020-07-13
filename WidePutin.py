from .. import loader, utils
import subprocess
import os
from moviepy.editor import VideoFileClip
def register(cb):
	cb(WidePutinMod())
class WidePutinMod(loader.Module):
	"""WidePutin"""
	strings = {'name': 'WidePutin'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def widepcmd(self, message):
		""".widep <reply to video>
		    Эффект wideputin
		"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("А где реплай на видео?")
			return
		await message.edit("<b>Скачиваем...</b>")
		await message.client.download_file(reply.media, "video.mp4")
		subprocess.check_output("ffmpeg -y -i {0} -vn -ar 44100 -ac 2 -ab 192K -f mp3 sound.mp3".format("video.mp4"), shell=True)
		await message.edit("<b>Wide'им...</b>")
		video = VideoFileClip("video.mp4")
		video.reader.close()
		w, h = video.size
		video = video.resize((w*2, h//2))
		await message.edit("<b>Экспортируем...</b>")
		video.write_videofile("result.mp4")
		subprocess.check_output("ffmpeg -y -i workwide/audio/sound.mp3 -i {0} {1}".format("video.mp4", "out.mp4"), shell=True)
		await message.edit("<b>Отправляем...</b>")
		await message.client.send_file(message.to_id, "result.mp4")
		await message.delete()
		os.remove("video.mp4")
		os.remove("out.mp4")
		os.remove("sound.mp3")
		os.remove("result.mp4")



