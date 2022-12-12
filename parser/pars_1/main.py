from time import sleep
from random import randint
from bs4 import BeautifulSoup
import requests
import lxml


local_file_name = "skillbox.html"
URL = "https://kinoprostor.ru/"
AJAX_URL = "https://kinoprostor.ru/?ajax=Y&movie="
header = {
    "accept" : "*/*",
    "sec-ch-ua-platform" : "Windows",
    "sec-ch-ua" : "'Not A;Brand';v='99', 'Chromium';v='101', 'Google Chrome';v='101'",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}



def random_sleep_time(): # засыпаем на случайное время
    res = randint(4,17)
    return res

def get_soup_in_local_file(local_file): #получаем суп из локального файла
    with open(local_file, "r", encoding="utf-8") as file:
        src = file.read()
        soup = BeautifulSoup(src, "lxml")
    file.close()
    return soup

def main():

    soup = get_soup_in_local_file(local_file_name)


if __name__ == '__main__':
    main() 




