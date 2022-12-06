import requests
from bs4 import BeautifulSoup as bs
import json

URL_TEMPLATE = "https://kinoprostor.ru/"
#r = requests.get(URL_TEMPLATE)
#print(r.status_code)

#html_data = r.text

#with open("prostor.html", "w", encoding="utf-8") as write_html:
#    write_html.write(html_data)

#write_html.close()



""" with open("prostor.html", "r", encoding="utf-8") as prostor_html_file:
    my_data = prostor_html_file.read()

my_data_soup = BeautifulSoup(my_data,"html.parser")


links = my_data_soup.find_all("a")

film_name = []
for item in links:
    film_name.append(item)
del film_name[-1] """





""" r =  requests.get("https://kinoprostor.ru/?ajax=Y&movie=2864")
htd = r.text

htd_soup = BeautifulSoup(htd)
htd_soup_data = htd_soup.find("p")
print(htd_soup_data.string) """


""" 
with open("skillbox.html", "r", encoding="utf-8") as html_file:
    html_file.read()

html_file_soup = BeautifulSoup(html_file)
html_file_soup_find = html_file_soup.find("a")

print(html_file_soup_find) """




# Откроем файл
html_file = open("prostor.html", "r", encoding="utf-8")
# Прочитаем содержимое фала
html_data = html_file.read()

# Разбьем содержимое файла на html элементы 
skillbox_soup = bs(html_data)

# Найдем все теги "a"
# links = skillbox_soup.findAll("a")
links = skillbox_soup.find_all("a")

# Распарсим найденные данные 
for item in links:
  print(item.attrs)
  print(f"Курс: {item.string.strip()}, ссылка: {item.attrs['href']}")
  print()










""" json_file = open("webinars.json", 'r', encoding="utf-8")
json_data = json.load(json_file)

for item in json_data:
  print(item["name"])
  print(item["speaker"])
  print("\n")

json_file.close() """

