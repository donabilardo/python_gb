import requests


url = "http://34.88.133.100/api/login-with-password"
payload = {"login": "root", "password": "12345"}


result = requests.post(url,payload)


#2** - Ок
#3** - редирект
#4** - ошибка клиента
#5** - ошибка сервера

print(result)
