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
import allure
from testcase.tag.conftest import tag_api_data
from api.address_book.tag_api import Tag
from takes.takes import obtain_response

@allure.epic("通讯录接口测试")
@allure.feature("标签管理")
@pytest.mark.usefixtures("get_token")
class TestTag:
    tag = Tag()

    @allure.story("用例--创建标签")
    @allure.description("该用例是针对通讯录管理下的标签管理 创建标签接口的测试")
    @pytest.mark.parametrize("tag_name, errcode, errmsg", tag_api_data["create_tag"])
    def test_01_create_tag(self, get_token, tag_name, errcode, errmsg):
        """创建标签"""
        req = self.tag.create_tag(get_token, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--更新标签名称")
    @allure.description("该用例是针对通讯录管理下的标签管理 更新标签名称接口的测试")
    @pytest.mark.parametrize("tag_id, tag_name, errcode, errmsg", tag_api_data["update_tag_name"])
    def test_02_update_tag_name(self, get_token, tag_id, tag_name, errcode, errmsg):
        """更新标签名称"""
        req = self.tag.update_tag_name(get_token, tag_id, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--获取标签列表")
    @allure.description("该用例是针对通讯录管理下的标签管理 获取标签列表接口的测试")
    @pytest.mark.parametrize("errcode, errmsg", tag_api_data["get_tag_list"])
    def test_03_get_tag_list(self, get_token, errcode, errmsg):
        """获取标签列表"""
        req = self.tag.get_tag_list(get_token)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--删除标签")
    @allure.description("该用例是针对根据获取的标签列表的标签id来删除标签")
    @pytest.mark.parametrize("errcode, errmsg", tag_api_data["delete_tag"])
    #@obtain_response(test_03_get_tag_list)
    def test_04_delete_tag(self, get_token, errcode, errmsg):
        """
        删除标签
        # TODO: 首先获取标签列表，然后根据标签id进行删除操作
        :param get_token:
        :param tag_id:
        :param errcode:
        :param errmsg:
        :return:
        """
        l = []
        tag_id_list = self.tag.get_tag_list(get_token)
        for i in tag_id_list.get("taglist"):
            l.append(i.get("tagid"))
        for tag_id in l:
            req = self.tag.delete_tag(get_token, tag_id)
            assert req.get("errcode") == errcode
            assert errmsg in req.get("errmsg")

