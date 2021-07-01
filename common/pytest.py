#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: pytest.py
@time: 2021/7/1 0001 11:09
@desc:
'''
import platform
#from common import BASE_PATH


def deal_pytest_ini_file():
    """
    由于当前(2020/1/15)pytest运行指定的pytest.ini在Windows下编码有bug，故对不同环境进行处理
    """
    with open('conf/pytest.conf','r',encoding='utf-8') as pytest_f:
        content=pytest_f.read()
        if 'Windows'==platform.system():
            with open('conf/pytest.ini','w+',encoding='gbk') as tmp_pytest_f:
                tmp_pytest_f.write(content)
                tmp_pytest_f.close()
        else:
            with open('conf/pytest.ini','w+',encoding='utf-8') as tmp_pytest_f:
                tmp_pytest_f.write(content)
                tmp_pytest_f.close()
        pytest_f.close()