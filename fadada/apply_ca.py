#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 20:56
# @Author  : zhouxw
# @File    : apply_ca.py
# @Software: PyCharm


import requests

from fadada import base
from fadada import crypt_util
from fadada.config import configs


class Individual(base.FddClient):
    def invoke(self, name, id_card, mobile, email=""):
        time_stamp = base.time_stamp()
        sha1_inner = crypt_util.sha1_str(self.secret)
        md5 = crypt_util.md5_str(time_stamp)
        sha1_outer = crypt_util.sha1_str(self.app_id + md5 + sha1_inner)
        base64 = crypt_util.base64_str(sha1_outer)

        id_mobile = crypt_util.triple_des_str(self.secret, id_card + "|" + mobile)
        params = {
            "customer_name": name,
            "email": email,
            "ident_type": "",
            "id_mobile": id_mobile,
            "employee_id": "",

            "app_id": self.app_id,
            "timestamp": time_stamp,
            "v": self.v,
            "msg_digest": base64
        }
        r = requests.post(self.api_url("syncPerson_auto"), data=params)
        print(r.content.decode())


if __name__ == "__main__":
    client = configs["client"]
    personal = configs["personal"]

    individual = Individual(client["app_id"], client["secret"], client["host"])
    individual.invoke(personal["name"], personal["id_card"], personal["mobile"])
