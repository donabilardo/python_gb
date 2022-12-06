import requests
from bs4 import BeautifulSoup as bs
import lxml
import csv
import json
import re #регулярные выражения
from time import sleep
from random import randint

def random_sleep_time():
    res = randint(7,12)
    return res


header = {
    "accept" : "*/*",
    "sec-ch-ua-platform" : "Windows",
    "sec-ch-ua" : "'Not A;Brand';v='99', 'Chromium';v='101', 'Google Chrome';v='101'",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
HOST = "https://kinoprostor.ru"
URL = "https://kinoprostor.ru/"
AJAX_URL = "https://kinoprostor.ru/?ajax=Y&movie="

def get_html_source():
    req = requests.get(URL, headers=header)
    src_html = req.text
    with open("prostor.html", "w", encoding="utf-8") as html_file:
        html_file.write(src_html)


with open("prostor.html", "r", encoding="utf-8") as html_file: #читаем полученный на предыдущем этапе html
    src = html_file.read()

soup = bs(src, "lxml") #получаем суп

data = soup.find_all("div", class_ = "wrap-content-tab") # суп из найденых дивов которые содержат информацию о фильме

for item in data:

    film_name = item.find("div", class_ = "name").find("h3").find("a").text.strip()
    film_genre = item.find("div", class_ = "genre").find("span").text.strip()
    film_duration = item.find("div", class_ = "duration").find("span").text.strip()
    film_poster_prev = HOST + item.find("div", class_ = "wrap-img").find("a").find("img").get("src")
    film_popup = AJAX_URL + item.find("div", class_ = "wrap-img").find("a").get("data-movie")

    src_get_popup = requests.get(film_popup, headers=header)
    src_popup = src_get_popup.text
    soup_popup = bs(src_popup, "lxml")
    film_decription = soup_popup.find("div", class_ = "right__descript-move").find("p").text.strip()

    print(f'Фильм: {film_name} \nЖанр: {film_genre} \nПродолжительность: {film_duration} \nПостер(мин): {film_poster_prev} \n{film_decription}\n\n')





#print(film_poster_prev)



    

