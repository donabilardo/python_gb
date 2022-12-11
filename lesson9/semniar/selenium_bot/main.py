from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
from time import sleep
from tqdm import tqdm
import requests

browser = Chrome("chromedriver.exe")
url = "https://2ip.ru/"
sleep(10)
print("hello world !!!")

#browser.get(url)

def main():
    pass

if __name__ == '__main__':
    main()