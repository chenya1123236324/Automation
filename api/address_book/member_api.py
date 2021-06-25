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

    def create_member(self, token, userid, name, mobile, department=None):
        """创建成员"""
        url = f'/cgi-bin/user/create?access_token={token}'
        if department is None:
            department = "1"
        data = {
            "userid": userid,
            "name": name,
            "mobile" : mobile,
            "department": department
        }
        req = self.post(url=url, json=data)
        return req

    def get_member(self, token, userid):
        """读取成员"""
        url = f'/cgi-bin/user/get?access_token={token}&userid={userid}'
        req = self.get(url=url)
        return req

    def update_member(self, token, userid, name=None, mobile=None):
        """更新成员"""
        url = f'/cgi-bin/user/update?access_token={token}'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        req = self.post(url=url, json=data)
        return req

    def delete_member(self, token, userid):
        """删除成员"""
        url = f'/cgi-bin/user/delete?access_token={token}&userid={userid}'
        req = self.get(url=url)
        return req

    def batch_delete_member(self, token, useridlist):
        """批量删除成员"""
        url = f'/cgi-bin/user/batchdelete?access_token={token}'
        data = {
            "useridlist": useridlist
        }
        req = self.post(url=url, json=data)
        return req

    def get_department_member_details(self, token, department_id, fetch_child=0):
        """
        获取部门成员详情
        :param token:
        :param department_id: 部门id
        :param fetch_child: 1/0：是否递归获取子部门下面的成员
        :return:
        """
        url = f'/cgi-bin/user/list?access_token={token}&department_id={department_id}&fetch_child={fetch_child}'

        req = self.get(url)
        return req


if __name__ == '__main__':
    from api.tokens import WechatApi

    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'

    token = WechatApi().obtain_token(corpid,secret)
    req = Member()
    # 创建成员
    #print(req.create_member(token, "taikong", name="taikong", mobile="18144854883", department="1"))
    # print(req.create_member(token, "taikong1", name="taikong1", mobile="18144854882", department="1"))
    # 获取成员
    #print(req.get_member(token, "taikong"))
    # 更新成员
    #print(req.update_member(token, userid="taikong", mobile="18144854889"))
    # 删除成员
    #print(req.delete_member(token, "taikong"))
    # 批量删除成员
    #print(req.batch_delete_member(token, ["taikong", "taikong1"]))
    # 获取部门成员详情
    #print(req.get_department_member_details(token, 1))