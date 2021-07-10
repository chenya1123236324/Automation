#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: exceptions.py
@time: 2021/7/11 0011 1:56
@desc:
'''
class BaseError(Exception):
    pass

class FileFormatError(BaseError):
    pass

class NotFoundError(BaseError):
    pass

class FileNotFound(FileNotFoundError, NotFoundError):
    pass

class FileFormatNotSupported(FileNotFoundError, NotFoundError):
    pass

class JSONDecodeError(NotFoundError):
    pass

class CSVNotFound(NotFoundError):
    pass

class FolderNotFound(NotFoundError):
    pass

# 解析字典错误
class ResolveDictError(NotFoundError):
    pass
