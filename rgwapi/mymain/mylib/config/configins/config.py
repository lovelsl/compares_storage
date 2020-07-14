# -*- coding: utf-8 -*-

from configparser import ConfigParser

class Dictionary(dict):
    """KV custom dict."""
    def __getattr__(self, key):
        return self.get(key, None)
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Config(object):
    '''
    获取分析配置文件
    '''

    def __init__(self, fpath=None):
        self.path = fpath
        self.config = ConfigParser()

        if self.path:
            self.config.read(self.path)
        else:
            raise FileNotFoundError('config.conf file not found')
        #print("1",self.path)

        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for name, raw_value in self.config.items(section):
                try:
                    if self.config.get(section, name) in ["0", "1"]:
                        raise (ValueError)

                    value = self.config.getboolean(section, name)
                except ValueError:
                    try:
                        value = self.config.getint(section, name)

                    except ValueError:
                        value = self.config.get(section, name)
                setattr(getattr(self, section), name, value)


if __name__ == "__main__":
    #from .filepath import getConfFile
    cfg =Config(fpath='G:\proj-company\socketserver\conf\server.conf')
    print(dir(cfg))
    print(cfg.socketserver.ip)
    print(cfg.socketserver.port)
    print(cfg.log.level)

