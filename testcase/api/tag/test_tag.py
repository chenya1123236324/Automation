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
from testcase.api.tag.conftest import tag_api_data
from api.apiautomation.tag_api import Tag


@allure.epic("通讯录接口测试")
@allure.feature("标签管理")
@pytest.mark.usefixtures("get_token")
class TestTag:
    tag = Tag()

    @pytest.mark.run(order=1)
    @allure.story("用例--创建标签")
    @allure.description("该用例是针对通讯录管理下的标签管理 创建标签接口的测试")
    @allure.title("测试数据：【 {tag_name}, {errcode}, {errmsg} 】")
    @pytest.mark.parametrize("tag_name, errcode, errmsg", tag_api_data["create_tag"])
    def test_01_create_tag(self, get_token, tag_name, errcode, errmsg):
        """创建标签"""
        req = self.tag.create_tag(get_token, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.run(order=2)
    @allure.story("用例--更新标签名称")
    @allure.description("该用例是针对通讯录管理下的标签管理 更新标签名称接口的测试")
    @allure.title("测试数据：【 {tag_id}, {tag_name}, {errcode}, {errmsg} 】")
    @pytest.mark.parametrize("tag_id, tag_name, errcode, errmsg", tag_api_data["update_tag_name"])
    def test_02_update_tag_name(self, get_token, tag_id, tag_name, errcode, errmsg):
        """更新标签名称"""
        req = self.tag.update_tag_name(get_token, tag_id, tag_name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.run(order=3)
    @allure.story("用例--获取标签列表")
    @allure.description("该用例是针对通讯录管理下的标签管理 获取标签列表接口的测试")
    @allure.title("测试数据：【 {errcode}, {errmsg} 】")
    @pytest.mark.parametrize("errcode, errmsg", tag_api_data["get_tag_list"])
    def test_03_get_tag_list(self, get_token, errcode, errmsg):
        """获取标签列表"""
        req = self.tag.get_tag_list(get_token)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.run(order=4)
    @allure.story("用例--删除标签")
    @allure.description("该用例是针对根据获取的标签列表的标签id来删除标签")
    @allure.title("测试数据：【 {errcode}, {errmsg} 】")
    @pytest.mark.parametrize("errcode, errmsg", tag_api_data["delete_tag"])
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
        with allure.step('获取所有的标签列表'):
            tag_id_list = self.tag.get_tag_list(get_token)
        with allure.step('提取标签id'):
            for i in tag_id_list.get("taglist"):
                l.append(i.get("tagid"))

        for tag_id in l:
            with allure.step(f'根据标签id: {tag_id} 进行删除'):

                req = self.tag.delete_tag(get_token, tag_id)
            with allure.step('断言'):

                assert req.get("errcode") == errcode
                assert errmsg in req.get("errmsg")

