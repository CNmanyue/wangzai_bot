#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 19:58
# @Author  : zhouxw
# @File    : joke_repo.py
# @Software: PyCharm

"""
    1. pip install requests


"""

import json
import os
import random
import time

import requests

# dd/mm/yyyy格式
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
joke_dir = os.path.join(BASE_DIR, 'joke_repo')
date = time.strftime("%Y-%m-%d")
joke_path = os.path.join(joke_dir, date + '.txt')


# 确保当天已经下载过笑话
def init():
    if not os.path.exists(joke_path):
        r = requests.get("http://api.laifudao.com/open/xiaohua.json")
        json_data = r.json()
        # print(json_data)
        with open(joke_path, "w", encoding="utf-8") as f:
            for joke in json_data:
                f.write(json.dumps(joke, ensure_ascii=False) + "\n")


def get_joke(*random_num):
    init()
    if not random_num:
        random_num = random.randint(0, 19)
        print("系统随机选择笑话编号：" + str(random_num))
    f = open(joke_path, "r", encoding="utf-8")
    # joke_repo = "this is a joke_repo"
    for index, line in enumerate(f.readlines()):
        if index == random_num:
            return joint_joke(json.loads(line))


def joint_joke(joke):
    return joke["title"] + "\r\n" + str(joke["content"]).replace("<br/><br/>", "\r\n")


if __name__ == "__main__":
    get_joke(9)
