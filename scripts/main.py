import requests
import json
import smtplib
from . import methods

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

admin_id = 0
host_id = 0
PASSWORD=""

mail_template = read_template("../templates/subscribers.txt")

dist_daily='https://api.covid19india.org/districts_daily.json'
# zones='https://api.covid19india.org/zones.json'

with open('../meta.json') as f:
  meta = json.load(f)


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

    message = mail_template.substitute(PERSON_NAME=user['name'], ACTIVE_CASES=dist_[-1]['active'], CONF_CASES=dist_[-1]['confirmed'], RECOV_CASES=dist_[-1]['recovered'], DEC_CASES=dist_[-1]['deceased'], DATE=dist_[-1]['date'])
    # message="Hi "+PERSON_NAME+"!\n"+"As of " + str(DATE) + " " + user['district']+" has " + str(ACTIVE_CASES) + " active cases, " + str(CONF_CASES) + " confirmed cases, " + str(RECOV_CASES) + " recovered cases and " + str(DEC_CASES) + " deceased cases.\n\nStay safe!\n\nYours Truly\n---\nevi1haxor"

    msg['From']=meta['admins'][admin_id]['email']
    msg['To']=user['email']
    msg['Subject']="Today's Update!"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
    
    del msg


