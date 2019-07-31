
# coding: utf-8

from slackbot.bot import respond_to # @botname: で反応するデコーダ
from slackbot.bot import listen_to #　チャンネル内発言で反応するデコーダ
from slackbot.bot import default_reply # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

@respond_to('無常')
def mention_func(message):
    message.reply('左様……')

@listen_to('ヴィンランド・サガ')
@listen_to('ヴィンランドサガ')
def listen_func(message):
    #message.send('誰かヴィンランド・サガの話してる？')
    message.reply('ヴィンランドサガの話ししてます？')

@respond_to('天気')
@listen_to('天気')
def weather(message):
    import urllib
    import json

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='

    city_id = '040010'
    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    title = jsonfile['title']
    telop = jsonfile['forecasts'][0]['telop']
    celsius_max = jsonfile['forecasts'][0]['temperature']['max']['celsius']

    # if jsonfile["forecasts"][0]["temperature"]["min"]["celsius"] is not None:
    #     celsius_min = jsonfile["forecasts"][0]["temperature"]["min"]["celsius"]
    # else:
    #     celsius_min = "--"
    #celsius_min = jsonfile['forecasts'][0]['temperature']['min']['celsius']
    # なぜか最低気温を出力するとなると
    # TypeError: 'NoneType' object is not subscriptable
    # ってエラー吐くよ

    telop_icon = ''
    if telop.find('雪') > -1:
        telop_icon = ':showman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thinder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'
    text = title + '\n' + '今日の天気 : ' + telop + telop_icon \
           + '\n' + '最高気温 : ' + celsius_max + '℃' \
            # + '最低気温 : ' + celsius_min + '℃'
    message.reply(text)

