import configparser
import os
import sys

base_path = os.path.abspath(os.path.dirname(__file__)).split('Unit')[0]
sys.path.append(base_path)




class HandIni:

    def load_ini(self):
        ini_path = os.path.join(base_path,'Config/server.ini')
        cf = configparser.ConfigParser()
        cf.read(ini_path,encoding='utf-8-sig')
        return cf

    def get_ini_value(self,section,key):
        cf = self.load_ini()
        data = cf.get(section,key)
        return data

hdini= HandIni()

if __name__ == '__main__':
    x = HandIni()
    res = x.get_ini_value('server','host')
    print(res)





