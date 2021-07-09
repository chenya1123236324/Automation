#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: web_ui_client.py
@time: 2021/7/9 0009 14:34
@desc:
'''
from common.base.read_web_ui_config import ReadWebUIConfig
from common.base.web_ui.webUtil.web_ui_pro_read_config import WebUIProReadConfig
from common.selenium.browserOperator import BrowserOperator
from common.selenium.driverUtil import DriverUtil

class WebUIProClient:
    def __init__(self):
        self.config = ReadWebUIConfig().web_ui_config
        self.proConfig = WebUIProReadConfig().config
        self.driver = DriverUtil.get_driver(self.config.selenium_hub, self.config.current_browser)
        self.driver.get(self.proConfig.web_host)
        self.browserOperator = BrowserOperator(self.driver)