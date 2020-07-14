#!/usr/bin/env python
# encoding: utf-8
'''
@author:lsl
@license:(C) Copyright 2017-2018 
@contact:
@software:
@file:comconfig.py
@time:20-6-2 上午9:38
@desc:
'''


import sys


if sys.version_info >= (3, 0):
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser



#from rgwapi.main.lib.config.filepath import getConfFile
from .filepath import getConfFile

# 通用配置方式
class CommonConfig(object):
    def __init__(self, config_path=getConfFile()):
        self.config = ConfigParser()
        self.config_path = config_path

        if config_path:
            self.config.read(config_path)
        else:
            raise Exception
            # print self.config.get('center', 'uid')

    def getallsections(self):
        """
            列表形式返回
        :return:
        """
        return self.config.sections()

    # 判断指定的section是否存在
    def hassection(self, name):
        if self.config.has_section(name):
            return True
        else:
            return False

    # 判断指定的option是否存在
    def hasoption(self, section, option):
        if self.config.has_option(section, option):
            return True
        else:
            return False

    # 为配置文件增加名为name的section
    def addsection(self, name):
        if self.hassection(name):
            return
        self.config.add_section(name)

    # 获取指定section的option选项值
    def getvalue(self, name, option):
        return self.config.get(name, option)

    # 配置指定section下option的值
    def setvalue(self, name, option, value):
        self.config.set(name, option, value)

    # 保存配置文件的修改
    def savevalue(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

if __name__ == "__main__":
    cc = CommonConfig()
    print(cc.getallsections())
