from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint
import lxml
import json
import requests
import os

def random_sleep_time(): #засыпаем от 4 до 10 сек (имитация пользователя)
    res = randint(4,10)
    sleep(res)

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

def get_html_source(): #обновляем дынные с удаленного сервера
    req = requests.get(URL, headers=header)
    src_html = req.text
    with open("prostor.html", "w", encoding="utf-8") as html_file:
        html_file.write(src_html)
get_html_source()

with open("prostor.html", "r", encoding="utf-8") as html_file: #читаем полученный на предыдущем этапе html
    src = html_file.read()

soup = bs(src, "lxml") #получаем суп
data = soup.find_all("div", class_ = "wrap-content-tab") # суп из найденых дивов которые содержат информацию о фильме

for item in data:

    random_sleep_time()

    film_name = item.find("div", class_ = "name").find("h3").find("a").text.strip()
    film_genre = item.find("div", class_ = "genre").find("span").text.strip()
    film_duration = item.find("div", class_ = "duration").find("span").text.strip()
    film_poster_prev = HOST + item.find("div", class_ = "wrap-img").find("a").find("img").get("src")
    film_popup = AJAX_URL + item.find("div", class_ = "wrap-img").find("a").get("data-movie")

    film_type = item.find("div", class_ = "time-film").get("data-format")

    time_film = item.find_all("div", class_ = "time-film") #получаем все элементы с датой показа
    time_film_list = [] 
    for i in time_film:
        time_film_list.append(i.text)
        
    price_film = item.find_all("div", class_ = "price-film") #получаем все элементы со стоимостью билета на кино
    price_film_list = []
    for i in price_film:
        price_film_list.append(i.text)

    time_and_price = zip(time_film_list,price_film_list) #склеиваем дату показа и стоимость кинофильма
    time_and_price_dict = dict(time_and_price) #преобразуем кортеж в словарь


    src_get_popup = requests.get(film_popup, headers=header)
    src_popup = src_get_popup.text
    soup_popup = bs(src_popup, "lxml")

    random_sleep_time()

    film_decription = soup_popup.find("div", class_ = "right__descript-move").find("p").text.strip()
    film_decription = film_decription[0: len(film_decription) - 28]
    film_youtube = soup_popup.find("div", class_ = "wrap-play").find("a").get("href")
    film_producer = soup_popup.find("div", class_ = "list-movie").next_element.next_element.next_element.next_element.next_element.next_element
    film_role = soup_popup.find("div", class_ = "list-movie").next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.text.strip()
    film_role = film_role.replace("В ролях", "")


    
    result.append({\
        "film_name" : film_name, "film_genre" : film_genre, \
        "film_duration" : film_duration, "film_poster_prev" : film_poster_prev, \
        "film_popup": film_popup, "film_decription" : film_decription, \
        "film_youtube" : film_youtube, "film_producer" : film_producer,  "film_role" : film_role,\
        "film_type" : film_type, "time_film" : time_film_list, "price_film" : price_film_list, \
        "time_and_price": time_and_price_dict
            })




with open ("shedule.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, indent=2, ensure_ascii=False)

for item_film in result:
    print(f"Фильм: {item_film['film_name']} [{item_film['film_type']}]")
    print(f"{item_film['film_decription']}")
    print(f"Жанр: {item_film['film_genre']}   {item_film['film_duration']}")
    print(f"Режиссёр: {item_film['film_producer']}")
    print(f"В ролях: {item_film['film_role']}")
    print(f"Постер: {item_film['film_poster_prev']}")
    print(f"Трейлер: {item_film['film_youtube']} \n")

    print("Расписание сеансов: ")
    for key, value in item_film['time_and_price'].items():
        print(f"Начало сеанса: {key} Стоимость: {value}")
    print("\n\n")



""" print(result[5])



with open("shedule.json", "r", encoding="utf-8") as json_file:
    data_json = json.load(json_file)
    print(type(data_json))

for item in data_json:
    print(item["film_genre"])
    print("\n") """




    
