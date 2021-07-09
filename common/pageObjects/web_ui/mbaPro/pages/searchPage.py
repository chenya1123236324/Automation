#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: searchPage.py
@time: 2021/7/9 0009 19:09
@desc:
'''
from common.pageObjects.web_ui.mbaPro.elements.searchPageElements import SearchPageElements

class SearchPage:
    def __init__(self, browserOperator, title):
        self._browserOperator = browserOperator
        self._searchPageElements = SearchPageElements()
        self._searchPageElements.title.wait_expected_value = title
        self._browserOperator.explicit_wait_page_title(self._searchPageElements.title)
        self._browserOperator.get_screenshot('searchPage')

    def _input_search_kw(self, kw):
        self._browserOperator.sendText(self._searchPageElements.search_input, kw)
        self._browserOperator.get_screenshot('input_search_kw')

    def _click_search_button(self):
        self._browserOperator.click(self._searchPageElements.search_button)
        self._browserOperator.get_screenshot('click_search_button')

    def search_kw(self, kw):
        self._input_search_kw(kw)
        self._click_search_button()

    def getElements(self):
        return self._searchPageElements