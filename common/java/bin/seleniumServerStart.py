#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: seleniumServerStart.py
@time: 2021/7/10 0010 23:42
@desc:
'''
import multiprocessing
import os
import platform
import subprocess
from common import BASE_PATH
from common.base.read_web_ui_config import ReadWebUIConfig
from common.network import Network
from common.strutil import StrUtil
from threading import Thread

selenium_server_path = BASE_PATH + os.sep + 'common' + os.sep + 'java' + os.sep + 'lib'

def run_async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def selenium_server_command():
    subprocess.check_output("start cmd.exe @cmd /c java -jar selenium-server-standalone-3.141.0.jar -log selenium.log", cwd=selenium_server_path, shell=True)

@run_async
def selenium_server_start():
    selenium_server_config = ReadWebUIConfig().web_ui_config
    port = selenium_server_config.selenium_hub_port

    if 'Windows' == platform.system():
        get_selenium_server_process_id_command = 'netstat -ano|findstr "0.0.0.0:%s"' % port
        try:
            get_selenium_server_process_id = subprocess.check_output(get_selenium_server_process_id_command, shell=True)
            get_selenium_server_process_id = get_selenium_server_process_id.decode('utf-8')
            get_selenium_server_process_id = StrUtil.getStringWithLBRB(get_selenium_server_process_id, 'LISTENING',
                                                                       '\r\n').strip()
            kill_selenium_server_process_command = 'taskkill /F /pid %s' % get_selenium_server_process_id
            try:
                subprocess.check_call(kill_selenium_server_process_command, shell=True)
            except:
                print('关闭 Selenium Server 进程,进程 id:' + get_selenium_server_process_id + ',该进程监听已监听端口: ' + port)
        except:
            print(' Selenium Server 未查找到监听端口 [%s] 的服务' % port)
        print('WebDriver Hub 地址: http://%s:%s/wd/hub' % (Network.get_local_ip(), port))
        process = multiprocessing.Process(target=selenium_server_command)
        process.start()
        process.join()

    else:
        # 获得当前allure所有进程id
        get_selenium_server_process_ids_command = "ps -ef|grep -i allure\\.CommandLine|grep -v grep|awk '{print $2}'"
        selenium_server_process_ids = subprocess.check_output(get_selenium_server_process_ids_command, shell=True)
        selenium_server_process_ids = selenium_server_process_ids.decode('utf-8')
        selenium_server_process_ids = selenium_server_process_ids.split('\n')

        # 获得当前监听port端口的进程id
        get_port_process_ids_command = "netstat -anp|grep -i " + port + "|grep -v grep|awk '{print $7}'|awk -F '/' '{print $1}'"
        port_process_ids = subprocess.check_output(get_port_process_ids_command, shell=True)
        port_process_ids = port_process_ids.decode('utf-8')
        port_process_ids = port_process_ids.split('\n')
        is_find = False
        for port_process_id in port_process_ids:
            if is_find:
                break
            for selenium_server_process_id in selenium_server_process_ids:
                selenium_server_process_id = selenium_server_process_id.strip()
                port_process_id = port_process_id.strip()
                if selenium_server_process_id == port_process_id and not is_find and selenium_server_process_id and port_process_id:
                    print('关闭 Selenium Server 进程,进程 id:' + selenium_server_process_id.strip() + ',该进程监听已监听端口: ' + port)

                    subprocess.check_output("kill -9 " + selenium_server_process_id.strip(), shell=True)
                    is_find = True
                    break

        print('WebDriver Hub 地址: http://%s:%s/wd/hub' % (Network.get_local_ip(), port))
        subprocess.check_output(
            "nohup java -jar selenium-server-standalone-3.141.0.jar > selenium.log 2>&1 &", shell=True,
            cwd=selenium_server_path)


