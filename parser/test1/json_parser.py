import requests
import json


json_file = open("webinars.json", 'r', encoding="utf-8")

#  Прочитать файл в формате json
json_data = json.load(json_file)

#  Распарсить результат
for item in json_data:
  print(item["name"])
  print(item["speaker"])
  print("____________________")

json_file.close()