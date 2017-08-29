from bs4 import BeautifulSoup
import requests

url = 'https://www.uuu.com.tw/'
result = requests.get(url)
soup = BeautifulSoup(result.content, 'html.parser')
hot = soup.find('div', {'id':'hot'})
items = hot.find_all('a')
for item in items:
    print item