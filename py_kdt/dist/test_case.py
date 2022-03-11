
import allure
# a = [{'项目名称':'XXXX公司的管理系统','测试模块':'登录模块','用例名称':'admin管理员登录','关键字':
#     [{'第一步:打开浏览器':'Browser.Max_Browser'},{'第二步:输入用户名':'Browser.input','页面元素':['css',''],'输入值':'admin'}]}]
import pytest
from woniusales_project.pytest_kdt_ui.common.read_yaml_data import Yaml_read_or_writer
f = Yaml_read_or_writer().read_yaml()
import sys
from woniusales_project.pytest_kdt_ui.common.Class_reflection import Class_Reflections
@allure.epic('XXX公司管理系统')
@pytest.mark.parametrize('data',f)
class Test_baidu():
    def setup_class(self):
        __import__(r'woniusales_project.pytest_kdt_ui.conftest')
        module = sys.modules[r'woniusales_project.pytest_kdt_ui.conftest']
        cls = getattr(module,'Browser')
        instance = cls()
        method = getattr(instance, 'Max_Browser')
        method_time = getattr(instance,'implicitly_wait')
        method()
        method_time()
    def test(self,data):
        __import__(r'woniusales_project.pytest_kdt_ui.conftest')
        module = sys.modules[r'woniusales_project.pytest_kdt_ui.conftest']
        allure.dynamic.feature('模块名称')
        allure.dynamic.story('模块功能点')
        allure.dynamic.title('登录功能有效等价类')
        for i in data['测试步骤']:
            cls_name = i[list(i.keys())[0]].split('.')[1] # 类名
            functon = Class_Reflections(module=module, j=i) # 返回一个类反射类,里面有点击,输入方法,获取网页等等
            if cls_name == 'input': # 输入
                functon.input_Class_Reflection()
            elif cls_name == 'get_url': # 获取网址
                functon.get_url_Class_Reflection()
            elif cls_name == 'click': # 点击
                functon.click_Class_Reflection()
            elif cls_name == 'get_png': # 截图
                functon.Get_PNG_Class_Reflection()
            elif cls_name == 'random_select_opt':
                functon.random_select() # 下拉框操作

if __name__ == '__main__':
    print(f)