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

from common.pageObjects.web_ui.mbaPro.pages.loginPage import LoginPage

@pytest.fixture(scope='class')
def start_module(project_module_start):
    print("==========开始执行测试用例集===========")
    global driver
    driver = project_module_start[1]

    lg = LoginPage(driver)
    yield (driver, lg)
    print("==========结束执行测试用例集===========")
    project_module_start[0].browserOperator.close()

@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver lg
    '''
    print("==========开始执行测试用例集===========")
    global driver
    driver = project_session_start[1]

    print("-------------------- " + str(driver) + " ------------------------")

    lg = LoginPage(driver)
    yield (driver,lg)
    project_session_start[0].browserOperator.close()
    print("==========结束执行测试用例集===========")