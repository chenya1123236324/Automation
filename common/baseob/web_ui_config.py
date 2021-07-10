#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: web_ui_config.py
@time: 2021/7/9 0009 14:25
@desc:
'''
class WebUIConfig:
    def __init__(self):
        self.selenium_hub=None
        self.selenium_hub_port=None
        self.test_workers=None
        self.test_browsers=[]
        self.current_browser=None
        self.download_dir = None
        self.is_chrome_headless = None
        self.is_firefox_headless = None