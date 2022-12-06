from bs4 import BeautifulSoup as bs
import lxml

with open("blank/index2.html", "r", encoding="utf-8") as file:
    src = file.read()
# print(src)

soup = bs(src, "lxml")

title = soup.title  # заголовок страницы
# print(title) #вместе с тегом
# print(title.string) #только текст


page_h1 = soup.find("h1")  # находит первый тег
page_h1 = soup.find("span")
# print(page_h1)


# находит все теги и записывает найденное в список
pahe_h1_all = soup.find_all("span")
# print(pahe_h1_all)

# print(type(pahe_h1_all))

""" for item in pahe_h1_all:
    print(item.string)

article_title = soup.find_all("div", class_="post__title")

for item in article_title:
    print(item.text.strip()) """


""" aricle_titile = soup.find(class_="user__info").find_all("span")
# print(aricle_titile)
for i in aricle_titile:
    print(i.text)
 """

""" user_info = soup.find(class_="user__info").find_all """


social = soup.find(class_ = "social__networks").find("ul").find_all("a")

c = 1
for item in social:
    item_url = item.get("href") #вытскиваем ссылку - атрибут ссылки
    print("Ссылка №",c, "Текст ссылки:", item.text   , "URL: ", item_url )
    c +=1 


links = soup.find(class_ = "some__links").find_all("a")

for item in links:
    link_href = item.get("href")
    link_data = item.get("data-movie")
    print(f"{item.text} ссылка: {link_href} data-movie = {link_data}")