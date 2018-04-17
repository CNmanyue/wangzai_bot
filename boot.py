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
from uuid import uuid4

import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram.utils.helpers import escape_markdown
from telegram.utils.request import Request

from gjj import query
from inline.query import query_bank
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


def query_my_bank(bot, update):
    """Handle the inline query."""
    query_text = update.inline_query.query
    print("inline input data:" + query_text)
    results_src = query_bank(query_text)
    results = []
    for r in results_src:
        results.append(InlineQueryResultArticle(
            id=uuid4()
            , title=r.get_name()
            , description=r.get_card_no()
            , input_message_content=InputTextMessageContent(r.get_name() + " " + r.get_card_no())
            , thumb_url="https://pbs.twimg.com/profile_images/731814947/7_400x400.gif"
            # , thumb_width=300
            # , thumb_height=86
            # , thumb_url="http://www.cool80.com/img.cool80/i/logo/j/jiansheyinhang.jpg"
            # , thumb_width=300
            # , thumb_height=100
            # , hide_url=True
            # ,thumb_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
            # , thumb_width=503
            # , thumb_height=170
        ))

    # results = [
    #     InlineQueryResultArticle(
    #         id=uuid4(),
    #         title="Caps",
    #         input_message_content=InputTextMessageContent(
    #             query.upper())),
    #     InlineQueryResultArticle(
    #         id=uuid4(),
    #         title="Bold",
    #         input_message_content=InputTextMessageContent(
    #             "*{}*".format(escape_markdown(query)),
    #             parse_mode=ParseMode.MARKDOWN)),
    #     InlineQueryResultArticle(
    #         id=uuid4(),
    #         title="Italic",
    #         input_message_content=InputTextMessageContent(
    #             "_{}_".format(escape_markdown(query)),
    #             parse_mode=ParseMode.MARKDOWN))]


    update.inline_query.answer(results)


mybank_handler = InlineQueryHandler(query_my_bank)
dispatcher.add_handler(mybank_handler)

# fire up bot
update.start_polling()
