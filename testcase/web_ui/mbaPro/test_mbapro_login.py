#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: test_mbapro_login.py
@time: 2021/7/9 0009 15:45
@desc:
'''
from common.base.web_ui.webUtil.web_ui_client import WebUIProClient
from common.pageObjects.web_ui.mbaPro.pages.loginPage import LoginPage
from assertpy import assert_that

class TestLogin:
    def setup_class(self):
        self.proClient = WebUIProClient()
        self.loginPage = LoginPage(self.proClient.browserOperator)

    def test_login_01(self):
        self.loginPage.login_page("Imobs", 'imobs123')
        assert_that('MBA智库资讯,汇聚中国主流的商业管理资讯').is_equal_to(self.proClient.browserOperator.getTitle())




    def teardown_class(self):
        self.proClient.browserOperator.close()