# ApiAutomation
基于python3 pytest+requests+allure的接口自动化框架改造

## 项目结构
api 封装请求方法
+   client.py 封装访问api请求方法
+   tokens.py 获取登录企业微信的token
+   address_book/member_api.py 通讯录/成员管理
+   address_book/department_api.py 通讯录/部门管理
+   address_book/tag_api.py 通讯录/标签管理

conf 配置文件
+   config.ini \
test_url 测试环境的url

common 封装常用的工具包
+   \_\_init\_\_.py \
`BASE_PATH 获取项目根路径`
+   read_config.py 封装读取文件方法\
`load_ini 加载ini配置文件`
`load_yaml 加载yaml文件`
`load_file 项目加载指定文件`
+   logger.py 封装日志方法

logs 存放日志文件

dataprovider 数据提供者
+   member/member.yaml 成员管理测试数据

testcase 测试用例
+   conftest.py 定义全局获取token
+   member/test_member.py 成员管理测试用例
+   member/conftest.py 定义加载 member_api_data文件

ApiAutoTest

pytest.mark.parametrize 参数化的测试方法中，有一段代码只需要跑第一条用例的时候执行?
依赖注解