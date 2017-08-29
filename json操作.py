# encoding=utf-8
import json

data1 = {'name': 'Mark', 'age': 42, 'weight': 73.5}
string1 = json.dumps(data1)
print string1

objFromJSON = json.loads(string1)
print type(objFromJSON)
print objFromJSON['name'], objFromJSON['age'], objFromJSON['weight']
data2 = ['Sun', 'Mon', u'火曜日']
string2 = json.dumps(data2, encoding='utf8')
print string2
arrayFromJSON = json.loads(string2)
for item in arrayFromJSON:
    print item

print [item for item in arrayFromJSON]
data3 = {'name':'19thTyphoon', 'date':['Sep-1', 'Sep-2', 'Sep-3']}
string3 = json.dumps(data3)
print string3
obj2FromJSON = json.loads(string3)
print [dateString for dateString in obj2FromJSON['date']]
