import random
import time

import allure
import pytest
from woniusales_project.pytest_kdt_ui.common.read_config import read_configini
from woniusales_project.pytest_kdt_ui.Lib.selenium.webdriver.firefox.service import Service as FireFoxService
from woniusales_project.pytest_kdt_ui.Lib.selenium import webdriver
from woniusales_project.pytest_kdt_ui.Lib.selenium.webdriver.chrome.service import Service as ChromeService
from woniusales_project.pytest_kdt_ui.Lib.selenium.webdriver.support.select import Select
'''单例运行浏览器'''
Browser_name = '火狐'
from woniusales_project.pytest_kdt_ui.config import Browser_Memory_address,Logged_in
class Browser():
    __instance = None # 实例的空间
    dr  = None # 浏览器的driver对象
    def __new__(cls,*args,**kwargs) ->Browser_Memory_address:
        '''返回一个内存地址,里面实例一个浏览器对象'''
        if cls.__instance is None:
            if Browser_name == '火狐' or Browser_name == 'firefox':
                cls.dr = webdriver.Firefox(service=FireFoxService("driver/geckodriver.exe")) # 火狐浏览器内核
            elif Browser_name == 'chrome' or  Browser_name == '谷歌':
                cls.dr = webdriver.Chrome(service=ChromeService("driver/chromedriver.exe")) # 谷歌浏览器内核
            else:
                raise TypeError(f"你选择的浏览器{Browser_name}不支持!!")
            cls.__instance = object.__new__(cls) # 实例化
        return cls.__instance
    def Max_Browser(self):
        '''最大化浏览器'''
        Browser.dr.maximize_window()
    def Close_Browser(self):
        '''退出浏览器'''
        if Browser.dr is not None:
            Browser.dr.quit()
        Browser.dr = None
        Browser.__instance = None
    def input(self,element,value):
        '''输入操作'''
        Browser.dr.find_element(*element).clear()
        Browser.dr.find_element(*element).send_keys(value)

    def click(self,element):
        '''点击操作'''
        Browser.dr.find_element(*element).click()

    def get_url(self,url):
        '''打开网址'''
        Browser.dr.get(url)

    def implicitly_wait(self,time=10):
        '''隐式等待'''
        Browser.dr.implicitly_wait(time)

    def get_png(self):
        '''浏览器截图'''
        allure.attach(body=Browser.dr.get_screenshot_as_png(),name='截图',attachment_type=allure.attachment_type.PNG)

    def select_opt(self,element,type='index',opt=''):
        '''
        :param element: 浏览器元素
        :param type: 告诉浏览器用什么定位,index,value,text
        :param opt: 选择值
        :return:
        '''
        ele = Browser.dr.find_element(*element)
        options = Select(ele)
        if type == 'index':
            # 通过下标选下拉框
            options.select_by_index(opt)
        elif type == 'value':
            '''通过value值选下拉框'''
            options.select_by_value(opt)
        elif type == 'text':
            '''通过文本内容选择下拉框'''
        else:
            '''随机取一个'''
            select_element = Browser.dr.find_element(*element) # 返回定位元素列表
            random_select = Select(select_element)
            options = random_select.options # 所有的选项
            random_select._setSelected(random.choice(options)) # 随机选择一个
            time.sleep(1)
    def assert_text_equals(self,element,txt=''):
        '''通过返回的text值进行断言'''
        assert Browser.dr.find_element(*element).text == txt,'断言失败'

    def assert_attribule_equals(self,element,attr,value):
        '''根据属性值进行断言'''
        assert Browser.dr.find_element(*element).get_attribute(attr) == value ,'attribule断言失败'
    def switch_to(self,value):
        '''断言弹窗值'''
        assert Browser.dr.switch_to.alert.text == value,'弹窗断言失败'
    def input_switch_to(self,value):
        '''弹窗输入'''
        Browser.dr.switch_to.alert.send_keys(value)

@pytest.fixture
def login_object() -> Logged_in:
    Browser().Max_Browser()
    Browser().implicitly_wait()
    Browser().get_url(read_configini().get('pytest','url')) # 读配置文件的url地址
    print(read_configini().get('pytest','username_element')[1:-2].split(','),read_configini().get('pytest','user_value'))
    Browser().input(element=[read_configini().get('pytest','username_element')[2:7],read_configini().get('pytest','username_element')[10:-2]],value=read_configini().get('pytest','user_value')) # 输入用户名
    Browser().input(element=[read_configini().get('pytest','password_element')[2:7],read_configini().get('pytest','password_element')[10:-2]],value=read_configini().get('pytest','password_value')) # 输入密码
    Browser().input(element=[read_configini().get('pytest', 'verifycode_element')[2:7],read_configini().get('pytest','verifycode_element')[10:-2]], value=read_configini().get('pytest','verifycode_value'))# 输入验证码
    Browser().click(element=[read_configini().get('pytest','click_element')[2:7],read_configini().get('pytest','click_element')[10:-2]])
    yield Browser
if __name__ == '__main__':
    print(read_configini().get('pytest','url'))