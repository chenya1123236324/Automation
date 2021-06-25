#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: member_api.py
@time: 2021/6/25 0025 10:59
@desc:
'''
from api.client import ApiRequest

class Member(ApiRequest):

    def create_member(self, token, userid, name, mobile, department):
        url = f'/cgi-bin/user/create?access_token={token}'
        data = {
            "userid": userid,
            "name": name,
            "mobile" : mobile,
            "department": department
        }
        req = self.post(url=url, data=data)
        return req

if __name__ == '__main__':
    from api.tokens import WechatApi

    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'

    token = WechatApi().obtain_token(corpid,secret)
    req = Member()
    #token = 'Yc66zreFu8eUYNyjEnHb5ow9iNF-t1DPKTfqFG0Qmw7FuZNYG9XaASCyrgdAJKfW2iWilg4T0DPkCSze6ruqW1IG5q_wgaIMnBq52juVKCmldzjJi2OC5Rp0wWFzSaTzg9NPkCMJDSvBqHy_LJ8MDvtlGPtp9YHby61i8oYyJhdO57saykP94YfIDOIzSm7kwD5JMpSm5Q8ROzhfZJD3_A'
    print(req.create_member(token, "taikong", name="taikong", mobile="18144854881", department="1"))