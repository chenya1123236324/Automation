#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: web_ui_pro_read_config.py
@time: 2021/7/9 0009 14:36
@desc:
'''
from common.baseob.web_ui.proConfig import ProConfig
import configparser as ConfigParser

class WebUIProReadConfig(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config=self._readConfig('conf/web_ui/web_ui_pro.conf')
            self.__inited=True

    def _readConfig(self, configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile,encoding='utf-8')
        demoProjectConfig = ProConfig()
        demoProjectConfig.web_host = config.get('servers','web_host')
        demoProjectConfig.init=config.get('isInit','init')
        return demoProjectConfig
