#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@author: yuejl
@application:
@contact: lewyuejian@163.com
@file: generate_web_ui_test_report.py
@time: 2021/7/10 0010 20:54
@desc:
'''
import platform
import subprocess
from multiprocessing import Pool

from common.base.read_report_config import ReadReportConfig
#from common.custom_multiprocessing import Custom_Pool
from common.network import Network
from common.strutil import StrUtil


def generate_windows_reports(report_dir,port):
    subprocess.check_output("start cmd.exe @cmd /c allure serve -p " + port + " " + report_dir, shell=True)

if __name__ == '__main__':
    report_config = ReadReportConfig().report_config
    ie_port = report_config.web_ui_ie_port
    chrome_port = report_config.web_ui_chrome_port
    firefox_port = report_config.web_ui_firefox_port
    if 'Windows' == platform.system():
        # 初始化进程池
        #p_pool = Custom_Pool(3)
        p_pool = Pool(3)
        if ie_port:
            # 获得当前监听ie端口的进程id
            get_ieport_process_id_command = 'netstat -ano|findstr "0.0.0.0:%s"' % ie_port
            try:
                get_allure_process_id = subprocess.check_output(get_ieport_process_id_command, shell=True)
                get_allure_process_id = get_allure_process_id.decode('utf-8')
                get_allure_process_id = StrUtil.getStringWithLBRB(get_allure_process_id, 'LISTENING', '\r\n').strip()
                kill_allure_process_command='taskkill /F /pid %s' % get_allure_process_id
                try:
                    subprocess.check_call(kill_allure_process_command,shell=True)
                except:
                    print('关闭 allure 进程,进程 id:' + get_allure_process_id + ',该进程监听已监听端口:' + ie_port)
            except:
                print('allure 未查找到监听端口 [%s] 的服务' % ie_port)
            print('生成 ie 报告,使用端口' + ie_port)
            print('ie 报告地址: http://%s:%s/' % (Network.get_local_ip(), ie_port))
            p = p_pool.apply_async(generate_windows_reports, ('report/web_ui/ie', ie_port))
        if chrome_port:
            # 获得当前监听chrome端口的进程id
            get_chrome_port_process_id_command = 'netstat -ano|findstr "0.0.0.0:%s"' % chrome_port
            try:
                get_allure_process_id = subprocess.check_output(get_chrome_port_process_id_command, shell=True)
                get_allure_process_id = get_allure_process_id.decode('utf-8')
                get_allure_process_id = StrUtil.getStringWithLBRB(get_allure_process_id, 'LISTENING', '\r\n').strip()
                kill_allure_process_command='taskkill /F /pid %s' % get_allure_process_id
                try:
                    subprocess.check_call(kill_allure_process_command,shell=True)
                except:
                    print('关闭 allure 进程,进程 id:' + get_allure_process_id + ',该进程监听已监听端口:' + chrome_port)
            except:
                print('allure 未查找到监听端口 [%s] 的服务' % chrome_port)
            print('生成 chrome 报告,使用端口' + chrome_port)
            print('chrome 报告地址: http://%s:%s/' % (Network.get_local_ip(), chrome_port))
            p = p_pool.apply_async(generate_windows_reports, ('report/web_ui/chrome', chrome_port))
        if firefox_port:
            # 获得当前监听ie端口的进程id
            get_firefox_port_process_id_command = 'netstat -ano|findstr "0.0.0.0:%s"' % firefox_port
            try:
                get_allure_process_id = subprocess.check_output(get_firefox_port_process_id_command, shell=True)
                get_allure_process_id = get_allure_process_id.decode('utf-8')
                get_allure_process_id = StrUtil.getStringWithLBRB(get_allure_process_id, 'LISTENING', '\r\n').strip()
                kill_allure_process_command='taskkill /F /pid %s' % get_allure_process_id
                try:
                    subprocess.check_call(kill_allure_process_command,shell=True)
                except:
                    print('关闭allure进程,进程id:' + get_allure_process_id + ',该进程监听已监听端口:' + firefox_port)
            except:
                print('allure未查找到监听端口 [%s] 的服务' % firefox_port)
            print('生成 firefox 报告,使用端口' + firefox_port)
            print('firefox 报告地址: http://%s:%s/' % (Network.get_local_ip(), firefox_port))
            p = p_pool.apply_async(generate_windows_reports, ('report/web_ui/firefox', firefox_port))
        p_pool.close()
        p_pool.join()
    else:
        # 获得当前allure所有进程id
        get_allure_process_ids_command = "ps -ef|grep -i allure\\.CommandLine|grep -v grep|awk '{print $2}'"
        allure_process_ids = subprocess.check_output(get_allure_process_ids_command, shell=True)
        allure_process_ids = allure_process_ids.decode('utf-8')
        allure_process_ids = allure_process_ids.split('\n')
        if ie_port:
            # 获得当前监听ie端口的进程id
            get_ieport_process_ids_command = "netstat -anp|grep -i " + ie_port + "|grep -v grep|awk '{print $7}'|awk -F '/' '{print $1}'"
            ie_port_process_ids = subprocess.check_output(get_ieport_process_ids_command, shell=True)
            ie_port_process_ids = ie_port_process_ids.decode('utf-8')
            ie_port_process_ids = ie_port_process_ids.split('\n')
            is_find = False
            for ie_port_process_id in ie_port_process_ids:
                if is_find:
                    break
                for allure_process_id in allure_process_ids:
                    allure_process_id = allure_process_id.strip()
                    ie_port_process_id = ie_port_process_id.strip()
                    if allure_process_id == ie_port_process_id and not is_find and allure_process_id and ie_port_process_id:
                        print('关闭 allure 进程,进程 id:' + allure_process_id.strip() + ',该进程监听已监听端口:' + ie_port)
                        subprocess.check_output("kill -9 " + allure_process_id.strip(), shell=True)
                        is_find = True
                        break
            print('生成 ie 报告,使用端口' + ie_port)
            print('ie 报告地址: http://%s:%s/' % (Network.get_local_ip(), ie_port))
            subprocess.check_output("nohup allure serve -p " + ie_port + " report/web_ui/ie > logs/ie_generate_web_ui_test_report.log 2>&1 &", shell=True)
        if chrome_port:
            # 获得当前监听chrome端口的进程id
            get_chromeport_process_ids_command = "netstat -anp|grep -i " + chrome_port + "|grep -v grep|awk '{print $7}'|awk -F '/' '{print $1}'"
            chrome_port_process_ids = subprocess.check_output(get_chromeport_process_ids_command, shell=True)
            chrome_port_process_ids = chrome_port_process_ids.decode('utf-8')
            chrome_port_process_ids = chrome_port_process_ids.split('\n')
            is_find = False
            for chrome_port_process_id in chrome_port_process_ids:
                if is_find:
                    break
                for allure_process_id in allure_process_ids:
                    allure_process_id = allure_process_id.strip()
                    chrome_port_process_id =  chrome_port_process_id.strip()
                    if allure_process_id == chrome_port_process_id and not is_find and allure_process_id and chrome_port_process_id:
                        print('关闭 allure 进程,进程 id:' + allure_process_id.strip() + ',该进程监听已监听端口:' + chrome_port)
                        subprocess.check_output("kill -9 " + allure_process_id.strip(), shell=True)
                        is_find = True
                        break
            print('生成 chrome 报告,使用端口' + chrome_port)
            print('chrome_port 报告地址: http://%s:%s/' % (Network.get_local_ip(), chrome_port))
            subprocess.check_output("nohup allure serve -p " + chrome_port + " report/web_ui/chrome > logs/chrome_generate_web_ui_test_report.log 2>&1 &", shell=True)
        if firefox_port:
            # 获得当前监听firefox端口的进程id
            get_firefox_port_process_ids_command = "netstat -anp|grep -i " + firefox_port + "|grep -v grep|awk '{print $7}'|awk -F '/' '{print $1}'"
            firefox_port_process_ids = subprocess.check_output(get_firefox_port_process_ids_command, shell=True)
            firefox_port_process_ids = firefox_port_process_ids.decode('utf-8')
            firefox_port_process_ids = firefox_port_process_ids.split('\n')
            is_find = False
            for firefox_port_process_id in firefox_port_process_ids:
                if is_find:
                    break
                for allure_process_id in allure_process_ids:
                    allure_process_id = allure_process_id.strip()
                    firefox_port_process_id =  firefox_port_process_id.strip()
                    if allure_process_id == firefox_port_process_id and not is_find and allure_process_id and firefox_port_process_id:
                        print('关闭 allure 进程,进程 id:' + allure_process_id.strip() +',该进程监听已监听端口:' + firefox_port)
                        subprocess.check_output("kill -9 " + allure_process_id, shell=True)
                        is_find = True
                        break
            print('生成 firefox 报告,使用端口' + firefox_port)
            print('firefox_port 报告地址:http://%s:%s/' % (Network.get_local_ip(), firefox_port))
            subprocess.check_output("nohup allure serve -p " + firefox_port + " report/web_ui/firefox > logs/firefox_generate_web_ui_test_report.log 2>&1 &", shell=True)
