#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:filepath.py
@time:20-6-1 上午10:24
@desc:
'''

import os


rootpath = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', '..'))
#rootpath = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'conf'))


def getConfFile():
    default_config_path = rootpath + os.sep + 'conf' + os.sep + 'sys.conf'
    default_config_path = os.path.normpath(default_config_path)
    # print(default_config_path)
    return default_config_path

def getLogFile():
    default_config_path = rootpath + os.sep + 'log' + os.sep + 'elastic.log'
    default_config_path = os.path.normpath(default_config_path)
    if os.path.isfile(default_config_path):
        os.mknod(default_config_path)

    # print(default_config_path)
    return default_config_path

def getCephConfigFlie():
    default_config_path = rootpath + os.sep + 'conf' + os.sep + 's3key.conf'
    default_config_path = os.path.normpath(default_config_path)
    # print(default_config_path)
    return default_config_path

def getCephBucketFlie():
    default_config_path = rootpath + os.sep + 'data' + os.sep + 'bucket.conf'
    default_config_path = os.path.normpath(default_config_path)
    # print(default_config_path)
    return default_config_path
