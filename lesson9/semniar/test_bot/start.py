import requests
from bs4 import BeautifulSoup as bs
import lxml


headers = {
":method" : "GET",
":authority" : "kinoprostor.ru",
":path" : "/",
":scheme" : "https",
"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding" : "gzip, deflate, br",
"accept-language" : "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"cache-control" : "max-age=0",
"dnt" : "1",
"referer" : "https://www.google.com/",
"sec-ch-ua" : "'Not A;Brand;' 'v=99', 'Chromium;' 'v=101', 'Google Chrome;' 'v=101'",
"sec-ch-ua-mobile" : "?0",
"sec-ch-ua-platform" : "Windows",
"sec-fetch-dest" : "document",
"sec-fetch-mode" : "navigate",
"sec-fetch-site" : "cross-site",
"sec-fetch-user" : "?1",
"upgrade-insecure-requests" : "1",
"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}







with open("skillbox.html", "r", encoding="utf-8") as html_file:
    src = html_file.read()


soup = bs(src, "lxml")

all_links = soup.find_all("a")

""" for link in all_links:
    print(f"{link.text.strip()} : {link.get('href')}") """

try:
   print(header["user-agent1"])
except KeyError:
    print("Такого ключа нет в словаре")
