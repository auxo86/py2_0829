# encoding=utf-8
import requests

url = 'https://cool-cf19a.firebaseio.com/'

request1 = requests.get(url + '/data1_string.json')
print request1.status_code, request1.content
request2 = requests.get(url + '/data2_utf_chinese.json')
print request2.status_code, request2.content
request3 = requests.get(url + '/data3_chinese.json')
print request3.status_code, request3.content

request4 = requests.get(url + '/data4_obj.json')
print request4.status_code, request4.content, request4.json()
print [key + ',= ' + str(request4.json()[key]) for key in request4.json().keys()]
print [key + '/' + str(value) for key, value in request4.json().items()]

request5 = requests.get(url + '/data5_array.json')
print request5.status_code, request5.content, request5.json()
print [item for item in request5.json()]

