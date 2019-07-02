# coding: utf-8

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


# @respond_to('string')

# @listen_to('string')

# @default_reply() <=> DEFAULT_REPLY

# massage.reply('string') @sender: send to memssage

# message.send('string') send to string massage

# massage.react('icon_emoji') send to emoji

@listen_to('')
def listen_func(massage):
    massage.reply('')