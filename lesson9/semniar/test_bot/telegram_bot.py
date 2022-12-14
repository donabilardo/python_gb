import requests

url_api = "https://api.telegram.org/bot5930634936:AAEb5i1G9q3QWqSVJ2xRoOs1FrJjJ4GtApY"


updates = requests.get(url_api + "/getUpdates").json()

print(updates)