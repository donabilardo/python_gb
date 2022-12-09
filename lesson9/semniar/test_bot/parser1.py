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
result = []
result_item = {}

def get_html_source():
    req = requests.get(URL, headers=header)
    src_html = req.text
    with open("prostor.html", "w", encoding="utf-8") as html_file:
        html_file.write(src_html)


with open("prostor.html", "r", encoding="utf-8") as html_file: #читаем полученный на предыдущем этапе html
    src = html_file.read()

soup = bs(src, "lxml") #получаем суп

data = soup.find_all("div", class_ = "wrap-content-tab") # суп из найденых дивов которые содержат информацию о фильме

count_for_popup_list = 0 #счётчик для перебора описания фильма в попап окне

for item in data:

    random_sleep_time()

    film_name = item.find("div", class_ = "name").find("h3").find("a").text.strip()
    film_genre = item.find("div", class_ = "genre").find("span").text.strip()
    film_duration = item.find("div", class_ = "duration").find("span").text.strip()
    film_poster_prev = HOST + item.find("div", class_ = "wrap-img").find("a").find("img").get("src")
    film_popup = AJAX_URL + item.find("div", class_ = "wrap-img").find("a").get("data-movie")

    src_get_popup = requests.get(film_popup, headers=header)
    src_popup = src_get_popup.text
    soup_popup = bs(src_popup, "lxml")
    film_decription = soup_popup.find("div", class_ = "right__descript-move").find("p").text.strip()
    film_youtube = soup_popup.find("div", class_ = "wrap-play").find("a").get("href")
    #film_producer = soup_popup.find("div", class_ = "list-movie").find("p").text.strip()
    #appael.find_all('p', class_='appeal-element-bottom')[2]
    #film_producer = soup_popup.find_all("div", class_ = "item__list-movie")[count_for_popup_list]



    result.append({\
        "film_name" : film_name, "film_genre" : film_genre, \
        "film_duration" : film_duration, "film_poster_prev" : film_poster_prev, \
        "film_popup": film_popup, "film_decription" : film_decription, \
        "film_youtube" : film_youtube, "film_producer" : film_producer \
            })

    count_for_popup_list = count_for_popup_list + 1




#print(f'Фильм: {film_name} \nЖанр: {film_genre} \nПродолжительность: {film_duration} \
#    \nПостер(мин): {film_poster_prev} \n{film_decription}\nСмотреть превью: {film_youtube} \
#    \nПродюсер: {film_producer}\nВ ролях: {film_in_cast} \
#    \n\n') 





print(result[3])



    

