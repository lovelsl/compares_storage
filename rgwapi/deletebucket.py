#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:deletebucket.py
@time:20-7-7 上午11:50
@desc:
'''

from mymain.mylib.cephs3.cephs3api import CephS3Api
from mymain.mylib.config.configinfo.sysconfig import SysConfig


if __name__ == "__main__":
    bucketname = SysConfig().getSampleBucket()
    cs = CephS3Api()
    #cs.getBucketsInfo(bucketname)
    cs.deletaAllDataInBuckets(bucketname)
    cs.deleteBuckets(bucketname)

