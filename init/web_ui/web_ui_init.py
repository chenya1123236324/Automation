#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: web_ui_init.py
@time: 2021/7/9 0009 16:12
@desc:
'''
from init.web_ui.mbaPro.mbaProInit import MbaProInit

def web_ui_init():
    """
    初始化必要的数据
    :return:
    """
    # 初始化java依赖的libs

    # demoProject项目初始化
    MbaProInit().init()