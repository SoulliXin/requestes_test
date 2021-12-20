import requests
from aglione_interface_test.Unit.handle_excel import hd_excel
import json




url = "http://192.168.2.160/agileone/index.php/proposal/add"
data1 = hd_excel.get_cell_value(18,8)
print(data1)
data = json.loads(data1)
cookie = {"PHPSESSID":"d7f6cf86de222faf4fb7bc2984fa711a"}

res = requests.post(url=url,data=data,cookies=cookie)
print(res.text)