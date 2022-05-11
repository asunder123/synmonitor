import sys
from flask import Flask
from datetime import datetime
import requests
import time

app = Flask(__name__)

val = input("Enter url")
print(val)


@app.route("/app")
def web():
    now = datetime.now()
    current_time=now.strftime("%H:%M:%S")
    resp=requests.get(val,verify=True)
    var=resp.text
    status=resp.status_code
    print("Response:::",var)
    i=0
    d=list()
    for i in range(100):
        list_entries=str(i)+'::'+current_time+'::'+'RespCode:'+str(status)
        d.append(list_entries)
        print("Entries:",d)
        time.sleep(1)
        k=str(d)
        if i>100:
            break
    return k


