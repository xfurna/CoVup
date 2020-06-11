import requests
import json

with open('targets.json') as f:
  targets = json.load(f)

dist_daily='https://api.covid19india.org/districts_daily.json'
# zones='https://api.covid19india.org/zones.json'

dist_daily_json=requests.get(dist_daily).json()
# zones_json=requests.get(zones).json()

for user in targets['registered']:
    print("emailing to: " + user['email'])
    obj=dist_daily_json['districtsDaily'][user['state']][user['district']]
    for objj in obj: 
        for arg, val in objj.items():
            print(arg, val)
