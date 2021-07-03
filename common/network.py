#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: network.py
@time: 2021/7/3 0003 22:22
@desc:
'''
import socket

class Network:
    @classmethod
    def get_local_ip(cls):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            host = s.getsockname()[0]
            return host
        except:
            print('通过UDP协议获取IP出错')
            hostname = socket.gethostname()
            host = socket.gethostbyname(hostname)
        return host