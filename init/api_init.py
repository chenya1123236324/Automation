#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: api_init.py
@time: 2021/7/1 0001 11:21
@desc:
'''

from init.api.wechatApi.wechatInit import WechatApiInit

def api_init():
    """
    初始化必要的数据
    """
    # 初始化wechatApi项目基础数据
    WechatApiInit().init()