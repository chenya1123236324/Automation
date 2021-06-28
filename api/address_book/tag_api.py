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
        """
        创建标签
        :param token:
        :param tagname: 标签名称
        :return:
        """
        url = f'/cgi-bin/tag/create?access_token={token}'
        data = {
            "tagname": tagname
        }
        req = self.post(url=url, json=data)
        return req

    def update_tag_name(self, token, tagid, tagname):
        """
        更新标签名称
        :param token:
        :param tagid: 标签ID
        :param tagname: 标签名城管
        :return:
        """
        url = f'/cgi-bin/tag/update?access_token={token}'
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        req = self.post(url=url, json=data)
        return req

    def delete_tag(self, token, tagid):
        """
        删除标签
        :param token:
        :param tagid: 标签ID
        :return:
        """
        url = f'/cgi-bin/tag/delete?access_token={token}&tagid={tagid}'
        req = self.get(url=url)
        return req

    def get_tag_list(self, token):
        """
        获取标签列表
        :param token:
        :return:
        """
        url = f'/cgi-bin/tag/list?access_token={token}'
        req = self.get(url=url)
        return req

    def get_tag_member(self, token, tagid):
        """
        获取标签成员
        :param token:
        :param tagid: 标签ID
        :return:
        """
        url = f'/cgi-bin/tag/get?access_token={token}&tagid={tagid}'
        req = self.get(url=url)
        return req

    def add_tag_member(self, token, tagid, userlist=None, partylist=None):
        """
        添加标签成员
        :param token:
        :param tagid:
        :param userlist: 企业成员ID列表
        :param partylist: 企业部门ID列表
        :return:
        """
        url = f'/cgi-bin/tag/addtagusers?access_token={token}'
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        req = self.post(url=url, json=data)
        return req

if __name__ == '__main__':
    from api.tokens import WechatApi

    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'

    token = WechatApi().obtain_token(corpid, secret)
    req = Tag()
    # 创建标签
    #print(req.create_tag(token, 'xiaotag'))
    # 更新标签名称
    # print(req.update_tag_name(token, 1, 'datag'))

    # 删除标签
    #print(req.delete_tag(token, 1))
    # 获取标签列表
    print(req.get_tag_list(token))

