#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: loginPage.py
@time: 2021/7/9 0009 15:37
@desc:
'''
from common.pageObjects.web_ui.mbaPro.elements.loginPageElements import LoginPageElements

class LoginPage:
    def __init__(self, browserOperator, title):
        self._browserOperator = browserOperator
        self._loginPageElements = LoginPageElements()
        self._loginPageElements.title.wait_expected_value = title
        self._browserOperator.explicit_wait_page_title(self._loginPageElements.title)
        self._browserOperator.get_screenshot('loginPage')

    # def _input_search_kw(self, kw):
    #     self._browserOperator.sendText(self._loginPageElements.search_input, kw)
    #     self._browserOperator.get_screenshot('input_search_kw')

    def _click_search_button(self):
        self._browserOperator.click(self._loginPageElements.login_entrance)
        self._browserOperator.get_screenshot('click_search_button')

    def login_kw(self):
        self._click_search_button()


    def getElements(self):
        return self._loginPageElements