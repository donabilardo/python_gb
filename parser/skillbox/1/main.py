import requests
from bs4 import BeautifulSoup as bs
import lxml


with open("skillbox.html", "r", encoding="utf-8") as html_file:
    src = html_file.read()


soup = bs(src, "lxml")

all_links = soup.find_all("a")

for link in all_links:
    print(f"{link.text.strip()} : {link.get('href')}")
