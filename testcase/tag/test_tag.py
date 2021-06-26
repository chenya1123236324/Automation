#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: test_tag.py
@time: 2021/6/26 0026 14:55
@desc:
'''
import pytest
from testcase.tag.conftest import tag_api_data
from api.address_book.tag_api import Tag

@pytest.mark.usefixtures("get_token")
class TestTag:
    tag = Tag()

    @pytest.mark.parametrize("tag_name, errcode, errmsg", tag_api_data["create_tag"])
    def test_01_create_tag(self, get_token, tag_name, errcode, errmsg):
        req = self.tag.create_tag(get_token, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("tag_id, tag_name, errcode, errmsg", tag_api_data["update_tag_name"])
    def test_02_update_tag_name(self, get_token, tag_id, tag_name, errcode, errmsg):
        req = self.tag.update_tag_name(get_token, tag_id, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("tag_id, errcode, errmsg", tag_api_data["delete_tag"])
    def test_03_delete_tag(self, get_token, tag_id, errcode, errmsg):
        req = self.tag.delete_tag(get_token, tag_id)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")