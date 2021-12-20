#coding=utf-8
import json
import os
import sys
base_path = os.path.abspath(os.path.dirname(__file__)).split('Unit')[0]
sys.path.append(base_path)
from aglione_interface_test.Unit.handle_json import read_json,write_value


def get_cookie_value(cookie_key):
    '''
    获取cookie
    '''
    data = read_json('/Config/cookie.json')
    return data[cookie_key]


def write_cookie(data,cookie_key):
    '''
    写入cookie
    '''
    data1 = read_json('/Config/cookie.json')
    data1[cookie_key] = data
    write_value(data1)




if __name__ == '__main__':
    data = {
        'PHPSESSID':'b663b98e48e04c2a81d063cb106916b2'
    }
    write_cookie(data,"web")