#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:folderwalk.py
@time:20-7-6 下午3:43
@desc:
'''


import os


from mymain.mylib.config.configinfo.sysconfig import SysConfig
from mymain.mylib.config.configins.filepath import getCephBucketFlie
from mymain.mylib.encry.myhash import sha256Hash
from mymain.mylib.cephs3.cephs3api import CephS3Api


class FolderWalk():

    def __init__(self):
        self._getRecordFile()
        self._getDstFolder()
        self._getCephInfo()
        pass

    def _getDstFolder(self):
        self.path = SysConfig().getSampleFolder()

    def _getRecordFile(self):
        self.rpath = getCephBucketFlie()
        if os.path.exists(self.rpath):
            os.remove(self.rpath)

    def _getCephInfo(self):
        self.ceph = CephS3Api()
        self.bucket = SysConfig().getSampleBucket()

    def _uploadFile(self, bucketname, filename, filepath):
        """
            将文件上传给ceph
        :param bucketname:
        :param filepath:   样本名不一定具有唯一性
        :param filename:   sha256做为文件名，用于唯一定位样本
        :return:
        """
        #ceph = CephS3Api()
        filesize = os.path.getsize(filepath)
        if filesize > 5 * 1024 * 1024:
            self.ceph.uploadBigFile(bucketname, filename, filepath)
        else:
            with open(filepath, 'rb') as f:
                filecontent = f.read()
            self.ceph.uploadFile(bucketname, filename, filecontent)

    def folderWalk(self):
        """
            将指定路径下的所有文件上传到ceph的指定bucket中
            bucket key为文件sha256
        :return:
        """
        fp = open(self.rpath, 'w+')
        for root, dirs, files in os.walk(self.path):
            for file in files:
                absfile = os.path.join(root, file)
                hash = sha256Hash(absfile)
                data = '{0}, {1}, {2} \n'.format(self.bucket, hash, absfile)
                fp.write(data)
                self._uploadFile(self.bucket, hash, absfile)
        fp.close()

