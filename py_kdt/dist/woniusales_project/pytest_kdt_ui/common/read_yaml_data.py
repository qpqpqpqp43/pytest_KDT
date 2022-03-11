'''Yaml_read_or_writer usr read or writer yaml format files!'''

class Yaml_read_or_writer(object):
    def __init__(self,Login_file_path='F:\WN\dist\woniusales_project\pytest_kdt_ui\data\case.yaml'):
        '''读取文件地址为实例属性'''
        self.Login_file_path = Login_file_path
    def read_yaml(self):
        '''读取yaml文件格式'''
        from yaml import load,dump
        try:
            from yaml import CLoader as Loader,Cdumper as Dumper
        except ImportError:
            from yaml import Loader,Dumper
        with open(self.Login_file_path,'r',encoding='utf8') as f:
            data = load(f,Loader=Loader)
            return data
    def writer_yaml(self,data):
        from yaml import load,dump
        try:
            from yaml import CLoader as Loader,CDumper as Dumper
        except ImportError:
            from yaml import Loader, Dumper
        with open(self.Login_file_path,'w',encoding='utf8') as f:
            out_put = dump(data=data,Dumper=Dumper,allow_unicode=True)
            f.write(out_put)

if __name__ == '__main__':
    f = Yaml_read_or_writer().read_yaml()
    print(f)