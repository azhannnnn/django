import requests
import json

URL = "http://127.0.0.1:8000/api/list/"
data = {'id':5}
json_data = json.dumps(data)
print(json_data)
r = requests.delete(url = URL, data = json_data)
data = r.json()
print(data)