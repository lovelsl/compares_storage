#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:sysconfig.py.py
@time:20-7-6 下午4:06
@desc:
'''



from ..configins.filepath import getConfFile
from ..configins.comconfig import CommonConfig


class SysConfig():

    def __init__(self, file=getConfFile()):
        self.cfg = CommonConfig(config_path=file)
        pass

    def getSampleFolder(self):
        try:
            path = self.cfg.getvalue("sys", "path")
        except:
            return ""
        return path

    def getSampleBucket(self):
        try:
            bucket = self.cfg.getvalue("sys", "bucket")
        except:
            return "test"
        return bucket

