#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: conftest.py
@time: 2021/6/25 0025 18:17
@desc:
'''
import pytest
from api.tokens import WechatApi


@pytest.fixture()
def get_token():
    init = WechatApi()
    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'
    token = init.obtain_token(corpid, secret)
    yield token

def pytest_collection_modifyitems(items):
    """
    pytest 测试用例参数化时用例名称有中文名，输出控制台和HTML测试报告unicpode编码问题
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        # 只需要对中括号内的数据做一个编码转换即可，防止因为测试用例本身就是中文导致编码再出问题
        names = item.name.split("[")
        nodeids = item.nodeid.split("[")
        if len(names) > 1:
            item.name = names[0] + "[" + names[-1].encode("utf-8").decode("unicode_escape")
        if len(nodeids) > 1:
            # 报告里用例名称用的是nodeis所以nodeid也需要转换一下
            item._nodeid = nodeids[0] + "[" + nodeids[-1].encode("utf-8").decode("unicode_escape")