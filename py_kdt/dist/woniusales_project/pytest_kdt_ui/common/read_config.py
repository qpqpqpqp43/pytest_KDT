'''封装一个读配置的类'''
def read_configini(fiel_ini='pytest.ini'):
    import configparser
    config = configparser.ConfigParser()
    config.read(fiel_ini,encoding='utf-8')
    return config