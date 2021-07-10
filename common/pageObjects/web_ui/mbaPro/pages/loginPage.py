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
    def __init__(self, browserOperator):
        self._browserOperator = browserOperator
        self._loginPageElements = LoginPageElements()
        self._browserOperator.explicit_wait_page_title(self._loginPageElements.title)
        self._browserOperator.get_screenshot('loginPage')

    # def _input_search_kw(self, kw):
    #     self._browserOperator.sendText(self._loginPageElements.search_input, kw)
    #     self._browserOperator.get_screenshot('input_search_kw')

    def _click_login_entrance_button(self):
        self._browserOperator.click(self._loginPageElements.login_entrance)
        self._browserOperator.get_screenshot('click_login_entrance_button')

    def _click_login_other_button(self):
        self._browserOperator.click(self._loginPageElements.login_other_entrance)
        self._browserOperator.get_screenshot('click_login_other_button')

    def _input_login_username(self, username):
        self._browserOperator.sendText(self._loginPageElements.login_username, username)
        self._browserOperator.get_screenshot('input_username')

    def _input_login_password(self, password):
        self._browserOperator.sendText(self._loginPageElements.login_password, password)
        self._browserOperator.get_screenshot('input_password')

    def _click_login_agreement(self):
        self._browserOperator.click(self._loginPageElements.login_agreement)
        self._browserOperator.get_screenshot('click_login_agreement_button')

    def _click_login_button(self):
        self._browserOperator.click(self._loginPageElements.login_button)
        self._browserOperator.get_screenshot('click_login_button')


    def login_page(self, username, password):
        self._click_login_entrance_button()
        self._click_login_other_button()
        self._input_login_username(username)
        self._input_login_password(password)
        self._click_login_agreement()
        self._click_login_button()



    def getElements(self):
        return self._loginPageElements