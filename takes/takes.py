#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: takes.py
@time: 2021/6/27 0027 12:28
@desc:
'''
from functools import wraps

def resolve_dict(name, key):
    """

    Args:
        Decorate the function that returns the dictionary.
    Examples:
        pattern.yaml
        =============================================
        pattern:
            zh_CN: r'[\u4e00-\u9fa5]+'

        =============================================

        >>> name = 'pattern'
        >>> key='zh_CN'

        @resolve_dict(name='pattern', key='zh_CN')
        def load_yaml(file='../config/pattern.yaml'):
            with open(file, 'r', encoding='utf-8') as f:
                yml_content = yaml.load(f, Loader=yaml.CLoader)

                return yml_content

    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            res = func(*args, **kwargs)
            if isinstance(res, dict):
                #logger.info(f'Obtain {func.__name__}')
                return res[name][key]
            else:
                return {}

        return wrapper

    return decorator

# 定义一个计算执行时间的函数作装饰器，传入参数为装饰的函数或方法
def execute_time(func):
    from time import time

    # 定义嵌套函数，用来打印出装饰的函数的执行时间
    def wrapper(*args, **kwargs):
        # 定义开始时间和结束时间，将func夹在中间执行，取得其返回值
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        # 打印方法名称和其执行时间
        #logger.info(f'{func.__name__}() execute time: {end - start}s')
        # 返回func的返回值
        return func_return

    # 返回嵌套的函数
    return wrapper

