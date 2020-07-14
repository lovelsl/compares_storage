#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:sampletest.py
@time:20-7-7 下午6:58
@desc:
'''

from mymain.mylib.cephs3.cephs3api import CephS3Api
from mymain.mylib.config.configinfo.sysconfig import SysConfig


if __name__ == "__main__":
    bucketname = SysConfig().getSampleBucket()
    cs = CephS3Api()
    with open('./bucketinfo.txt', 'r') as f, open('./infotest.txt', 'w+') as fp:
        while True:
            sample = f.readline()
            if sample == None or sample == '':
                break
            s = sample.split('\t')
            sha256 = s[0]
            print(sha256)
            ret = cs.fileExists(bucketname, sha256)
            if ret == 0:
                fp.write(sample)

