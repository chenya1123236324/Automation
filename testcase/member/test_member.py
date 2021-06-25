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
from api.address_book.member_api import Member as member

@pytest.mark.usefixtures("get_token")
class TestMember:

    @pytest.mark.parametrize("userid, name, mobile, errcode, errmsg", member_api_data["create_member"])
    def test_01_create_member(self, get_token, userid, name, mobile, errcode, errmsg):
        req = member().create_member(get_token, userid, name, mobile)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")
