#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:mysha.py
@time:20-7-6 下午3:22
@desc:
'''


import hashlib

def sha1Hash(filepath):
    """

    :param filepath:  传入文件路径
    :return:
                返回hash字符串
    """
    sha = hashlib.sha1()
    with open(filepath, 'rb') as f:
        while True:
            content = f.readline()
            if not content:
                break
            sha.update(content)
    hash = sha.hexdigest()
    return hash


def sha256Hash(filepath):
    """

    :param filepath:  传入文件路径
    :return:
                返回hash字符串
    """
    sha = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            content = f.readline()
            if not content:
                break
            sha.update(content)
    hash = sha.hexdigest()
    return hash



