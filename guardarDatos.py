import requests
from español import SPANISH

for palabra in SPANISH:
    myobj = {"name": palabra, "language": "ES"}
    try:
        print(requests.post("https://localhost:5001/api/createword", json=myobj, verify=False).json())
    except Exception:
        print('come pinga lol')