#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: test_mbapro_search.py
@time: 2021/7/9 0009 19:14
@desc:
'''
# from common.base.web_ui.webUtil.web_ui_client import WebUIProClient
# from common.pageObjects.web_ui.mbaPro.pages.loginPage import LoginPage
import pytest
from common.pageObjects.web_ui.mbaPro.pages.searchPage import SearchPage
from assertpy import assert_that

@pytest.mark.usefixtures('start_module')
class TestSearch:

    # def setup_class(self):
    #     self.proClient = WebUIProClient()
    #     self.loginPage = LoginPage(self.proClient.browserOperator)
    #     self.searchPage = SearchPage(self.proClient.browserOperator, 'MBA智库资讯,汇聚中国主流的商业管理资讯')

    def test_search_01(self, start_module):
        start_module[1].login_page("Imobs", 'imobs123')

        # assert_that('MBA智库资讯,汇聚中国主流的商业管理资讯').is_equal_to(self.proClient.browserOperator.getTitle())
        SearchPage(start_module[0], 'MBA智库资讯,汇聚中国主流的商业管理资讯').search_kw("摸鱼")
        assert_that('搜索:摸鱼 - MBA智库资讯').is_equal_to(start_module[0].getTitle())

    # def teardown_class(self):
    #     self.proClient.browserOperator.close()