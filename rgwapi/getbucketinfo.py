#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:getallinfo.py.py
@time:20-7-7 上午11:46
@desc:
'''


from mymain.mylib.cephs3.cephs3api import CephS3Api
from mymain.mylib.config.configinfo.sysconfig import SysConfig


if __name__ == "__main__":
    bucketname = SysConfig().getSampleBucket()
    cs = CephS3Api()
    with open('./bucketinfo.txt', 'w+') as f:
        for keyinfo in cs.getBucketsInfo(bucketname):
            #print(keyinfo)
            f.write(keyinfo)


    #bucketname = "lsl-bucket"
    # cs.deletaAllDataInBuckets(bucketname)
    # cs.createBucket(bucketname)
    # cs.getBucketsInfo(bucketname)
    # cs.deleteBuckets(bucketname)
    # filename = 'fa5a625b6d0121cd5503f074e407c69a5a5528605dd35a327762da4e80b9266f'
    # filepath = '/lovelsl/share/socketserver/socketserver/server/sserver/sencrypt/gmssl/libsm3/test.bin'
    # cs.uploadBigFile(bucketname, filename, filepath)