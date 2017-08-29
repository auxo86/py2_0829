import requests

url = 'https://bugzilla.mozilla.org/rest/bug/35'
result = requests.get(url)
print result.status_code, result.headers['content-type']
print [bug['cc'] for bug in result.json()['bugs']]
print [bug['cc_detail'][0] for bug in result.json()['bugs']]