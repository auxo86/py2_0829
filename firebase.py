# encoding=utf-8
import requests
import datetime

url = 'https://cool-cf19a.firebaseio.com/'
request1 = requests.put(url + '/data1_string.json', json='Hello World 0829')
print request1.status_code, request1.content
request2 = requests.put(url + '/data2_utf_chinese.json', json=u'中文0829')
print request2.status_code, request2.content
request3 = requests.put(url + '/data3_chinese.json', json='中文非utf八月二十九號')
print request3.status_code, request3.content
object1 = {'name':'Mark', 'age': 42}
request4 = requests.put(url + '/data4_obj.json', json=object1)
print request4.status_code, request4.content
# 插入None, 3就沒有了
array1 = ['Mark', True, 3.1415926, None, '2.968', 0, 2.968]
request5 = requests.put(url + '/data5_array.json', json=array1)
print request5.status_code, request5.content
# /代表路徑
request6 = requests.put(url + '/can/be/any/path/sample.json', json='Hello World ' + str(datetime.datetime.utcnow()))
print request6.status_code, request6.content