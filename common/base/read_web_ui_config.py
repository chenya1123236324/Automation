#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: read_web_ui_config.py
@time: 2021/7/9 0009 14:23
@desc:
'''
from common.baseob.web_ui_config import WebUIConfig
import configparser as ConfigParser

class ReadWebUIConfig(object):
    __instance = None
    __inited = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.web_ui_config = self._readConfig('conf/web_ui_config.conf')
            self.__inited = True

    def _readConfig(self, configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile, encoding='utf-8')
        web_ui_config = WebUIConfig()
        web_ui_config.selenium_hub = config.get('selenium_server', 'selenium_hub')
        web_ui_config.test_workers = config.get('test', 'test_workers')
        web_ui_config.test_browsers = config.get('browser', 'test_browsers').split('||')
        web_ui_config.current_browser = config.get('browser', 'current_browser')
        web_ui_config.download_dir = config.get('browser', 'download_dir')
        web_ui_config.is_chrome_headless = config.get('browser', 'is_chrome_headless')
        web_ui_config.is_firefox_headless = config.get('browser', 'is_firefox_headless')
        return web_ui_config
