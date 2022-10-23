#!/usr/bin/python3
from urllib import parse
import urllib.request
import json
import time

too_difficult_words = list()

with open("korplain.txt") as f:
    difficult_words = [l.replace('\n', '') for l in f.readlines()]
    too_difficult_words = [w.replace('*', '') for w in difficult_words if w.endswith('*')]

url = "https://plainkorean.kr/api.jsp?"

for tdw in too_difficult_words:
    thisurl = url + parse.urlencode([("keyword", tdw)])
    f = urllib.request.urlopen(thisurl)
    response = f.read().decode("utf-8")
    #print(response)
    data = json.loads(response)[0]
    easyword = data["alt"]
    print(f"{tdw}\t{easyword}")
    time.sleep(0.5)
    
