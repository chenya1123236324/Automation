#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: test_member.py
@time: 2021/6/25 0025 18:08
@desc:
'''
import pytest
from testcase.member.conftest import member_api_data
from api.address_book.member_api import Member

@pytest.mark.usefixtures("get_token")
class TestMember:
    member = Member()

    @pytest.mark.parametrize("userid, name, mobile, errcode, errmsg", member_api_data["create_member"])
    def test_01_create_member(self, get_token, userid, name, mobile, errcode, errmsg):
        req = self.member.create_member(get_token, userid, name, mobile)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("userid, errcode, errmsg", member_api_data["get_member"])
    def test_02_get_member(self, get_token, userid, errcode, errmsg):
        req = self.member.get_member(get_token, userid)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("userid, name, mobile, errcode, errmsg", member_api_data["update_member"])
    def test_03_update_member(self, get_token, userid, name, mobile, errcode, errmsg):
        # TODO api文档说明手机号与邮箱不能同时为空，由于此处并没有定义邮箱，则手机号不能为空，成员名称也不能为空
        req = self.member.update_member(get_token, userid, name, mobile)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("userid, errcode, errmsg", member_api_data["delete_member"])
    def test_04_delete_member(self, get_token, userid, errcode, errmsg):
        req = self.member.delete_member(get_token, userid)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("useridlist, errcode, errmsg", member_api_data["batch_delete_member"])
    def test_05_batch_delete_member(self, get_token, useridlist, errcode, errmsg):
        req = self.member.batch_delete_member(get_token, useridlist)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("department_id, fetch_child, errcode, errmsg", member_api_data["get_department_member_details"])
    def test_06_get_department_member_details(self, get_token, department_id, fetch_child, errcode, errmsg):
        req = self.member.get_department_member_details(get_token, department_id, fetch_child)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")