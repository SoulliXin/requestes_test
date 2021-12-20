import os
import sys
import requests
import json
base_path = os.path.abspath(os.path.dirname(__file__)).split('Base')
sys.path.append(base_path)
from aglione_interface_test.Unit.handle_ini import hdini
from aglione_interface_test.Unit.handle_cookies import write_cookie

class BaseRequest:

    def send_post(self,url,data,cookie=None,get_cookie=None,headers=None):
        '''
        send post method request
        '''
        response =  requests.post(url=url,data=data,cookies=cookie,headers=headers)
        if get_cookie !=None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])

        res = response.text
        return res

    def send_get(self,url,data,cookie=None,get_cookie=None,headers=None):
        '''
        send get method request

        '''

        response = requests.get(url=url,data=data,cookies=cookie,headers=headers)
        if get_cookie !=None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self,method,url,data,cookies=None,get_cookie=None,headers=None):
        base_url = hdini.get_ini_value('server','host')
        if 'http' not in url:
            url = base_url + url
        if method == 'post':
            res = self.send_post(url,data,cookies,get_cookie,headers)
        else:
            res = self.send_get(url,data,cookies,get_cookie,headers)
        # try:
        #     res = json.loads(res)
        # except:
        #    print('This is a text response')
        return res



base_requst = BaseRequest()


if __name__ == '__main__':
    b = BaseRequest()
    url = 'http://172.17.118.75/agileone/index.php/common/login'
    data = {
        "username":"admin",
        "password":"admin",
        "savelogin":False
    }
    response = requests.post(url,data)
    cookie_jar = response.cookies
    cookie_value = requests.utils.dict_from_cookiejar(cookie_jar)
    print(cookie_value)
    print(type(cookie_value))






