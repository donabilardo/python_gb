import requests
from bs4 import BeautifulSoup as bs
import lxml
import csv

header = {
    "accept" : "*/*",
    "sec-ch-ua-platform" : "Windows",
    "sec-ch-ua" : "'Not A;Brand';v='99', 'Chromium';v='101', 'Google Chrome';v='101'",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
URL = "https://kinoprostor.ru/"

req = requests.get(URL, headers=header)

src_html = req.text

""" with open("prostor.html", "r", encoding="utf-8") as html_file:
    src = html_file.read()

soup = bs(src, "lxml") """


print(src_html)