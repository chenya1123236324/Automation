# ApiAutomation
基于python3 pytest+requests+allure的接口自动化框架改造

执行前创建目录 logs，report/,report/tempdata, report/html

## 项目结构
api 封装请求方法
+   client.py 封装访问api请求方法
+   tokens.py 获取登录企业微信的token
+   address_book/member_api.py 通讯录/成员管理
+   address_book/department_api.py 通讯录/部门管理
+   address_book/tag_api.py 通讯录/标签管理

conf 配置文件
+   config.ini \
+   pytest.conf 生成pytest.ini 文件的模板
+   conf/wechatApi/wechatApi.conf # wechatApi项目的配置文件
+   conf/wechatApi/report.conf # 配置生成测试报告的端口

common 封装常用的工具包
+   common/baseob 存放自定义类对象
+   `common/baseob/api/wechatApi/wechatApiConf.py 定义wechatApi项目的类对象`
+   `common/baseob/report_config.py 定义报告配置的类对象`
+   common/base 基础可调用函数
+   `common/base/api/api_wechatApi_read_config.py 读取wechatApi项目的配置文件 `
+   `common/base/api/read_report_config.py 读取生成测试报告的配置文件`
+   \_\_init\_\_.py \
`BASE_PATH 获取项目根路径`
+   read_config.py 封装读取文件方法\
`load_ini 加载ini配置文件`
`load_yaml 加载yaml文件`
`load_file 项目加载指定文件`
+   logger.py 封装日志方法
+   processfiletool.py 处理文档内容工具函数
+   datetimeutil.py 处理时间工具
+   network.py 获取本地IP
+   strutil.py 处理字符串的模块

init 初始化工具
+   init/api_init.py 初始化必要数据
+   `init/api/wechatApi/wechatInit.py 初始化函数，比如：清除上一次构造的数据`

```python
baseob 自定义类对象 或者 *.conf
base 基础可调用函数（调用自定义类对象以及配置文件）
初始化函数
初始化函数入口 api_init.py
测试用例执行文件 run_api_test.py

初始化函数的使用:
run_api_test.py >> api_init.py >> init/api/wechatApi/wechatInit.py >> 
common/base/api/api_wechatApi_read_config.py >> common/baseob/api/wechatApi/wechatApiConf.py
common/base/api/api_wechatApi_read_config.py >> conf/wechatApi/wechatApi.conf
```

logs 存放日志文件

report 存放测试报告
+   report/tempdata
`pytest testcase --alluredir report\tempdata --clean-alluredir`
+   report/html
`allure generate --clean report\tempdata -o report\html`


dataprovider 数据提供者
+   member/member.yaml 成员管理测试数据
+   department/department.yaml 部门管理测试数据
+   tag/tag.yaml 标签管理测试数据

testcase 测试用例
+   conftest.py 定义全局获取token
`get_token 声明全局获取token`
`pytest_collection_modifyitems钩子函数 解决测试用例参数化时用例名称有中文，输出控制台与html测试报告unicode编码问题`
+   member/test_member.py 成员管理测试用例
+   member/conftest.py 定义加载 member_api_data 文件
+   department/test_department.py 部门管理测试用例
+   department/conftest.py 定义加载 department_api_data 文件
+   tag/test_tag.py 标签管理测试用例
+   tag/conftest.py 定义加载 tag_api_data 文件

run_api_test.py 运行api测试用例文件
generate_api_test_report.py 生成测试报告并自动打开浏览器

ApiAutoTest

pytest.mark.parametrize 参数化的测试方法中，有一段代码只需要跑第一条用例的时候执行?
依赖注解

## pytest
### 执行指定的测试用例
`pytest testcase\member` 执行这个路径下的所有测试用例
`pytest testcase\member\test_member.py` 执行这个文件下的所有测试用例
`pytest --pyargs member` 执行member目录下的所有测试用例
`pytest test_member.py::TestMember::test_01_create_member` 执行指定测试文件下的指定测试类的测试用例
`pytest -k "tset_01" testcase\tag\test_tag.py` 通过指定关键字执行匹配的测试用例
`pytest -k "not test_01" testcase\tag\test_tag.py` 通过指定关键字忽略匹配的test_01*测试用例
`pytest -k "test_01 or test_04" test_member.py` 测试类或函数名包含test_01或test_04的测试用例将被执行
`pytest -k "test_member and TestMember and not test_03" test_member.py` 执行test_member.py文件TestMember测试类，且test_03将会被取消选择（跳过）
`pytest -v -m webtest` 执行标记的webtest的测试用例

```python
# 在类或者方法上，增加标记，如@pytest.marker.webtest
import pytest
@pytest.mark.webtest
def test_01_demo():
    ...

# 运行指定标记的用例
# 在pytest.ini配置文件的
[pytest]
markers = 
    smoke: #添加标签，可以自定义
@pytest.mark.smoke
def test_02_demo():
    ...

```
## 运行测试
1、API测试

cd AutomationTest\
python3 -u run_api_test.py --help\
python3 -u run_api_test.py 运行cases/api/目录所有的用例\
python3 -u run_api_test.py -k keyword 运行匹配关键字的用例，会匹配文件名、类名、方法名\
python3 -u run_api_test.py -d dir 运行指定目录的用例，默认运行cases/api/目录\
python3 -u run_api_test.py -m mark 运行指定标记的用例

https://blog.csdn.net/yxxxiao/article/details/94591174

## 生成测试报告

1、API测试

+   cd ApiAutomation\
+   pytest testcase --alluredir report\tempdata --clean-alluredir 运行测试用例
+   python3 -u generate_api_test_report.py -p 9080\
+   在使用Ubuntu进行报告生成时，请勿使用sudo权限，否则无法生成，allure不支持



## 提交记录
1. 生成requirements.txt依赖文件
2. 封装访问请求方法client
3. 配置文件 添加config.ini配置文件
4. 声明BASE_PATH 项目路径 read_config 封装读取文件方法 logger 封装日志方法
5. 数据提供者
6. 获取登录企业微信的token
7. 通讯录管理 成员管理
   通讯录管理 封装成员管理的api
8. 通讯录管理 封装部门管理的api
9. 通讯录管理 封装标签管理的api
10. 引入数据提供者驱动、conftest.py声明全局token
11. 封装通讯录管理 部门管理测试用例
    pytest_collection_modifyitems钩子 解决测试用例参数化时用例名称有中文，输出控制台与html测试报告unicode编码问题(tag: v0.2.7)
12. 封装通讯录管理 标签管理测试用例(tag: v0.2.8)
13. 引入allure生成测试报告(tag: v0.2.9)
14. 测试报告添加内容：测试数据作为测试报告的标题，添加bug链接，添加测试用例链接，测试步骤( tag: v0.3.1)
添加处理文档内容工具函数
添加时间处理函数
15. 添加项目初始化工具(tag: v0.3.2)
16. 添加命令行运行测试
17. 自动打开浏览器查看测试报告





