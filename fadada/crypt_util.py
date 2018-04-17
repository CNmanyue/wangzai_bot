#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 16:36
# @Author  : zhouxw
# @File    : crypt_util.py
# @Software: PyCharm


"""
    $ pip install cryptography


"""

import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# test aes
def aes(original):
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


def triple_des_str(key, original):
    """
    :param key:
    :param original:
    :return: str
    """
    if not original and not isinstance(original, str):
        return None
    if not key and not isinstance(key, str):
        return None
    backend = default_backend()
    alg = algorithms.TripleDES(key.encode())
    cipher = Cipher(alg, mode=modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(original.encode())
    padded_data += padder.finalize()
    cryptograph_str = encryptor.update(padded_data)
    cryptograph_str += encryptor.finalize()
    cryptograph_str = cryptograph_str.hex().upper()
    return cryptograph_str


def md5_str(original):
    if not original and not isinstance(original, str):
        return None
    digest = hashes.Hash(hashes.MD5(), backend=default_backend())
    digest.update(original.encode())
    md5_str = digest.finalize()
    return md5_str.hex().upper()


def sha1_str(original):
    if not original and not isinstance(original, str):
        return None
    digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
    digest.update(original.encode())
    sha1_str = digest.finalize()
    return sha1_str.hex().upper()


def base64_str(original):
    if not original and not isinstance(original, str):
        return None
    b64_str = base64.b64encode(original.encode())
    return b64_str.decode()
