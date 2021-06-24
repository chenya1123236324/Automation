#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: read_config.py
@time: 2021/6/24 0024 17:16
@desc:
'''
import os
import yaml
from configparser import ConfigParser
from common import BASE_PATH

class LoadConfParser(ConfigParser):
    '''
    重写 configparser 中的 optionxform 函数
    解决 .ini 文件中的 键option 自动转为小写的问题
    '''

    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr: str) -> str:
        return optionstr

def load_yaml(filePath):
    """
    读取yaml文件
    :param filePath:
    :return:
    """
    with open(filePath, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data

def load_file(fileName, path=BASE_PATH):
    """
    项目加载指定文件
    :param fileName:
    :param path:
    :return:
    """
    folder_path = os.listdir(path)
    for file in folder_path:
        # 将目录和文件名拼接
        c_path = os.path.join(path, file)
        # 如果是目录则继续调用
        if os.path.isdir(c_path):
            data = load_file(fileName, c_path)
            if data is not None:
                return data
        elif fileName == file:
            data = load_yaml(c_path)
            return data


def load_ini(section, filePath=BASE_PATH + r'\conf\config.ini'):
    """
    读取ini配置文件
    :param section:
    :param filePath:
    :return: 键值对
    """
    filePath = filePath.replace(r'\/'.replace(os.sep, ''), os.sep)
    conf = LoadConfParser()
    conf.read(filePath, encoding='utf-8')
    load_data = dict(conf.items(section))
    return load_data

if __name__ == '__main__':
    data =load_file('test.yaml')
    print(data)
