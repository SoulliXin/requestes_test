#coding=utf-8
import os
import sys
base_path = os.path.abspath(os.path.dirname(__file__)).split('Unit')[0]
sys.path.append(base_path)
import json


class OpeerationJson:

    def __int__(self,file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = base_path + "/Config/user_data.json"

    def read_json(self):
        # if file_name == None:
        #     file_path = base_path + "/Config/user_data.json"
        # else:
        #     file_path = base_path + file_name
        with open(self.file_path,encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def get_value(self,key):
        data = self.read_json()
        return data.get(key)


    def write_value(slef,data,file_name=None):
        data_value = json.dumps(data)
        if file_name == None:
            path = base_path + "/Config/cookie.json"
        else:
            path =  base_path +  file_name

        with open(path,'w') as f:
            f.write(data_value)

if __name__ == '__main__':
    CL = OpeerationJson()
    data = {
        ""
    }
    CL.write_value(data)