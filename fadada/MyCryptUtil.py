#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 16:36
# @Author  : zhouxw
# @File    : MyCryptUtil.py
# @Software: PyCharm


"""
    $ pip install cryptography


"""

import base64
import binascii
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

original = b"abcdefghijklmnopqrstuvwxyz"


# test aes
def test_aes():
    print("-------------aes begin-------------")
    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(original) + encryptor.finalize()
    decryptor = cipher.decryptor()
    result = decryptor.update(ct) + decryptor.finalize()
    print(result)
    print(result.decode())


def test_3des():
    print("-------------3des begin-------------")
    backend = default_backend()
    alg = algorithms.TripleDES(b"tx6GyEM6VZ3ErWId0qizln6w")
    cipher = Cipher(alg, mode=modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    # ct = encryptor.update(b"a secret message") + encryptor.finalize()

    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(original)
    padded_data += padder.finalize()
    cryptograph_str = encryptor.update(padded_data)
    cryptograph_str += encryptor.finalize()
    cryptograph_str = cryptograph_str.hex().upper()
    print("加密结果：", cryptograph_str)

    decryptor = cipher.decryptor()
    # 将字符密文转字节
    cryptograph_b = binascii.a2b_hex(cryptograph_str.encode())
    ct = decryptor.update(cryptograph_b)
    ct += decryptor.finalize()
    print("解密结果：", ct.decode())


def test_padding():
    print("-------------padding begin-------------")
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(original)
    padded_data += padder.finalize()
    # print(type(padded_data))
    print(padded_data.hex())
    unpadder = padding.PKCS7(64).unpadder()
    data = unpadder.update(padded_data)
    data += unpadder.finalize()
    print(data.decode())


def test_md5():
    print("-------------md5 begin-------------")
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(original)
    md5_str = digest.finalize()
    print(type(md5_str))
    print(md5_str.hex().upper())


def test_sha1():
    print("-------------sha1 begin-------------")
    digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
    digest.update(original)
    sha1_str = digest.finalize()
    print(type(sha1_str))
    print(sha1_str.hex().upper())


def test_base64():
    print("-------------base64 begin-------------")
    b64_str = base64.b64encode(original)
    print(type(b64_str))
    print(b64_str.decode())


if __name__ == "__main__":
    # test_aes()
    test_padding()
    test_3des()
    test_md5()
    test_sha1()
    test_base64()
