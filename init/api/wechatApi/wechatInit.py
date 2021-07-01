#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: wechatInit.py
@time: 2021/7/1 0001 11:23
@desc:
'''
from common.base.api.api_wechatApi_read_config import WechatApiReadConfig
class WechatApiInit:
    def __init__(self):
        self._api_wechat_read_config = WechatApiReadConfig().config

    def init(self):
        if int(self._api_wechat_read_config.init) == 0:
            return
        # 每次测试前先清除上次构造的数据
        self._deinit()

        # 初始化必要的数据，如在数据库中构建多种类型的账号
        pass

    def _deinit(self):
        # 清除构造的数据
        pass