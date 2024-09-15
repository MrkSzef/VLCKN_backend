import requests
import asyncio
import json
from flask import Flask
import datetime

app = Flask(__name__)

with open('config.json') as f:
    config = json.load(f)

def init():
    global Session
    Session = requests.Session()
    requests.utils.add_dict_to_cookiejar(Session.cookies, {"cookie": config["cookie"]})
    request_test = Session.get(url=f"https://uczen.eduvulcan.pl/piotrkowtrybunalski/App/TWpBd056SXROVE16TWkweExUUT0/tablica")
    if request_test.status_code != 200:
        raise requests.exceptions.ConnectionError("Cookie Expired")

#print(request.text)


@app.route('/plan_zajec', methods=['GET'])
async def test():
    weekday_start = datetime.datetime.date(datetime.datetime.now()) - datetime.timedelta(days=datetime.datetime.weekday(datetime.datetime.now()))
    data = {
    "key":"TWpBd056SXROVE16TWkweExUUT0",
    "dataOd":weekday_start.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "dataDo":(weekday_start+datetime.timedelta(days=6)).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "zakresDanych":1
    }
    
    headers = {"cookie":config["cookie"]}

    request = Session.get(url=f"{config['api_endpoint']}79ad9207-6132-427d-bbfa-62a7cff7735f",params=data,headers=headers)
    return request.text,200


if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0')