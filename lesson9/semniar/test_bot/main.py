import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = "https://oto-register.autoins.ru/oto/"
r = requests.get(URL_TEMPLATE)
print(r.status_code)