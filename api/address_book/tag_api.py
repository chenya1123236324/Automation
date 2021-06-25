#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: tag_api.py
@time: 2021/6/25 0025 17:45
@desc:
'''
from api.client import ApiRequest

class Tag(ApiRequest):
    def create_tag(self, token, tagname):
        url = f'/cgi-bin/tag/create?access_token={token}'
        data = {
            "tagname": tagname
        }
        req = self.post(url=url, json=data)
        return req

    def update_tag_name(self, token, tagid, tagname):
        url = f'/cgi-bin/tag/update?access_token={token}'
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        req = self.post(url=url, json=data)
        return req

    def delete_tag(self, token, tagid):
        url = f'/cgi-bin/tag/delete?access_token={token}&tagid={tagid}'
        req = self.get(url=url)
        return req

    def get_tag_member(self, token, tagid):
        url = f'/cgi-bin/tag/get?access_token={token}&tagid={tagid}'
        req = self.get(url=url)
        return req

    def add_tag_member(self, token, tagid, userlist=None, partylist=None):
        url = f'/cgi-bin/tag/addtagusers?access_token={token}'
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        req = self.post(url=url, json=data)
        return req
