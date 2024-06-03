import requests

url = "http://127.0.0.1:8000/api/list/"

r = requests.get(url)
print(r.text)
print(r.json)


