import json
import requests
import sys
e=sys.argv[1]
url="http://api.weatherapi.com/v1/current.json?key=e7831ff2a2fc4d358c855310212212&q="
url2="&aqi=yes"
req=url+e+url2
x=requests.get(req)
y=x.text
z=json.loads(y)
a=z["location"]
b=a["name"]
cur=z["current"]
temp=cur["temp_c"]
print(b,temp)


