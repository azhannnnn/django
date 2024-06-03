import requests
import json

URL = "http://127.0.0.1:8000/api/list/"

data = {
    "username":"AzhanKhan",
    "first_name":"Azhan",
    "last_name":"Khan",
    "email":"Azhan@gmail.com",
    "password":"azhan123"
}

json_data = json.dumps(data)
# print(json_data)
r = requests.post(url=URL,data=json_data)
data1 = r.json()
print(data1)