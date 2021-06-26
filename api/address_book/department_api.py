#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: department_api.py
@time: 2021/6/25 0025 17:09
@desc:
'''
from api.client import ApiRequest

class Department(ApiRequest):
    def create_department(self, token, parentId, name):
        """
        创建部门
        :param token:
        :param parentId: 父部门ID
        :param name: 部门名称
        :return:
        """
        url = f'/cgi-bin/department/create?access_token={token}'
        data = {
            "parentid": parentId,
            "name": name
        }
        req = self.post(url=url, json=data)

        return req

    def update_department(self, token, id, name=None):
        """
        更新部门
        :param token:
        :param id: 部门ID
        :param name: 部门名称
        :return:
        """
        url = f'/cgi-bin/department/update?access_token={token}'
        data = {
            "id": id,
            "name": name
        }
        req = self.post(url=url, json=data)
        return req

    def delete_department(self, token, id):
        """
        删除部门
        :param token:
        :param id: 部门ID
        :return:
        """
        url = f'/cgi-bin/department/delete?access_token={token}&id={id}'
        req = self.get(url=url)
        return req

    def get_department_list(self, token, id=None):
        """
        获取部门列表
        :param token:
        :param id: 部门ID
        :return:
        """
        url = f'/cgi-bin/department/list?access_token={token}&id={id}'
        req = self.get(url=url)
        return req

if __name__ == '__main__':
    from api.tokens import WechatApi

    corpid = 'wwb4f39b63b59a8a3a'
    secret = 'Oyc2BalKGSP1KCmdld0P2urxPOJCTcDV91mLMIRb_wA'

    token = WechatApi().obtain_token(corpid, secret)
    req = Department()
    # 创建部门
    print(req.create_department(token, 1, '广州研发中心'))
    # 更新部门
    # print(req.update_department(token, 2, '深圳研发中心'))
    # 删除部门
    print(req.delete_department(token, 2))
    # 获取部门列表
    #print(req.get_department_list(token, 1))
