#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: conftest.py
@time: 2021/7/10 0010 16:42
@desc:
'''
import pytest

from common.base.web_ui.webUtil.web_ui_client import WebUIProClient

driver = None

@pytest.fixture(scope='session')
def project_session_start():
    print("==========开始 UI自动化项目 执行测试===========")
    global driver
    proClient = WebUIProClient()
    driver = proClient.browserOperator
    yield proClient, driver
    print("==========结束 UI自动化项目 测试===========")

@pytest.fixture(scope='module')
def project_module_start():
    print("==========开始 XX模块 执行测试===========")
    global driver
    proClient = WebUIProClient()
    driver = proClient.browserOperator

    yield proClient, driver

    print("==========结束 XX模块 测试===========")

def pytest_configure(config):
    # 标签名集合
    marker_list = ['smoke', 'lucas']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)