#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:downloadfile.py
@time:20-7-9 下午4:34
@desc:
'''


from mymain.mylib.cephs3.cephs3api import CephS3Api
from mymain.mylib.config.configinfo.sysconfig import SysConfig


if __name__ == "__main__":
    bucketname = SysConfig().getSampleBucket()
    cs = CephS3Api()
    #cs.createBucket(bucketname)
    filename = 'Hash1.1.exe'
    cs.downloadFile(bucketname, filename, "./hash")
