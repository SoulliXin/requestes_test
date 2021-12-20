import os
import sys
base_path = os.path.abspath(os.path.dirname(__file__)).split('Unit')[0]
sys.path.append(base_path)
from aglione_interface_test.Unit.handle_json import get_value
from deepdiff import DeepDiff


def handle_result_json(dict1,dict2):
    '''
    check two dic
    '''
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if cmp_dict.get('dictionary_item_added'):
            return False
        else:
            return True
    return False

def get_result_json(url):
    data = get_value(url,'/Config/user_data.json')
    return data


if __name__ == '__main__':
    dict1 = {
        "username":"123"
    }
    dict2 = {
        'username':'222'
    }
    x = handle_result_json(dict1,dict2)
    print(x)
