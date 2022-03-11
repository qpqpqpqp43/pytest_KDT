'''类反射源生类'''
# from pytest_kdt.common.Class_reflection import Class_reflection
import time

from woniusales_project.pytest_kdt_ui.common.Reflection_method import Class_read
import allure
class Class_Reflections():
    '''类反射一个大类'''

    def __init__(self,module,j):
        self.module = module
        self.j = j
        self.CR = Class_read(module=self.module,cls_name=list(self.j.values())[0].split('.')[0],init_name=list(self.j.values())[0].split('.')[1])
    def input_Class_Reflection(self):
        '''元素输入类反射'''
        b = [self.j['页面元素'], self.j['输入值']]
        self.CR(*b)
        allure.attach(body=str(self.j['输入值']), name=f'{list(self.j.keys())[0]}', attachment_type=allure.attachment_type.CSV)
    def click_Class_Reflection(self):
        '''点击操作类反射'''
        xpath = self.j['页面元素']
        self.CR(xpath)
        allure.attach(body='元素点击', name=f'{list(self.j.keys())[0]}',
                      attachment_type=allure.attachment_type.CSV)
    def get_url_Class_Reflection(self):
        '''打开网址'''
        url = self.j['网址']
        self.CR(url)
        allure.attach(body=f'{url}', name=f'{list(self.j.keys())[0]}',
                      attachment_type=allure.attachment_type.CSV)
    def implicitly_wait_Class_Reflection(self):
        '''浏览器等待'''
        time = self.j['隐式等待时间']
        self.CR(time)

    def Get_PNG_Class_Reflection(self):
        '''截图'''
        time.sleep(2)
        self.CR()

    def random_select(self):
        '''随机选择下拉框'''
        self.CR()
