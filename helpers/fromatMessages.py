from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from utils.Logger import *
from utils.Config import Config

Config = Config()


def getMessage(message, action):
    try:
        ALLOWED_CHAT_TYPES = config.get("ALLOWED_CHAT_TYPES")

        if action == "private-chat":
            send_message = f"**Hi 🎵 {message.chat.first_name if hasattr(message.chat, 'first_name') else 'User'}**"
            send_message = send_message + \
                f"\n\n**[Paattupetti VCBOT]({config.get('BOT_URL')})** is maintained by [Adith Balan]({config.get('PARENT_URL')})."
            send_message = send_message + \
                f"\n__It is designed to play, as simple as possible, music in your groups through the **new voice chats** introduced by Telegram.__"
            send_message = send_message + \
                f"\n\n**So why wait 🌀 add the bot to a group and get started 🎧**\n\n"
            return send_message, getReplyKeyBoard(message, action)

        elif action == "help-msg":
            helpMessage = f"Paattupetti VCBOT"
            helpMessage = helpMessage + \
                f"\n\n• **/play song name/song url : ** __Start a song / add to queue.__"
            helpMessage = helpMessage + f"\n• **/skip : ** __Skip to the next song in queue.__"
            helpMessage = helpMessage + f"\n• **/stop : ** __Stop the playback.__"
            helpMessage = helpMessage + \
                f"\n• **/refreshadmins : ** __Refreshes the admin list.__"
            helpMessage = helpMessage + \
                f"\n• **/auth : ** __Adds the user in reply to the message as admin.__"
            helpMessage = helpMessage + \
                f"\n• **/unauth : ** __Removes the user in reply to the message as admin.__"
            helpMessage = helpMessage + \
                f"\n• **/listadmins : ** __Lists the users assigned as admins for the bot.__"
            helpMessage = helpMessage + \
                f"\n• **/adminmode on|off : ** __Turning this on makes the bot actions available only to bot admins.__"
            helpMessage = helpMessage + \
                f"\n• **/loop [2-5]|off : ** __Loop the playback [x] times(x is between 2-5) / Turn off the loop playback.__"
            helpMessage = helpMessage + f"\n\n**__For any issues contact @voicechatsupport__**"
            return helpMessage, getReplyKeyBoard(message, action)

        elif action == "start-voice-chat":
            send_message = f"**Please start a voice chat and then send the command again**"
            send_message = send_message + \
                f"\n**1.** __To start a group chat, you can head over to your group’s description page.__"
            send_message = send_message + \
                f"\n**2.** __Then tap the three-dot button next to Mute and Search start a Voice Chat.__"
            return send_message, getReplyKeyBoard(message, action)

    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)


