import os
import sys
base_path = os.path.abspath(os.path.dirname(__file__)).split('Unit')[0]
sys.path.append(base_path)
from aglione_interface_test.Unit.handle_excel import hd_excel
from jsonpath_rw import parse
from aglione_interface_test.Unit.handle_excel import hd_excel
import json

def split_data(data):
    '''
    拆分数据字段
    '''
    # case_id>noticeid
    case_id = data.split('>')[0]
    rule_data = data.split('>')[1]
    return case_id,rule_data



def depend_data(data):
    '''
    获取数据依赖集
    '''
    case_id = split_data(data)[0]
    rows_number = hd_excel.get_rows_number(case_id)
    data = hd_excel.get_cell_value(rows_number,14)
    return data

def get_depend_data(res_data,key):
    '''
    '''
    res_data = json.loads(res_data[0])
    print(res_data)
    json_exe =parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]

def get_data(data):
    '''
    获取依赖数据
    '''
    res_data = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data,rule_data)

if __name__ == '__main__':
   data = hd_excel.get_cell_value(10,14)
   print(data[0])
