# Automation
自动化框架改造
包含：接口自动化、app自动化

## apiautomation 接口自动化
基于python3 pytest+requests+allure的接口自动化框架改造

## web_ui Web UI自动化化
### 环境准备
#### 1、selenium server 运行环境部署
##### 1.1 安装jdk 1.8，并配置环境变量
```python
export JAVA_HOME=/usr/lib/jvm/jdk8
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```
##### 1.2 安装配置selenium
+   配置selenium server
    +   下载selenium-server-standalone-3.141.0.jar
    +   下载地址:http://selenium-release.storage.googleapis.com/index.html
    +   以管理员身份启动服务:java -jar selenium-server-standalone-3.141.0.jar -log selenium.log
+   下载浏览器驱动
    +   谷歌浏览器：http://chromedriver.storage.googleapis.com/index.html
    +   火狐浏览器：https://github.com/mozilla/geckodriver/
        +   驱动支持的最低浏览器版本：https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html
    +   将驱动所在目录加入到selenium server服务器系统环境变量:
        +   export PATH=/home/john/selenium/:$PATH
        +   或者直接放在python目录下即可


执行前创建目录 logs，report/,report/tempdata, report/html

## 项目结构

api 封装请求方法
+   apiautomation/client.py 封装访问api请求方法
+   apiautomation/tokens.py 获取登录企业微信的token
+   apiautomation/address_book/member_api.py 通讯录/成员管理
+   apiautomation/address_book/department_api.py 通讯录/部门管理
+   apiautomation/address_book/tag_api.py 通讯录/标签管理

conf 配置文件
+ config.ini 

+ pytest.conf 生成pytest.ini 文件的模板

+ `conf/web_ui_config.conf # web_ui入口的配置文件`

+ conf/wechatApi

  +   `conf/wechatApi/wechatApi.conf # wechatApi项目的配置文件`
  +   `conf/wechatApi/report.conf # 配置生成测试报告的端口`

+ conf/web_ui

  + `conf/web_ui/web_ui_pro.conf #web_ui项目的配置文件`

    

common 封装常用的工具包

+ common/selenium
  + `common/selenium/browserOperator.py # 封装浏览常用方法`
  + `driverUtil.py # driver对象`

+ common/pageObjects
  + `common/pageObjects/createElement.py # 封装创建元素对象入口`
  + common/pageObjects/web_ui
    + `common/pageObjects/web_ui/locator_type.py # 定位方式类型对象` 
    + `common/pageObjects/web_ui/wait_type.py # 等待方式类型对象`
    + `common/pageObjects/web_ui/mbaPro # mba网站项目`
      + `common/pageObjects/web_ui/mbaPro/elements # 元素`
      + `common/pageObjects/web_ui/mbaPro/pages # 封装页面对象`

+   common/baseob 存放自定义类对象
    +   `common/baseob/report_config.py 定义报告配置的类对象`
    +   `common/baseob/web_ui_config.py 定义web_ui入口的类对象`
    +   `common/baseob/elementInfo.py 定义元素信息的类对象`
    +   `common/baseob/api/wechatApi/wechatApiConf.py 定义wechatApi项目的类对象`
    +   `common/baseob/web_ui/proConfig.py 定义web_ui项目的类对象`
+   common/base 基础可调用函数
    +   `common/base/api/read_report_config.py 读取生成测试报告的基础配置`
    +   `common/base/read_web_ui_config.py 读取web_ui自动化的基础配置`
    +   `common/base/api/api_wechatApi_read_config.py 读取wechatApi项目的配置文件 `
    +   `common/base/web_ui/webUtil/web_ui_client.py 封装访问web请求基础函数`
    +   `common/base/web_ui/webUtil/web_ui_pro_read_config.py 读取web_ui项目的配置`
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
+   `init/web_ui/mbaPro/mbaProInit.py # web_ui mba网站项目初始化`
+   `init/web_ui/web_ui_init.py #web_ui 入口初始化`

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
+   report/web_ui


dataprovider 数据提供者
+   api/member/member.yaml 成员管理测试数据
+   api/department/department.yaml 部门管理测试数据
+   api/tag/tag.yaml 标签管理测试数据

testcase 测试用例

+ web_ui
  + `testcase/web_ui/mbaPro # mba网站项目 测试用例`

+ api
  + api/conftest.py 定义全局获取token
    `get_token 声明全局获取token`
    `pytest_collection_modifyitems钩子函数 解决测试用例参数化时用例名称有中文，输出控制台与html测试报告unicode编码问题`
  + api/member/test_member.py 成员管理测试用例
  + api/member/conftest.py 定义加载 member_api_data 文件
  + api/department/test_department.py 部门管理测试用例
  + api/department/conftest.py 定义加载 department_api_data 文件
  + api/tag/test_tag.py 标签管理测试用例
  + api/tag/conftest.py 定义加载 tag_api_data 文件

run_api_test.py 运行api测试用例文件

run_web_ui_test.py 运行web_ui测试用例文件

generate_api_test_report.py 生成测试报告并自动打开浏览器

ApiAutoTest

pytest.mark.parametrize 参数化的测试方法中，有一段代码只需要跑第一条用例的时候执行?
依赖注解

## pytest
### 执行指定的测试用例
`pytest testcase\api\member` 执行这个路径下的所有测试用例\
`pytest testcase\api\member\test_member.py` 执行这个文件下的所有测试用例\
`pytest --pyargs member` 执行member目录下的所有测试用例\
`pytest test_member.py::TestMember::test_01_create_member` 执行指定测试文件下的指定测试类的测试用例\
`pytest -k "tset_01" testcase\api\tag\test_tag.py` 通过指定关键字执行匹配的测试用例\
`pytest -k "not test_01" testcase\api\tag\test_tag.py` 通过指定关键字忽略匹配的test_01*测试用例\
`pytest -k "test_01 or test_04" test_member.py` 测试类或函数名包含test_01或test_04的测试用例将被执行\
`pytest -k "test_member and TestMember and not test_03" test_member.py` 执行test_member.py文件TestMember测试类，且test_03将会被取消选择（跳过）\
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

### 使用pytest-orderding 指定用例运行顺序
```python


@pytest.mark.run(order=1)
def test_03_demo():
    """
    order >>> 1~n
    order >>> first，second，third...second-to-last（倒数第二）, last（最后）
    或者
    after >>> 通过指定函数名指定，比如：被装饰的函数都要在after=test_demo后执行，这种用法就比较适合此类场景。
    """
    ...
```

### 使用pytest-xdist 多进程运行测试用例
```python

pytest -s -n auto testcase # 自动检测到系统的CPU核数；使用auto等于利用了所有CPU来跑用例，此时CPU占用率会特别高
pytest -s -n 2 testcase # 指定需要2个cpu来跑用例
# pytest -s -n auto --html=report.html --self-contained-html
# 按照一定顺序执行（默认是无序执行）
--dist=loadscope
将按照同一个模块module下的函数和同一个测试类class下的方法来分组，然后将每个测试组发给可以执行的worker，确保同一个组的测试用例在同一个进程中执行
目前无法自定义分组，按类class分组优先于按模块module分组
--dist=loadfile
按照同一个文件名来分组，然后将每个测试组发给可以执行的worker，确保同一个组的测试用例在同一个进程中执行


#如何让scope=session的fixture在test session中仅仅执行一次

pytest-xdist是让每个worker进程执行属于自己的测试用例集下的所有测试用例

这意味着在不同进程中，不同的测试用例可能会调用同一个scope范围级别较高（例如session）的fixture，该fixture则会被执行多次，这不符合scope=session的预期

# 解决方案
可以通过使用锁定文件进行进程间通信来实现
import pytest
from filelock import FileLock


@pytest.fixture(scope="session")
def login():
    """
    下面的示例只需要执行一次login（因为它是只需要执行一次来定义配置选项，等等）
    当第一次请求这个fixture时，则会利用FileLock仅产生一次fixture数据
    当其他进程再次请求这个fixture时，则会从文件中读取数据
    """
    print("====登录功能，返回账号，token===")
    with FileLock("session.lock"):
        name = "testyy"
        token = "npoi213bn4"
        # web ui自动化
        # 声明一个driver，再返回

        # 接口自动化
        # 发起一个登录请求，将token返回都可以这样写

    yield name, token
    print("====退出登录！！！====")
```


```
## 运行测试
1、API测试

+   cd Automation
+   python -u run_api_test.py --help
+   python -u run_api_test.py 运行testcase/api/目录所有的用例
+   python -u run_api_test.py -k keyword 运行匹配关键字的用例，会匹配文件名、类名、方法名
+   python -u run_api_test.py -d dir 运行指定目录的用例，默认运行cases/api/目录
+   python -u run_api_test.py -m mark 运行指定标记的用例

2、Web UI测试
+	cd Automation
+	python -u run_web_ui_test.py --help
+	python -u run_web_ui_test.py 运行testcase/web_ui/目录所有的用例

https://blog.csdn.net/yxxxiao/article/details/94591174

## 生成测试报告

1、API测试

+   cd Automation
+   pytest testcase/api --alluredir report\tempdata --clean-alluredir 运行测试用例
+   python3 -u generate_api_test_report.py -p 9080
+   在使用Ubuntu进行报告生成时，请勿使用sudo权限，否则无法生成，allure不支持

## pip 安装依赖
`https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype`

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
17. 自动打开浏览器查看测试报告(tag: v0.3.3)
18. 整合并管理项目(tag: v0.3.4)






```