#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: run_api_test.py
@time: 2021/7/1 0001 11:10
@desc:
'''
import argparse
#from common.pytest import deal_pytest_ini_file
from common.datetimeutil import DateTimeUtil
from init.api_init import api_init

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-k', '--keyword', help='只执行匹配关键字的用例，会匹配文件名、类名、方法名', type=str)
    # parser.add_argument('-d', '--dir', help='指定要测试的目录', type=str)
    # args = parser.parse_args()
    #
    # # 处理pytest文件
    # deal_pytest_ini_file()

    # 初始化
    print('%s开始初始化......' % DateTimeUtil.getNowTime())
    api_init()
    print('%s初始化完成......' % DateTimeUtil.getNowTime())