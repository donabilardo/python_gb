import requests
from bs4 import BeautifulSoup as bs
import lxml
import csv
import json

header = {
    "accept" : "*/*",
    "sec-ch-ua-platform" : "Windows",
    "sec-ch-ua" : "'Not A;Brand';v='99', 'Chromium';v='101', 'Google Chrome';v='101'",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
URL = "https://kinoprostor.ru/"
AJAX_URL = "https://kinoprostor.ru/?ajax=Y&movie="

def get_html_source():
    req = requests.get(URL, headers=header)
    src_html = req.text
    with open("prostor.html", "w", encoding="utf-8") as html_file:
        html_file.write(src_html)


with open("prostor.html", "r", encoding="utf-8") as html_file:
    src = html_file.read()

soup = bs(src, "lxml")

items_films_block = soup.find_all(class_ = "wrap-content-tab")

""" for item in items_films_block:
    print(item) """


#print(src_html)


""" 
all_links = soup.find_all("a")
for item in all_links:
    print(URL,item.get("href")) """


film_name = ""
film_genre = ""
film_duration = ""
film_discont = ""
price_film = ""
