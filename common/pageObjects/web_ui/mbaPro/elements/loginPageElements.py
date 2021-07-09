#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: loginPageElements.py
@time: 2021/7/9 0009 15:29
@desc:
'''
from common.pageObjects.createElement import CreateElement
from common.pageObjects.web_ui.wait_type import Wait_Type as Wait_By
from common.pageObjects.web_ui.locator_type import Locator_Type

class LoginPageElements:
    def __init__(self):
        self.path = '/'
        self.title = CreateElement.create(None, None, None, Wait_By.TITLE_IS, 'MBA智库资讯,汇聚中国主流的商业管理资讯')
        # 登录入口
        self.login_entrance = CreateElement.create(Locator_Type.XPATH, '//*[@id="Personal"]/a[1]', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 用户登录入口
        self.login_other_entrance = CreateElement.create(Locator_Type.XPATH, '//*[@id="userName_login"]/a/i', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 输入用户名
        self.login_username = CreateElement.create(Locator_Type.XPATH, '//*[@id="login-input-name"]', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 输入密码
        self.login_password = CreateElement.create(Locator_Type.XPATH, '//*[@id="login-input-pwd"]', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 勾选协议
        self.login_agreement = CreateElement.create(Locator_Type.XPATH, '//*[@id="check-contract"]', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 登录按钮
        self.login_button = CreateElement.create(Locator_Type.XPATH, '//*[@id="login_submit"]', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
