#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 14:14
# @Author  : zhouxw
# @File    : query.py
# @Software: PyCharm

from inline.repo.bank import banks


def query_bank(name):
    results = []
    for _name in banks.keys():
        if str(_name).find(name) > -1:
            results += banks.get(_name)

    return results


if __name__ == "__main__":
    for x in query_bank("银行"):
        print(x)

    print("xx")
