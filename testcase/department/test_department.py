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
from testcase.department.conftest import department_api_data
from api.address_book.department_api import Department

@pytest.mark.usefixtures("get_token")
class TestDepartment:
    depart = Department()

    @pytest.mark.parametrize("parentid, name, errcode, errmsg", department_api_data["create_department"])
    def test_01_create_department(self, get_token, parentid, name, errcode, errmsg):
        # TODO 创建指定父部门的子部门，需要获取父部门id
        req = self.depart.create_department(get_token, parentid, name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("id, name, errcode, errmsg", department_api_data["update_department"])
    def test_02_update_department(self, get_token, id, name, errcode, errmsg):
        req = self.depart.update_department(get_token, id, name)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("id, errcode, errmsg", department_api_data["get_department_list"])
    def test_03_get_department_list(self, get_token, id, errcode, errmsg):
        req = self.depart.get_department_list(get_token, id)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")

    @pytest.mark.parametrize("id, errcode, errmsg", department_api_data["delete_department"])
    def test_04_delete_department(self, get_token, id, errcode, errmsg):
        # TODO 部门存在子部门 不能删除 errcode==60006
        # TODO 根据获取部门列表返回的父部门id删除，父部门id!=1需要查找子部门id
        req = self.depart.delete_department(get_token, id)
        assert req.get("errcode") == errcode
        assert errmsg in req.get("errmsg")
