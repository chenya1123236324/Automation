#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: processfiletool.py
@time: 2021/6/30 0030 16:04
@desc:
'''
import os
import re
import time
from typing import Text, List
import ujson as ujson
from common.exceptions import FolderNotFound


def get_base_dir():
    """获取根目录"""
    base_path_temp = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    root_dir = base_path_temp.replace(r'\/'.replace(os.sep, ''), os.sep)
    return root_dir

def clear_file(dir_path):
    """
    清除目录以及子目录下的文件
    :param dir_path: 路径
    :return: None
    """
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        # 获取目录下文件和文件夹列表
        ls = os.listdir(dir_path)
        # 删除目录下的所有文件及子目录下的所有文件
        for i in ls:
            c_path = os.path.join(dir_path, i)  # 将目录和文件名拼接
            if os.path.isdir(c_path):  # 如果是目录继续调用清除函数
                clear_file(c_path)
            else:
                os.remove(c_path)

    else:
        raise NameError('路径不存在或者不是一个目录')

def clear_log(dir_path):
    """
    清空一天前生成的log
    :param dir_path: 目录路径
    :return: None
    """
    now_time = time.time()  # 获取现在时间戳
    if os.path.exists(dir_path) and os.path.isdir(dir_path):  # 判断路径是目录并且路径下有文件或者目录
        ls = os.listdir(dir_path)
        for i in ls:
            c_path = os.path.join(dir_path, i)  # 将目录和文件名拼接
            if os.path.isdir(c_path):
                clear_log(c_path)
            else:
                cre_time = os.path.getmtime(c_path)  # 获取文件创建时间戳
                if cre_time < (now_time - 86400):  # 删除符合条件文件
                    os.remove(c_path)
    else:
        raise NameError('路径不存在或者不是一个目录')


class FileUtil:

    @staticmethod
    def load_folder_files(folderPath: Text, recursive: bool = True) -> List:
        '''

        :param folderPath:
        :param recursive: 是否递归(是否加载下级目录文件)
        :return: file_list >>> 文件路径 ; fileList>>> 文件名
        '''
        if not os.path.isdir(folderPath):
            raise FolderNotFound(u"Folder does not exist \"{}\"".format(folderPath))

        if isinstance(folderPath, (list, set)):
            files = []
            for path in set(folderPath):
                files.extend(FileUtil.load_folder_files(path, recursive))
            return files
        if not os.path.exists(folderPath):
            raise FolderNotFound(u"Folder does not exist \"{}\"".format(folderPath))
        file_list = []
        # fileList = []
        for dirPath, dirNames, fileNames in os.walk(folderPath):
            fileNames_list = []
            for fileName in fileNames:
                # 过滤掉yaml文件和json文件
                if not fileName.endswith(('.yml', '.yaml', '.json', '.txt', '.xlsx')):
                    continue
                fileNames_list.append(fileName)
                # fileList.append(fileName)
            for fileName in fileNames_list:
                filePath = os.path.join(dirPath, fileName)
                file_list.append(filePath)
            if not recursive:
                break
        return file_list

    @staticmethod
    def load_sub_folder(folderPath: Text) -> List:
        files_list = []
        folder_files = os.listdir(folderPath)
        for i in range(0, len(folder_files)):
            path = os.path.join(folderPath, folder_files[i])
            if os.path.isdir(path):
                files_list.extend(FileUtil.load_sub_folder(path))
            if os.path.isfile(path):
                files_list.append(path)
        return files_list

    @staticmethod
    def load_file_name(filePath: Text, recursive: bool = False) -> List:
        '''
            获取目录 或者 文件的文件名
        :param filePath: 目录路径 或者 文件路径
        :param recursive: 是否递归下级目录 True > 递归
        :return:
        '''
        # 路径 文件  文件夹
        result = []
        if os.path.isdir(filePath):
            files = FileUtil.load_folder_files(filePath, recursive=recursive)
            for file in files:
                data = os.path.splitext(file)[0]
                if '\\' in data:
                    temp = data.rsplit('\\', 1)[1]
                else:
                    temp = data.rsplit('/', 1)[1]
                result.append(temp)
        if os.path.isfile(filePath):
            # 文件带路径
            if '\\' in filePath:
                data = filePath.rsplit('\\', 1)[1]
                temp = data.rsplit('.', 1)[0]
                result.append(temp)
            elif '/' in filePath:
                data = filePath.rsplit('/', 1)[1]
                print(data)
                temp = data.rsplit('.', 1)[0]
                print(temp)
                result.append(temp)

        return result

    @classmethod
    def replaceFileLineContent(cls, filePath, match_keyword, old, new, encoding='utf-8'):
        """
                根据关键字匹配文档中的行，对行内容进行替换
                :param filePath: 文档路径
                :param match_keyword: 用于匹配文档中包含的关键字行
                :param old: 匹配的行中包含的字符串
                :param new: 用于替换匹配的行中的旧字符串
                :return:
                """
        with open(filePath, 'r', encoding=encoding) as f:
            new_lines = []
            lines = f.readlines()
            for line in lines:
                if match_keyword in line:
                    line = line.replace(old, new)
                new_lines.append(line)
            f.close()

            with open(filePath, 'w+', encoding=encoding) as f:
                f.writelines(new_lines)
                f.close()

    @classmethod
    def replaceFileContent(cls, filePath, old, new, replaceNum=-1, replaceOffset=0, encoding='utf-8'):
        """
        替换文档中的内容,支持替换全部、替换指定前几个、替换第N个
        :param filePath: 文档路径
        :param old: 要替换的字符串
        :param new: 要替换的新字符串
        :param replaceNum: 从头开始替换。-1代表替换所有；-2代表该参数无效，replaceOffset参数生效
        :param replaceOffset: 替换第几个，下标从0开始，
        :return:
        """
        with open(filePath, 'r', encoding=encoding) as f:
            content = f.read()
            if int(replaceNum) == -1:
                content = content.replace(old, new)
            elif not int(replaceNum) == -2:
                # 参数为整数
                replaceNum = abs(replaceNum)
                content = re.sub(old, new, content, replaceNum)
            else:
                # 参数为-2
                index = 0
                # 存储查找到的次数
                times = 0
                while True:
                    # 第一次查找匹配所在的位置
                    if index == 0:
                        index = content.find(old)
                        if index == -1:
                            break
                        else:
                            times = times + 1
                    else:
                        # 从上一次匹配的位置开始查找下一次匹配的位置
                        index = content.find(old, index + 1)
                        if index == -1:
                            break
                        else:
                            times = times + 1

                    if times == int(replaceOffset) + 1:
                        preContent = content[:index]
                        centerContent = new
                        suffContent = content[index + len(old):]
                        content = preContent + centerContent + suffContent
                        break

            with open(filePath, 'w+', encoding=encoding) as f:
                f.writelines(content)
                f.close()

    @classmethod
    def replaceFileContentWithLBRB(cls, filePath, new, lbStr, rbStr, replaceOffset=0, encoding='utf-8'):
        """
        根据左右字符串匹配要替换的文档内容，支持多处匹配只替换一处的功能
        :param filePath: 文档路径
        :param new: 要替换的新字符串
        :param lbStr: 要替换内容的左侧字符串
        :param rbStr: 要替换内容的右侧字符串
        :param replaceOffset: 需要将第几个匹配的内容进行替换，下标从0开始，所有都替换使用-1
        :return:
        """
        if lbStr == '' and rbStr == '':
            return
        regex = '([\\s\\S]*?)'
        r = re.compile(lbStr + regex + rbStr)
        with open(filePath, 'r', encoding=encoding) as f:
            content = f.read()
            match_results = r.findall(content)
            if int(replaceOffset) == -1:
                for result in match_results:
                    # 为了防止匹配的内容在其他地方也有被替换掉，故需要将匹配的前后字符串加上
                    content = content.replace(lbStr + result + rbStr, lbStr + new + rbStr)
            elif len(match_results) >= replaceOffset and len(match_results) != 0:
                # 用于记录匹配到关键字的位置
                index = None
                for i in range(len(match_results)):
                    if i == 0:
                        # 第一次查找匹配所在的位置
                        index = content.find(lbStr + match_results[i] + rbStr)
                    else:
                        # 从上一次匹配的位置开始查找下一次匹配的位置
                        index = content.find(lbStr + match_results[i] + rbStr, index + 1)
                    if i == int(replaceOffset):
                        preContent = content[:index]
                        centerContent = lbStr + new + rbStr
                        suffContent = content[index + len(lbStr + match_results[i] + rbStr):]
                        content = preContent + centerContent + suffContent
                        break
            f.close()

            with open(filePath, 'w+', encoding=encoding) as f:
                f.writelines(content)
                f.close()

    @classmethod
    def readJsonFromFile(cls, filePath, encoding='utf-8'):
        """
        从文件里读取json字符串
        :param filePath:
        :return:
        """
        with open(filePath, 'r', encoding=encoding) as f:
            result = f.read()
            f.close()
        result = ujson.loads(result)
        return result