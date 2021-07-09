#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: searchPageElements.py
@time: 2021/7/9 0009 19:04
@desc:
'''
from common.pageObjects.createElement import CreateElement
from common.pageObjects.web_ui.wait_type import Wait_Type as Wait_By
from common.pageObjects.web_ui.locator_type import Locator_Type

class SearchPageElements:
    def __init__(self):
        self.path = '/'
        self.title = CreateElement.create(None, None, None, Wait_By.TITLE_IS)
        # 搜索输入框
        self.search_input = CreateElement.create(Locator_Type.XPATH, '/html/body/div[2]/div/div[2]/div/div[9]/div[1]/div[1]/form/div/div[2]/input', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        # 搜索按钮
        self.search_button = CreateElement.create(Locator_Type.XPATH, '/html/body/div[2]/div/div[2]/div/div[9]/div[1]/div[1]/form/div/div[1]/button', wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)

