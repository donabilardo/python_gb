import requests

url = "http://34.88.133.100/api/login-with-password"

payload = {"login": "admin", "password": "12345"}

result = requests.post(url, payload)


print(result)
