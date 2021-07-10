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
import pytest
from assertpy import assert_that

@pytest.mark.usefixtures('start_session')
class TestLogin:
    # def setup_class(self):
    #     self.proClient = WebUIProClient()
    #     self.loginPage = LoginPage(self.proClient.browserOperator)

    def test_login_01(self, start_session):
        start_session[1].login_page("Imobs", 'imobs123')
        assert_that('MBA智库资讯,汇聚中国主流的商业管理资讯').is_equal_to(start_session[0].getTitle())



    #
    # def teardown_class(self):
    #     self.proClient.browserOperator.close()