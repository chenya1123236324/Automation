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