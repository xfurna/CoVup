import requests
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template


admin_id = 0
host_id = 0
PASSWORD="update.exp1"


dist_daily='https://api.covid19india.org/districts_daily.json'
# zones='https://api.covid19india.org/zones.json'

# with open('../meta.json') as f:
#   meta = json.load(f)

meta={
    "registered" : [
        {
            "name": "evi1",
            "email" : "archi7dwivedi@gmail.com",
            "district" : "Lucknow",
            "state" : "Uttar Pradesh"
        },
        
        {
            "name": "Archit",
            "email" : "architdwivedi.off@gmail.com",
            "district" : "Mathura",
            "state" : "Uttar Pradesh"
        }
    ],

    "admins" : [
        {
            "id" : 0,
            "name": "idiot",
            "email" : "idiotnotidiot@gmail.com",
            "district" : "Lucknow",
            "state" : "Uttar Pradesh"
        },

        {
            "id" : 1,
            "name": "evi1haxor",
            "email" : "architdwivedi.0ff@gmail.com",
            "district" : "Lucknow",
            "state" : "Uttar Pradesh"
        }
    ],
    
    "host-params" : [
        {
            "id" : 0,
            "HostName" : "smtp.gmail.com",
            "port" : 587
        }
    ]
}

s = smtplib.SMTP(host=meta['host-params'][host_id]['HostName'], port=meta['host-params'][0]['port'])
s.starttls()
s.login(meta['admins'][admin_id]['email'], PASSWORD)



dist_daily_json=requests.get(dist_daily).json()
# zones_json=requests.get(zones).json()

for user in meta['registered']:
    print("emailing to: " + user['email'])
    dist_ = dist_daily_json['districtsDaily'][user['state']][user['district']]
    # print("Active: ", dist_[-1]['active'])
    # print("Confirmed: ", dist_[-1]['confirmed'])
    # print("Deceased: ", dist_[-1]['deceased'])
    # print("Recovered: ", dist_[-1]['recovered'])
    # print("Date: ", dist_[-1]['date'])
    msg = MIMEMultipart()
    PERSON_NAME=user['name']
    ACTIVE_CASES=dist_[-1]['active']
    CONF_CASES=dist_[-1]['confirmed']
    RECOV_CASES=dist_[-1]['recovered']
    DEC_CASES=dist_[-1]['deceased']
    DATE=dist_[-1]['date']

    message="Hi "+PERSON_NAME+"!\n"+"As of " + str(DATE) + " " + user['district']+" has " + str(ACTIVE_CASES) + " active cases, " + str(CONF_CASES) + " confirmed cases, " + str(RECOV_CASES) + " recovered cases and " + str(DEC_CASES) + " deceased cases.\n\nStay safe!\n\nYours Truly\n---\nevi1haxor"
    
    msg['From']=meta['admins'][admin_id]['email']
    msg['To']=user['email']
    msg['Subject']="Today's Update!"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    
    del msg


