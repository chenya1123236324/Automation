#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: read_report_config.py
@time: 2021/7/3 0003 22:07
@desc:
'''
from common.baseob.report_config import ReportConfig
import configparser as ConfigPaser

class ReadReportConfig(object):
    __instance = None
    __inited = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.report_config = self._readConfig('conf/wechatApi/report.conf')
            self.__inited = True

    def _readConfig(self, configFile):
        configParser = ConfigPaser.ConfigParser()
        configParser.read(configFile, encoding='utf-8')
        report_config = ReportConfig()
        report_config.api_port = configParser.get('api', 'api_port')
        return report_config
