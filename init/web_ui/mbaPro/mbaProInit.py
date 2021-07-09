#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: mbaProInit.py
@time: 2021/7/9 0009 16:09
@desc:
'''
from common.base.web_ui.webUtil.web_ui_pro_read_config import WebUIProReadConfig

class MbaProInit:
    def __init__(self):
        self._web_ui_mbaPro_read_config = WebUIProReadConfig().config

    def init(self):
        if int(self._web_ui_mbaPro_read_config.init)==0:
            return

        #每次测试前先清除上次构造的数据
        self._deinit()
        #初始化必要的数据，如在数据库中构建多种类型的账号，
        pass

    def _deinit(self):
        #清除构造的数据
        pass