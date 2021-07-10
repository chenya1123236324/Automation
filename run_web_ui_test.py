#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: run_web_ui_test.py
@time: 2021/7/9 0009 16:05
@desc:
'''
import argparse
import sys

import pytest
import ujson
from common.java.bin.seleniumServerStart import selenium_server_start
from common.datetimeutil import DateTimeUtil
from common.httpclient.doRequest import DoRequest
from common.pytest import deal_pytest_ini_file
from init.web_ui.web_ui_init import web_ui_init
from common.base.read_web_ui_config import ReadWebUIConfig
from common.processfiletool import FileUtil
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.remote_connection import RemoteConnection

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', help='只执行匹配关键字的用例，会匹配文件名、类名、方法名', type=str)
    parser.add_argument('-d', '--dir', help='指定要测试的目录', type=str)
    parser.add_argument('-m', '--markexpr', help='只运行符合给定的mark表达式的测试', type=str)
    parser.add_argument('-s', '--capture', help='是否在标准输出流中输出日志,1:是、0:否,默认为0', type=str)
    parser.add_argument('-r', '--reruns', help='失败重跑次数,默认为0', type=str)
    parser.add_argument('-lf', '--lf', help='是否运行上一次失败的用例,1:是、0:否,默认为0', type=str)
    parser.add_argument('-clr', '--clr', help='是否清空已有测试结果,1:是、0:否,默认为0', type=str)
    args = parser.parse_args()

    # 启动selenium server服务
    print('[%s] 开始启动 selenium server ......' % DateTimeUtil.getNowTime())
    selenium_server_start()
    
    print('[%s] 开始初始化......' % DateTimeUtil.getNowTime())
    print('[%s] 开始检测 selenium server 是否可用......' % DateTimeUtil.getNowTime())

    try:
        doRquest=DoRequest(ReadWebUIConfig().web_ui_config.selenium_hub)
        httpResponseResult=doRquest.get('/status')
        result=ujson.loads(httpResponseResult.body)
        if result['status']==0:
            print('[%s] selenium server 状态为可用......' % DateTimeUtil.getNowTime())
        else:
            sys.exit('[%s] selenium server 状态为不可用' % DateTimeUtil.getNowTime())

    except:
        sys.exit('[%s] selenium server 状态为不可用' % DateTimeUtil.getNowTime())


    # 处理pytest文件
    deal_pytest_ini_file()

    print('[%s] 初始化基础数据......'% DateTimeUtil.getNowTime())
    web_ui_init()
    print('[%s] 初始化基础数据完成......'% DateTimeUtil.getNowTime())
    print('[%s] 初始化完成......'% DateTimeUtil.getNowTime())

    print('[%s] 开始测试......' % DateTimeUtil.getNowTime())
    exit_code = 0
    for current_browser in ReadWebUIConfig().web_ui_config.test_browsers:
        print('[%s] 开始【%s】浏览器测试......' % (DateTimeUtil.getNowTime(), current_browser))
        # 由于pytest的并发插件xdist采用子进程形式，当前主进程的单例在子进程中会重新创建，所以将每次要测试的浏览器信息写入到文件中，
        # 保证子进程能够正确读取当前要测试的浏览器
        FileUtil.replaceFileContent('conf/web_ui_config.conf', '\r\n', '\n')
        FileUtil.replaceFileContentWithLBRB('conf/web_ui_config.conf', '=' + current_browser, 'current_browser', '\n')
        # 执行pytest前的参数准备
        # pytest_execute_params = ['-c', 'conf/pytest.ini', '-v', '--alluredir',
        #                          'report/web_ui/' + current_browser + '/', '-n',
        #                          ReadWebUIConfig().web_ui_config.test_workers, '--dist', 'loadfile']
        pytest_execute_params = ['-c', 'conf/pytest.ini', '-v', '--alluredir',
                                  'report/web_ui/' + current_browser + '/',
                                  ]

        # 判断目录参数
        dir = 'testcase/web_ui/'
        if args.dir:
            dir = args.dir
        # 判断关键字参数
        if args.keyword:
            pytest_execute_params.append('-k')
            pytest_execute_params.append(args.keyword)
        # 判断markexpr参数
        if args.markexpr:
            pytest_execute_params.append('-m')
            pytest_execute_params.append(args.markexpr)
        # 判断是否输出日志
        if args.capture:
            if int(args.capture):
                pytest_execute_params.append('-s')
        # 判断是否失败重跑
        if args.reruns:
            if int(args.reruns):
                pytest_execute_params.append('--reruns')
                pytest_execute_params.append(args.reruns)
        # 判断是否只运行上一次失败的用例
        if args.lf:
            if int(args.lf):
                pytest_execute_params.append('--lf')
        # 判断是否清空已有测试结果
        if args.clr:
            if int(args.clr):
                pytest_execute_params.append('--clean-alluredir')
        pytest_execute_params.append(dir)
        tmp_exit_code = pytest.main(pytest_execute_params)
        if not tmp_exit_code == 0:
            exit_code = tmp_exit_code
        print('[%s] 结束【%s】浏览器测试......' % (DateTimeUtil.getNowTime(), current_browser))

    print('[%s] 清除未被关闭的浏览器......' % DateTimeUtil.getNowTime())
    try:
        conn = RemoteConnection(ReadWebUIConfig().web_ui_config.selenium_hub, True)
        sessions = conn.execute(Command.GET_ALL_SESSIONS, None)
        sessions = sessions['value']
        for session in sessions:
            session_id = session['id']
            conn.execute(Command.QUIT, {'sessionId': session_id})
    except Exception as e:
        print('[%s] 清除未关闭浏览器异常:\r\n %s' % (DateTimeUtil.getNowTime(), e.args.__str__()))
    print('[%s] 清除未被关闭的浏览器完成......' % DateTimeUtil.getNowTime())

    print('[%s] 结束测试......' % DateTimeUtil.getNowTime())
