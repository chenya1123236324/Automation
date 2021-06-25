#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: tokens.py
@time: 2021/6/25 0025 10:33
@desc:
'''
from api.client import ApiRequest
class WechatApi(ApiRequest):
    def __init__(self):
        super(WechatApi, self).__init__()

    def obtain_token(self, corpid, secret):
        params = f'/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}'
        req = self.get(params)
        return req.get("access_token")

if __name__ == '__main__':
    req = WechatApi()
    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'
    print(req.obtain_token(corpid, secret))