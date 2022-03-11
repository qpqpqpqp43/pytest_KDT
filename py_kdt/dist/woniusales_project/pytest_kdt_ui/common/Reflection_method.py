'''类反射方法'''
# 1、导入模块
import sys
from woniusales_project.pytest_kdt_ui.config  import function_methods
def Class_read(module,cls_name,init_name) -> function_methods:
    '''
    :param module: 模块名
    :param cls_name: 类名
    :param init_name: 方法名
    :return:
    '''
    cls = getattr(module,cls_name) # 获取类
    instance = cls() # 实例
    method = getattr(instance,init_name) # 获去类的方法，或者实例方法
    return method # 返回出去调用