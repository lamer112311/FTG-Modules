# -*- coding: utf-8 -*-

#   Friendly Telegram (telegram userbot)
#   Copyright (C) 2018-2020 The Authors

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging
import requests

from .. import loader, utils
from PIL import Image
from urllib.request import urlretrieve
from telethon.tl.types import (MessageEntityBold, MessageEntityItalic,
                               MessageEntityMention, MessageEntityTextUrl,
                               MessageEntityCode, MessageEntityMentionName,
                               MessageEntityHashtag, MessageEntityCashtag,
                               MessageEntityBotCommand, MessageEntityUrl,
                               MessageEntityStrike, MessageEntityUnderline)

from simplejson.scanner import JSONDecodeError
import telethon

logger = logging.getLogger(__name__)


def register(cb):
    cb(rsQuotesMod())


@loader.tds
class rsQuotesMod(loader.Module):
    """Quote a message"""
    strings = {
        "name": "rsQuotes",
        "api_token_cfg_doc": "API Token for Quotes",
        "api_url_cfg_doc": "API Url for Quotes",
        "quote_style_cfg_doc": "Default Quote style (template)",
        "username_colors_cfg_doc": "Username Colors",
        "default_username_color_cfg_doc": "Default color for username",
        "default_sendtype_cfg_doc": "Default Quote send type",
        "no_reply": "<code>You didn\'t reply to a message.</code>",
        "processing": "<code>Processing quote...</code>",
        "processing_onlytext": "<code>Processing quote... Note: only message w/o media will get processed.</code>",
        "unreachable_error": "<b>API Host is unreachable now. Please try again later.</b>",
        "server_error": "<b>API Error occured :)</b>",
        "invalid_token_error": "<b>Wrong API Token.</b>",
        "template_notfound_error": "<b>Requested template</b> <code>{}</code> <b>not found</b>",
        "template_accessdenied_error": "<b>Not enough rights to use <code>{}</code> template.</b>",
        "available_templates": "Available templates: <code>{}</code>",
        "markdown_error": "<code>Markdown has broken. Try another message</code>",
        "cannot_resolve_error": "<b>Cannot resovle an error.\nServer returned:</b> <code>{}</code>",
        "filename": "quote.png",
        "stickername": "quote.webp",
        "admin": "admin",
        "creator": "creator",
        "channel": "Channel",
        "hidden": "Hidden",
        "delimiter": "</code>, <code>",
        "mediaType_photo": "Photo",
        "mediaType_video": "Video",
        "mediaType_videomessage": "Video message",
        "mediaType_voice": "Voice message",
        "mediaType_audio": "Audio",
        "mediaType_poll": "Poll",
        "mediaType_location": "Location",
        "mediaType_gif": "GIF",
        "mediaType_sticker": "Sticker",
        "mediaType_file": "File",
        "diceType_dice": "Dice",
        "diceType_dart": "Dart",
        "ball_thrown": "Ball thrown",
        "dart_thrown": "Dart thrown",
        "dart_almostthere": "almost there!",
        "dart_missed": "missed!",
        "dart_bullseye": "bullseye!"
    }

    def __init__(self):
        self.config = loader.ModuleConfig("API_TOKEN", 'xxx-xxx-xxx',
                                          lambda: self.strings['api_token_cfg_doc'],
                                          "DEFAULT_STYLE", 'ios',
                                          lambda: self.strings['quote_style_cfg_doc'],
                                          "API_URL", 'http://rsdev.ml/dev',
                                          lambda: self.strings['api_url_cfg_doc'],
                                          "USERNAME_COLORS", ["#fb6169", "#85de85", "#f3bc5c", "#65bdf3", "#b48bf2", "#ff5694", "#62d4e3", "#faa357"],
                                          lambda: self.strings['username_colors_cfg_doc'],
                                          "DEFAULT_USERNAME_COLOR", "#b48bf2",
                                          lambda: self.strings['default_username_color_cfg_doc'],
                                          "DEFAULT_SENDTYPE", "sticker",
                                          lambda: self.strings['default_sendtype_cfg_doc'])

    async def client_ready(self, client, db):
        self.client = client
    
    @loader.unrestricted
    @loader.ratelimit
    async def rquotecmd(self, message):
        """Usage: .rquote (template) (optional: file/force_file/sticker)
        Sends as setted config value by default
        Needs an API Token."""
        args = utils.get_args(message)
        reply = await message.get_reply_message()

        if not reply:
            return utils.answer(message, self.strings('no_reply', message))

        if reply.media:
            await utils.answer(message, self.strings('processing_onlytext', message))
        else:
            await utils.answer(message, self.strings('processing', message))

        sendtype = self.config['DEFAULT_SENDTYPE']
        has_reply = "reply"

        if not args:
            style = self.config['DEFAULT_STYLE']
        else:
            style = args[0]

        if args:
            if len(args) < 2:
                pass
            else:
                sendtype = args[1]
            if len(args) < 3:
                pass
            else:
                has_reply = args[2]
                if has_reply not in ["reply", "noreply"]:
                    has_reply = "reply"
        else:
            pass
        
        pfp = username_color = username = user_id = hasMedia = None
        media_image = reply_username = reply_text = admintitle = ""
        profile_photo_url = reply.from_id
        no_pfp = True

        if isinstance(reply.to_id, telethon.tl.types.PeerChannel) and reply.fwd_from:
            user = reply.forward.chat
        elif isinstance(reply.to_id, telethon.tl.types.PeerChat):
            chat = await self.client(telethon.tl.functions.messages.GetFullChatRequest(reply.to_id))
            participants = chat.full_chat.participants.participants
            participant = next(filter(lambda x: x.user_id == reply.from_id, participants), None)
            if isinstance(participant, telethon.tl.types.ChatParticipantCreator):
                admintitle = self.strings("creator", message)
            elif isinstance(participant, telethon.tl.types.ChatParticipantAdmin):
                admintitle = self.strings("admin", message)
            user = await reply.get_sender()
        else:
            user = await reply.get_sender()

        username = telethon.utils.get_display_name(user)
        if reply.fwd_from is not None and reply.fwd_from.post_author is not None:
            username += f" ({reply.fwd_from.post_author})"
        user_id = reply.from_id

        if reply.fwd_from:
            if reply.fwd_from.saved_from_peer:
                profile_photo_url = reply.forward.chat
                admintitle = self.strings("channel", message)
            elif reply.fwd_from.from_name:
                username = reply.fwd_from.from_name
                profile_photo_url = None
                admintitle = ""
            elif reply.forward.sender:
                username = telethon.utils.get_display_name(reply.forward.sender)
                profile_photo_url = reply.forward.sender.id
                admintitle = ""
            elif reply.forward.chat:
                admintitle = self.strings("channel", message)
                profile_photo_url = user
        else:
            if isinstance(reply.to_id, telethon.tl.types.PeerUser) is False:
                try:
                    user = await self.client(telethon.tl.functions.channels.GetParticipantRequest(message.chat_id,
                                                                                                  user))
                    if isinstance(user.participant, telethon.tl.types.ChannelParticipantCreator):
                        admintitle = user.participant.rank or self.strings("creator", message)
                    elif isinstance(user.participant, telethon.tl.types.ChannelParticipantAdmin):
                        admintitle = user.participant.rank or self.strings("admin", message)
                    user = user.users[0]
                except telethon.errors.rpcerrorlist.UserNotParticipantError:
                    pass
        if profile_photo_url is not None:
            pfp = await self.client.download_profile_photo(profile_photo_url)

        if pfp is not None:
            profile_photo_url = upload_to_0x0st(pfp)
            no_pfp = False
        else:
            profile_photo_url = ""

        if user_id is not None:
            colors = self.config['USERNAME_COLORS']
            num1 = user_id % 7
            num2 = [0, 7, 4, 1, 6, 3, 5]
            username_color = colors[num2[num1]]
        else:
            username_color = self.config['DEFAULT_USERNAME_COLOR']

        if reply.is_reply is True:
            reply_to = await reply.get_reply_message()
            reply_peer = None
            if reply_to.fwd_from is not None:
                if reply_to.forward.chat is not None:
                    reply_peer = reply_to.forward.chat
                elif reply_to.fwd_from.from_id is not None:
                    try:
                        user_id = reply_to.fwd_from.from_id
                        user = await self.client(telethon.tl.functions.users.GetFullUserRequest(user_id))
                        reply_peer = user.user
                    except ValueError:
                        pass
                else:
                    reply_username = reply_to.fwd_from.from_name
            elif reply_to.from_id is not None:
                reply_user = await self.client(telethon.tl.functions.users.GetFullUserRequest(reply_to.from_id))
                reply_peer = reply_user.user

            if reply_username is None or reply_username == "":
                reply_username = telethon.utils.get_display_name(reply_peer)
            reply_text = reply_to.message
        if reply.media:
            data = await check_media(reply)
            if not isinstance(data, bool):
                hasMedia = True
        if hasMedia:
	        path_img = await self.client.download_media(
	                    reply,
	                    progress_callback=progress,
	        )
	        media_image = upload_to_0x0st(path_img)
        media_caption = await get_media_caption(await reply.get_reply_message())
        if media_caption != "":
            if not reply_text:
                reply_text = media_caption
            else:
                reply_text = "{} \"{}\"".format(media_caption, reply_text)
        if has_reply == "noreply":
            reply_username = ""
            reply_text = ""
        token = self.config['API_TOKEN']
        try:
            requested = requests.post(self.config['API_URL'] + '/quote', data={
                'pfp': profile_photo_url.encode('utf-8'),
                'no_pfp': str(no_pfp).encode('utf-8'),
                'colour': username_color.encode('utf-8'),
                'username': username.encode('utf-8'),
                'admintitle': admintitle.encode('utf-8'),
                'raw_text': process_entities(reply).encode('utf-8'),
                'token': token.encode('utf-8'),
                'style': style.encode('utf-8'),
                'replyNick': reply_username.encode('utf-8'),
                'replyText': reply_text.encode('utf-8'),
                'mediaImage': media_image.encode('utf-8')
            })
        except requests.ConnectionError:
            return await utils.answer(message, self.strings('unreachable_error', message))
        if requested.status_code == 500:
            return await utils.answer(message, self.strings('server_error', message))
        else:
            requested = requested.json()
        
        try:
            urlretrieve(requested['success']['file'], self.strings('filename', message))
            if sendtype.lower() == 'file':
                with open(self.strings('filename', message), 'rb') as file:
                    await utils.answer(message, file)
                os.remove(self.strings('filename', message))
            elif sendtype.lower() == 'force_file':
                with open(self.strings('filename', message), 'rb') as file:
                    await utils.answer(message, file, force_file=True)
                os.remove(self.strings('filename', message))
            else:
                Image.open(self.strings('filename', message)).save(
                    self.strings('stickername', message
                ), 'webp')
                with open(self.strings('stickername', message), 'rb') as sticker:
                    await utils.answer(message, sticker)
                os.remove(self.strings('stickername', message))
                try:
                    os.remove(self.strings('filename', message))
                except:
                    pass
        except KeyError:
            if requested.get('402'):
                if requested['402'] == 'TEMPLATE_NOT_FOUND':
                    templates = requests.get(self.config['API_URL'] + '/quote/getTemplates', params={
                        'token': token.encode('utf-8')
                    })
                    try:
                        requestedTemplates = templates.json()
                    except JSONDecodeError:
                        return await utils.answer(message, 
                                                  self.strings('invalid_token_error',
                                                               message))
                    try:
                        if requestedTemplates['success']:
                            templateList = self.strings('delimiter', message)\
                                .join(list(requestedTemplates['success']['templates']))
                            return await utils.answer(message, self.strings('template_notfound_error', message)\
                                .format(style) + '\n' + self.strings('available_templates', message)\
                                    .format(templateList))
                    except KeyError:
                        return await utils.answer(message, self.strings('template_notfound_error', message)\
                            .format(style))
            elif requested.get('707'):
                if requested['707'] == 'TEMPLATE_ACCESS_DENIED':
                    templates = requests.get(self.config['API_URL'] + '/quote/getTemplates', params={
                        'token': token.encode('utf-8')
                    })
                    try:
                        requestedTemplates = templates.json()
                    except JSONDecodeError:
                        return await utils.answer(message, self.strings('invalid_token_error',
                                                                        message))
                    try:
                        if requestedTemplates['success']:
                            templateList = self.strings('delimiter', message)\
                                .join(list(requestedTemplates['success']['templates']))
                            return await utils.answer(message, self.strings('template_accessdenied_error', message)\
                                .format(style) + '\n' + self.strings('available_templates', message)\
                                    .format(templateList))
                    except KeyError:
                        return await utils.answer(message, self.strings('template_accessdenied_error', message)\
                            .format(style))
            elif requested.get('202'):
                if requested['202'] == 'INVALID TOKEN':
                    return await utils.answer(message, self.strings('invalid_token_error',
                                                                    message))
            elif requested.get('499'):
                if requested['499'] == "'ERROR_TEXT_MARKDOWN_INVALID'":
                    return await utils.answer(message, self.strings('markdown_error',
                                                                    message))
            else:
                err = self.strings('cannot_resolve_error', message)\
                    .format(str(requested))
                return await utils.answer(message, err)


def process_entities(reply):
    if not reply.entities:
        return reply.raw_text

    raw_text = reply.raw_text
    text = [x for x in raw_text]
    for entity in reply.entities:
        entity_type = type(entity)
        start = entity.offset
        end = start + (entity.length - 1)
        if entity_type is MessageEntityBold:
            text[start] = '{b}' + text[start]
        elif entity_type is MessageEntityItalic:
            text[start] = '{i}' + text[start]
        elif entity_type in [MessageEntityMention, MessageEntityTextUrl,
                             MessageEntityMentionName, MessageEntityHashtag,
                             MessageEntityCashtag, MessageEntityBotCommand,
                             MessageEntityUrl]:
            text[start] = '{l}' + text[start]
        elif entity_type is MessageEntityCode:
            text[start] = '{c}' + text[start]
        elif entity_type is MessageEntityStrike:
            text[start] = '{s}' + text[start]
        elif entity_type is MessageEntityUnderline:
            text[start] = '{u}' + text[start]
        text[end] = text[end] + '{cl}'

    return ''.join(text)


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
            if reply_message.gif or reply_message.video or reply_message.audio or reply_message.voice:
                return False
            data = reply_message.media.document
        else:
            return False
    else:
        return False

    if not data or data is None:
        return False
    else:
        return data


async def get_media_caption(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            return rsQuotesMod.strings["mediaType_photo"]
        dice = False
        try:
            dice = True if reply_message.dice else False
        except AttributeError:
            try:
                dice = True if type(reply_message.media) == telethon.tl.types.MessageMediaDice else False
            except AttributeError:
                pass
        if dice:
            dice_type = ""
            dice_text = reply_message.media.value
            if reply_message.media.emoticon == "🎲":
                dice_type = rsQuotesMod.strings["diceType_dice"]
                return "{} {}: {}".format(reply_message.media.emoticon,
                                                      dice_type,
                                                      dice_text)
            elif reply_message.media.emoticon == "🎯":
               if dice_text == 1:
                   dice_text = rsQuotesMod.strings["dart_missed"]
               elif dice_text == 5:
                   dice_text = rsQuotesMod.strings["dart_almostthere"]
               elif dice_text == 6:
                   dice_text = rsQuotesMod.strings["dart_bullseye"]
               else:
                    return "{} {}".format(reply_message.media.emoticon,
                                                      rsQuotesMod.strings["dart_thrown"])
               dice_type = rsQuotesMod.strings["diceType_dart"]
               return "{} {}: {}".format(reply_message.media.emoticon,
                                                     dice_type,
                                                     dice_text)
            elif reply_message.media.emoticon == "🏀":
                return "{} {}".format(reply_message.media.emoticon,
                                                  rsQuotesMod.strings["ball_thrown"])
        elif reply_message.poll:
            return rsQuotesMod.strings["mediaType_poll"]
        elif reply_message.geo:
             return rsQuotesMod.strings["mediaType_location"]
        elif reply_message.document:
            if reply_message.gif :
                return rsQuotesMod.strings["mediaType_gif"]
            elif reply_message.video:
                if reply_message.video.attributes[0].round_message:
                    return rsQuotesMod.strings["mediaType_videomessage"]
                else:
                    return rsQuotesMod.strings["mediaType_video"]
            elif reply_message.audio:
                return rsQuotesMod.strings["mediaType_audio"]
            elif reply_message.voice:
                return rsQuotesMod.strings["mediaType_voice"]
            elif reply_message.file:
                if reply_message.file.mime_type == "application/x-tgsticker":
                        emoji = ""
                        try:
                            emoji = reply_message.media.document.attributes[0].alt
                        except AttributeError:
                            try:
                                emoji = reply_message.media.document.attributes[1].alt
                            except AttributeError:
                                emoji = ""
                        caption = "{} {}".format(emoji, rsQuotesMod.strings["mediaType_sticker"]) if emoji != "" else rsQuotesMod.strings["mediaType_sticker"]
                        return caption
                else:
                    if reply_message.sticker:
                        emoji = ""
                        try:
                            emoji = reply_message.file.emoji
                            logger.debug(len(emoji))
                        except TypeError:
                            emoji = ""
                        caption = "{} {}".format(emoji, rsQuotesMod.strings["mediaType_sticker"]) if emoji != "" else rsQuotesMod.strings["mediaType_sticker"]
                        return caption
                    else:
                        return rsQuotesMod.strings["mediaType_file"]
        else:
            return ""
    else:
        return ""
   
    return ""


def upload_to_0x0st(path):
    req = requests.post('https://0x0.st', files={'file': open(path, 'rb')})
    os.remove(path)
    return req.text


def progress(current, total):
	""" Logs the download progress """
	logger.info("Downloaded %s of %s\nCompleted %s", current, total,
			  (current / total) * 100)
