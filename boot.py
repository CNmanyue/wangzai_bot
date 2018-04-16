#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 19:58
# @Author  : zhouxw
# @File    : boot.py
# @Software: PyCharm

"""
    1. pip install python-telegram-bot

"""

import logging

import telegram
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram.utils.request import Request

from gjj import query
from laifudao import joke

token = '584347337:AAE0Q9hvVwPTckmZlSWY_xtuS1iIl5gd4I8'

# proxy = telegram.utils.request.Request(con_pool_size=10)
proxy = telegram.utils.request.Request(con_pool_size=10, proxy_url='https://127.0.0.1:1080')
bot = telegram.Bot(token=token, request=proxy)
print(bot.get_me())

update = Updater(bot=bot)
dispatcher = update.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    text = "I'm a bot, please talk to me!	__zhouxw"
    chat_id = update.message.chat_id
    logging.info(str(chat_id) + " - " + text, )
    bot.send_message(chat_id=chat_id, text=text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# 回声效果
def echo(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    logging.info(str(chat_id) + " - " + text, )
    bot.send_message(chat_id=chat_id, text=text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


# 转大写
def caps(bot, update, args):
    text_caps = "command invalid: /caps string"
    if len(args) > 0:
        text_caps = ' '.join(args).upper()

    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)


# 查询公积金
def gjj(bot, update, args):
    print("telegram /gjj param:", args[0:])
    result = "command invalid: /gjj gjj_account id_card"
    if len(args) >= 2:
        result = query.query(args[0], args[1])

    bot.send_message(chat_id=update.message.chat_id, text=result)


gjj_handler = CommandHandler('gjj', gjj, pass_args=True)
dispatcher.add_handler(gjj_handler)


# 发送爱心
def mlq(bot, update, args):
    text_caps = '（づ￣3￣）づ╭❤～'
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


mlq_handler = CommandHandler('mlq', mlq, pass_args=True)
dispatcher.add_handler(mlq_handler)


# 讲个笑话
def get_joke(bot, update, args):
    text_joke = "this is a joke_repo"
    print(text_joke)
    if len(args) > 0 and isinstance(args[0], int):
        text_joke = joke.get_joke(args[0])
        print(text_joke)
    else:
        text_joke = joke.get_joke()
        print(text_joke)

    print(text_joke)
    bot.send_message(chat_id=update.message.chat_id, text=text_joke)


joke_handler = CommandHandler('joke', get_joke, pass_args=True)
dispatcher.add_handler(joke_handler)

# fire up bot
update.start_polling()
