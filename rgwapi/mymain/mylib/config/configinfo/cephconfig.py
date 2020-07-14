#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:syncconfig.py
@time:20-6-5 下午2:53
@desc:
'''


from ..configins.filepath import getCephConfigFlie
from ..configins.comconfig import CommonConfig


class CephConfig():

    def __init__(self, file=getCephConfigFlie()):
        self.cfg = CommonConfig(config_path=file)
        pass

    def getCephHost(self):
        try:
            host = self.cfg.getvalue("ceph", "host")
        except:
            return "127.0.0.1"
        return host

    def getCephPort(self):
        try:
            port = self.cfg.getvalue("ceph", "port")
            port = int(port)
        except:
            return 7480
        return port

    def getCephAccess(self):
        try:
            access_key = self.cfg.getvalue("ceph", "access_key")
        except:
            return ""
        return access_key

    def getCephSecret(self):
        try:
            secret_key = self.cfg.getvalue("ceph", "secret_key")
        except:
            return ""
        return secret_key
