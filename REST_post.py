# encoding=utf-8
import requests

url = 'https://cool-cf19a.firebaseio.com/'

for i in range(0,10):
    obj1 = {'name': 'Mark', 'id': i}
    # 執行完會回傳一個unikey
    result = requests.post(url + '/data_post_obj_new.json', json=obj1)
    print result.status_code, result.content