#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: logger.py
@time: 2021/6/24 0024 17:40
@desc:
'''
from common import BASE_PATH
import logging
import os
import datetime

def logFile(fileName, output='all'):
    # 设置路径
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    path_file = BASE_PATH + r'\logs\{}_{}.log'.format(fileName, now_time).replace(r'\/'.replace(os.sep, ''), os.sep)
    # 设置日志器
    log = logging.getLogger()
    log.setLevel(level=logging.INFO)
    # 设置格式器
    streanFormatter = logging.Formatter(fmt='[%(asctime)s]：[%(levelname)s] '
                                            '->>%(message)s')
    fileFormatter = logging.Formatter(fmt='[%(filename)s]: [%(levelname)s] '
                                          '[%(asctime)s] ''line:%(lineno)d->>%(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
    # 设置控制台处理器
    s_hand = logging.StreamHandler()
    s_hand.setLevel(logging.ERROR)  # 设置处理器级别
    s_hand.setFormatter(streanFormatter)  # 添加控制台格式器
    # 设置文件处理器
    f_hand = logging.FileHandler(filename=path_file, encoding='utf-8')
    f_hand.setLevel(logging.INFO)  # 设置处理器级别
    f_hand.setFormatter(fileFormatter)  # 添加文件格式器

    if output == "all":
        # 日志器添加控制台处理器
        log.addHandler(s_hand)
        # 日志器添加文件处理器
        log.addHandler(f_hand)
        return log
    elif output == 'strean':
        log.addHandler(s_hand)
        return log
    elif output == 'file':
        log.addHandler(f_hand)
        return log
    else:
        raise ValueError("output参数错误")


logger = logFile('接口测试', output='file')

# logger.critical('critical严重错误')
# logger.error('error错误')
# logger.warning('warning警告')
# logger.info('info信息')
# logger.debug('debug调试日志')
