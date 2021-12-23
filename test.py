import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/20")
print(response.json())

#response2 = requests.post(BASE + "helloworld")
#print(response.json())