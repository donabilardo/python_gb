from bs4 import BeautifulSoup as bs
import lxml

with open("blank/index2.html", "r", encoding="utf-8") as file:
    src = file.read()
#print(src)

soup = bs(src, "lxml")

title = soup.title # заголовок страницы
print(title) #вместе с тегом
print(title.string) #только текст


page_h1 = soup.find("h1") #находит первый тег
page_h1 = soup.find("span") 
print(page_h1)


pahe_h1_all = soup.find_all("span") #находит все теги и записывает найденное в список
print(pahe_h1_all)


