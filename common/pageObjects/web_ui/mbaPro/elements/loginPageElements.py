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
