#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: test_department.py
@time: 2021/6/26 0026 9:11
@desc:
'''
import pytest
import allure
from testcase.department.conftest import department_api_data
from api.address_book.department_api import Department

@allure.epic("通讯录接口测试")
@allure.feature("部门管理")
@pytest.mark.usefixtures("get_token")
class TestDepartment:
    depart = Department()

    @allure.story("用例--创建部门")
    @allure.description("该用例是针对通讯录管理下的部门管理 创建部门接口的测试")
    @pytest.mark.parametrize("parentid, name, errcode, errmsg", department_api_data["create_department"])
    def test_01_create_department(self, get_token, parentid, name, errcode, errmsg):
        # TODO 创建指定父部门的子部门，需要获取父部门id
        req = self.depart.create_department(get_token, parentid, name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--更新部门")
    @allure.description("该用例是针对通讯录管理下的部门管理 更新部门接口的测试")
    @pytest.mark.parametrize("id, name, errcode, errmsg", department_api_data["update_department"])
    def test_02_update_department(self, get_token, id, name, errcode, errmsg):
        req = self.depart.update_department(get_token, id, name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--获取部门列表")
    @allure.description("该用例是针对通讯录管理下的部门管理 获取部门列表接口的测试")
    @pytest.mark.parametrize("id, errcode, errmsg", department_api_data["get_department_list"])
    def test_03_get_department_list(self, get_token, id, errcode, errmsg):
        req = self.depart.get_department_list(get_token, id)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @allure.story("用例--删除部门")
    @allure.description("该用例是针对通讯录管理下的部门管理 删除部门接口的测试")
    @pytest.mark.parametrize("id, errcode, errmsg", department_api_data["delete_department"])
    def test_04_delete_department(self, get_token, id, errcode, errmsg):
        # TODO 部门存在子部门 不能删除 errcode==60006
        # TODO 根据获取部门列表返回的父部门id删除，父部门id!=1需要查找子部门id
        req = self.depart.delete_department(get_token, id)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")
