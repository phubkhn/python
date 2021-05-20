import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.japc.co.jp/pis/tokai/unten.htm")
soup = BeautifulSoup(response.content, 'html.parser')
divs = soup.findAll('div', id='sprytooltip4')
for x in divs:
    print(x.find('p').text)