import requests
import json

URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

res = requests.get(url=URL)
data = res.json()

with open('UAH_exchange_rate.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(data)
