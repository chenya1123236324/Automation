#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: api_wechatApi_read_config.py
@time: 2021/7/1 0001 11:36
@desc:
'''
from common.baseob.api.wechatAPI.wechatApiConf import WechatApiConfig
import configparser as ConfigParser

class WechatApiReadConfig(object):
    __instance = None
    __inited = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config = self._readConf('conf/wechatApi/wechatApi.conf')
            self.__inited = True

    def _readConf(self, configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile, encoding='utf-8')
        wechatConfig = WechatApiConfig()
        wechatConfig.url = config.get('servers', 'url')
        wechatConfig.init = config.get('isInit', 'init')
        return wechatConfig
