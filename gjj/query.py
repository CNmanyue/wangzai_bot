#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/9 11:46
# @Author  : zhouxw
# @File    : query.py
# @Software: PyCharm
# query_gjj.py

"""
    $ pip install pytesseract

    1. 使用requests，设置sessionid
    2. 使用了验证码识别技术（pytesseract,PIL,tesseract-ocr)
    pytesseract: https://github.com/madmaze/pytesseract 要设置Path，设置后要重启
    tesseract-ocr: https://github.com/UB-Mannheim/tesseract/wiki  要设置环境变量，设置后要重启
    params:
        argv[1] = 公积金帐号
        argv[2] = 身份证号码
"""

import os
# from datetime import datetime
import uuid
from io import BytesIO

import pytesseract
import requests
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
verify_code_dir = os.path.join(BASE_DIR, 'verify')

if not os.path.isdir(verify_code_dir):
    os.makedirs(verify_code_dir)


def query(acc_num, id_card):
    print("query szgjj, input data: acc_num=%s,id_card=%s" % (acc_num, id_card))
    # time = datetime.now().timestamp() * 10000000
    verify_code_path = os.path.join(verify_code_dir, uuid.uuid1().hex + '.png')
    print("验证码图片路径：", verify_code_path)

    verify_code_url = 'http://app.szzfgjj.com:7001/pages/code.jsp'
    r_verify_code = requests.get(verify_code_url)

    with open(verify_code_path, "wb") as f:
        f.write(r_verify_code.content)

    verify_code_img = Image.open(BytesIO(r_verify_code.content))
    verify_code_cookie = r_verify_code.cookies['JSESSIONID']

    # Example config: '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # verify_code_num = pytesseract.image_to_string(verify_code_img,config=tessdata_dir_config)
    verify_code_num = pytesseract.image_to_string(verify_code_img)
    print("验证码：", verify_code_num)

    query_url = 'http://app.szzfgjj.com:7001/accountQuery'
    payload = {'accnum': acc_num, 'certinum': id_card, 'qryflag': 1, 'verify': verify_code_num}
    r = requests.post(query_url, data=payload, cookies=dict(JSESSIONID=verify_code_cookie))
    rsp_content = parse_js(r.content.decode('utf-8'))
    print("结果：", rsp_content)
    if rsp_content["success"] == "false":
        return rsp_content["msg"]
    # rJson = json.loads(rStr)
    return "您的公积金帐户[%s]余额为：￥%s" % (rsp_content["newaccnum"], rsp_content["msg"])


def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    import ast
    m = ast.parse(expr)
    a = m.body[0]

    def parse(node):
        if isinstance(node, ast.Expr):
            return parse(node.value)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Dict):
            return dict(zip(map(parse, node.keys), map(parse, node.values)))
        elif isinstance(node, ast.List):
            return map(parse, node.elts)
        else:
            raise NotImplementedError(node.__class__)

    return parse(a)
