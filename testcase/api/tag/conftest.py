#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: conftest.py
@time: 2021/6/26 0026 14:56
@desc:
'''

from common.read_config import load_file

tag_api_data = load_file("tag.yaml")

def obtain_response(before_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(args[0])
            print(args[1])

            # before_result = before_func(*args, **kwargs)
            # if isinstance(before_result, dict):
            #     for i in before_result.get("taglist"):
            #
            #         res = func(i.get("tagid"))
            #         return res
        return wrapper
    return decorator