import requests
from bs4 import BeautifulSoup
r = requests.get('http://google.es')
soup = BeautifulSoup(r.text, 'lxml')

print(soup.title)