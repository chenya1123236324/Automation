#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: client.py
@time: 2021/6/24 0024 17:02
@desc:
'''
import json as js
import requests
from common.read_config import load_ini
from common.logger import logger

class ApiRequest:
    def __init__(self):
        self.variables = {}
        self.url = load_ini('host')['test_url']
        self.session = requests.session()

    def get(self, url, method='GET', **kwargs):
        return self.request(url, method, **kwargs).json()

    def post(self, url ,method='POST', data=None, json=None, **kwargs):
        return self.request(url, method, data, json, **kwargs).json()

    def put(self, url, method='PUT', data=None, **kwargs):
        return self.request(url, method, data, **kwargs)

    def delete(self, url, method='DELETE', data=None, **kwargs):
        return self.request(url, method, data, **kwargs)

    def patch(self, url, method='PATCH', data=None, **kwargs):
        return self.request(url, method, data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        """
        封装访问请求
        :param url:
        :param method:
        :param data:
        :param json:
        :param kwargs:
        :return:
        """
        url = self.url + url

        if "herders" in kwargs:
            self.variables["herders"] = kwargs.get("herders")
        if "params" in kwargs:
            self.variables["params"] = kwargs.get("params")
        if "files" in kwargs:
            self.variables["files"] = kwargs.get("files")
        if "cookies" in kwargs:
            self.variables["cookies"] = kwargs.get("cookies")
        self.request_log(url, method, data, json,
                         params=self.variables.get('params'),
                         headers=self.variables.get('herders'),
                         files=self.variables.get('files'),
                         cookies=self.variables.get('cookies'))
        if method in ['GET', 'get']:
            return self.session.get(url, **kwargs)
        if method in ['POST', 'post']:
            return self.session.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = js.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = js.dumps(json)
            return self.session.patch(url, data, **kwargs)


    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(js.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(js.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(js.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(js.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(js.dumps(cookies, indent=4, ensure_ascii=False)))
