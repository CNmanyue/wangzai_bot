#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 21:37
# @Author  : zhouxw
# @File    : base.py
# @Software: PyCharm
import time


def time_stamp():
    return time.strftime("%Y%m%d%H%M%S")


class FddClient(object):
    def __init__(self, app_id, secret, host, v="2.0", api=""):
        self.app_id = app_id
        self.secret = secret
        self.host = host
        self.v = v
        self.api = api

    def api_url(self, addr):
        if not addr and isinstance(addr, str):
            raise ValueError("data can not be None.")
        if addr.find(".api") < 0:
            addr += ".api"

        return self.host + addr

    def invoke(self, **kw):
        pass
