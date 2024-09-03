import requests
import asyncio
import json

with open('config.json') as f:
    config = json.load(f)

print(config)
data = {
    "key":"TWpBd056SXROVE16TWkweExUUT0",
    "dataOd":"2024-09-01T22:00:00.000Z",
    "dataDo":"2024-09-08T21:59:59.999Z",
    "zakresDanych":1
}
headers = {"cookie":""}

request = requests.get(url="https://uczen.eduvulcan.pl/piotrkowtrybunalski/api/79ad9207-6132-427d-bbfa-62a7cff7735f",params=data,headers=headers)
print(request.text)