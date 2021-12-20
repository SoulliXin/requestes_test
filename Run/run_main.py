import os
import sys
import json
base_path = os.path.abspath(os.path.dirname(__file__)).split('Run')[0]
sys.path.append(base_path)
from aglione_interface_test.Base.base_requsts import base_requst
from aglione_interface_test.Unit.handle_excel import hd_excel
from aglione_interface_test.Base.var_number import var
from aglione_interface_test.Unit.handle_cookies import get_cookie_value
from jsonpath_rw import parse
from aglione_interface_test.Unit.handle_db import query_db_data
from aglione_interface_test.Unit.handle_ini import hdini
from aglione_interface_test.Unit.hand_result import get_result_json,handle_result_json
from aglione_interface_test.Unit.handle_depend import depend_data


class RunMain:

    def run_case(self):
        rows = hd_excel.get_rows()
        for i in range(rows):
            data = hd_excel.get_row_data(i+2)
            is_run = data[var.get_is_run_nb()]
            if is_run == 'yes':
                cookies = None
                headers = None
                get_cookie = None
                is_depend = data[var.get_condition_nb()]
                depend_key = data[var.get_depend_way_nb()]
                cookie_method = data[var.get_cookie_nb()]
                method = data[var.get_method_nb()]
                url = data[var.get_url_nb()]
                data_str = data[var.get_data_nb()]
                data1 = json.loads(data_str)
                expected_way = data[var.get_expected_way_nb()]
                if is_depend:
                    depend_datas = depend_data(is_depend)
                    data1[depend_key] = depend_datas
                if cookie_method == 'yes':
                    cookies = get_cookie_value('web')
                if cookie_method == 'write':
                    get_cookie = {"is_cookie":"web"}
                res = base_requst.run_main(method,url,data1,cookies,get_cookie,headers)
                print(data1)
                if expected_way == 'db':
                    sql = hdini.get_ini_value('server','sql')
                    excected_data = query_db_data(sql)[0][0]
                    actual = int(res)
                    if excected_data == actual:
                        hd_excel.excel_write_data(i + 2, var.get_result_nb() + 1, 'pass')
                    else:
                        hd_excel.excel_write_data(i + 2, var.get_result_nb() + 1, 'fail')
                if expected_way == 'messeage':
                    expected_data = data[var.get_expected_result()]
                    if expected_data == res:
                        hd_excel.excel_write_data(i+2,var.get_result_nb()+1,'pass')
                    else:
                        hd_excel.excel_write_data(i+2,var.get_result_nb()+1,'fail')
                if expected_way == 'json':
                    res_data = json.loads(res)
                    if  handle_result_json(res_data[0],get_result_json(url)):
                        hd_excel.excel_write_data(i + 2, var.get_result_nb() + 1, 'pass')
                    else:
                        hd_excel.excel_write_data(i + 2, var.get_result_nb() + 1, 'fail')
                hd_excel.excel_write_data(i+2,var.get_response_nb()+1,res)




if __name__ == '__main__':
    x = RunMain()
    x.run_case()



