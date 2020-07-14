#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:test.py.py
@time:20-7-6 上午9:29
@desc:
'''

import os
import math
import boto
import boto.s3.connection
from filechunkio import FileChunkIO

access_key = "NBCGVUXBWLEL7FBVUTDG"
secret_key = "eK08vp15NS68PNsgMJdIy5Gj4X9HsPT4lYWSuASs"

host = '192.168.0.131'
port = 7480


class CephS3Api():
    def __init__(self):
        self.access_key = access_key
        self.secret_key = secret_key
        self._getConn()

    def _getConn(self):
        self.conn = boto.connect_s3(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                host=host,
                port=port,
                is_secure=False,               # uncomment if you are not using ssl
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )

    #创建bucket
    #bucketname 字符串  字母和数字组成
    def createBucket(self, bucketname):
        bucket = self.conn.create_bucket(bucketname)
        #print(bucket)

    #获取所有buckets
    def getAllBuckets(self):
        for bucket in self.conn.get_all_buckets():
            print ("{name}\t{created}".format(
                name=bucket.name,
                created=bucket.creation_date,
            ))

    #获取buckets中的所有对象 key
    # bucketname 字符串  字母和数字组成
    def getBucketsInfo(self, bucketname):
        bucket = self.conn.get_bucket(bucketname)
        for key in bucket.list():
            info = "{name}\t{size}\t{modified}".format(
                name=key.name,
                size=key.size,
                modified=key.last_modified,
            )
            print(info)

    #获取bucket中某一个文件对象的基本属性，如文件大小，最后修改时间等
    # bucketname 字符串  字母和数字组成
    # filename 字符串  字母和数字组成
    def getFileInfo(self, bucketname, filename):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        #print(dir(key))
        dic = {
            "size": key.size,
            "modifield":key.last_modified,
        }
        return dic

    #删除Buckets之前，必须保证内部的key已经 全部删除
    # bucketname 字符串  字母和数字组成
    def deleteBuckets(self, bucketname):
        self.conn.delete_bucket(bucketname)

    #上传文件
    # bucketname   字符串  字母和数字组成
    # filename     字符串  字母和数字组成
    # filecontent  整个文件内容
    def uploadFile(self, bucketname, filename, filecontent):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        if key != None:
            return 1
        key = bucket.new_key(filename)
        key.set_contents_from_string(filecontent)

    #下载文件
    def downloadFile(self, bucketname, filename, storepath):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        key.get_contents_to_filename(storepath)

    #删除文件
    def deleteFile(self, bucketname, filename):
        bucket = self.conn.get_bucket(bucketname)
        bucket.delete_key(filename)

    #下载文件的url
    def downloadUrl(self, bucketname, filename):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        url = key.generate_url(0, query_auth=False, force_http=True)
        #0 url有效访问时长
        #False url是否需要使用签名验证有效性
        return url

    #使用s3协议的客户端，都可以读取数据
    def setAclRead(self, bucketname, filename):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        key.set_canned_acl('public-read')

    #取消s3客户端访问权限
    def setAclPrivate(self, bucketname, filename):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        key.set_canned_acl('private')

    #上传一个大文件 -- 分段上传
    def uploadBigFile(self, bucketname, filename, filepath):
        bucket = self.conn.get_bucket(bucketname)
        key = bucket.get_key(filename)
        if key != None:
            return 1

        chunksize = 1024 * 1024 * 5 #2M
        filesize = os.path.getsize(filepath)
        chunkcnt = int(math.ceil(filesize * 1.0 / chunksize))

        mp = bucket.initiate_multipart_upload(filename)  # 创建Multipart对象
        for i in range(0, chunkcnt):
            offset = chunksize * i
            len = min(chunksize, filesize - offset)
            fp = FileChunkIO(filepath, 'r', offset=offset, bytes=len)  # 创建文件的分段
            mp.upload_part_from_file(fp, part_num=i + 1)  # 上传每个分段
        mp.complete_upload()

    #下载一个大文件 -- 分段下载文件
    def downloadBigFile(self, bucketname, filename, filepath):
        chunksize = 1024 * 1024 * 5  # 5M
        info = s3.getFileInfo(bucketname, bigfilename)
        filesize = info['size']
        chunkcnt = int(math.ceil(filesize * 1.0 / chunksize))

        fp = open(filepath, 'wb+')
        for i in range(0, chunkcnt):
            offset = chunksize * i
            len = min(chunksize, filesize - offset)
            resp = self.conn.make_request("GET", bucketname, filename,
                                     headers={"Range": "bytes=%d-%d" % (offset, offset + len)})
            data = resp.read(len)
            if data == "":
                break
            fp.write(data)
        fp.close()

if __name__ == "__main__":
    s3 = CephS3Api()
    bucketname = "lsl-bucket"
    s3.createBucket(bucketname)


    filename = "moon.jpg"
    with open("./" + filename, 'rb') as f:
        filecontent = f.read()
    s3.uploadFile(bucketname, filename, filecontent)

    #s3.getBucketsInfo(bucketname)

    s3.downloadFile(bucketname, filename, './m.jpg')
    s3.deleteFile(bucketname, filename)
    os._exit(1)

    url = s3.downloadUrl(bucketname, filename)
    print(url)

    s3.setAclRead(bucketname, filename)
    #http://192.168.0.131:7480/lsl-bucket/moon.jpg   可访问

    bigfilename = 'viruslib.zip'
    bigfilepath = './' + bigfilename
    s3.uploadBigFile(bucketname, bigfilename, bigfilepath)
    url = s3.downloadUrl(bucketname, bigfilename)
    print(url)  #http://192.168.0.131:7480/lsl-bucket/viruslib.zip
    s3.setAclRead(bucketname, bigfilename)

    s3.downloadBigFile(bucketname,  bigfilename, './virus.test')
    #info = s3.getFileInfo(bucketname, bigfilename)
    #print(info)
