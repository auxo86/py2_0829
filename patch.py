# encoding=utf-8
import requests

url = 'https://cool-cf19a.firebaseio.com/'
object_patch = {'name': 'Mark Ho', 'location':'Taipei'}
result = requests.put(url + '/data4_obj.json', json=object_patch)
object_patch2 = {'0':'Meng-Hang Ho', '3': 'ucom', '7': 'something new'}
result2 = requests.put(url + '/data5_array.json', json=object_patch2)
print result.status_code, result.content
print result2.status_code, result2.content