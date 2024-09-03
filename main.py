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
headers = {"cookie":"EfebSsoCookie=8MelOCc3ziGH_WhGZR-Udh22NhMLCD9tqjP-J8lKQ4onE6-F_VcFeY-4UgOrTM8_Sq6JSe6W1mGaV931J3SmyP3Lwv7d6ml5vhXb0s2E3bc7EDet5O1CfoHpwCYgrdVXM7GkhM2AAz_jSfzgK0fzRgYd57b_vOUj5Rym8PoB0fOYPwzhGBYibt8l2lQRyNDusC-UPM4KU2OmL8fcaaTRFC2_Q3WxUsZqv3wVUW_vO1GMiUocVl99fpBOT8CHoi5lg4KUVVdB0i7PoUNST1bNCV3rbkQNDlca7iP2;"}

request = requests.get(url="https://uczen.eduvulcan.pl/piotrkowtrybunalski/api/79ad9207-6132-427d-bbfa-62a7cff7735f",params=data,headers=headers)
print(request.text)