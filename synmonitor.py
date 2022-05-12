import sys
from flask import Flask,Response
from datetime import datetime
import requests
import time
import json 
from configparser import ConfigParser

app = Flask(__name__)

c=ConfigParser()

#Read from config file
read = c.read('config.ini')
print("Read from config file",read)

#Get endpoint from ini file
url = c.get('endpoint','url')
print("End point is ",url)

#Fetch no of hits
hits = c.get('endpoint','hits')
print("Set no of hits to ...",hits)


#sleep time
pollperiod = c.get('endpoint','pollperiod')
print("Configured poll period is....", pollperiod)


@app.route("/syn")
def web():
    now = datetime.now()
    current_time=now.strftime("%H:%M:%S")
    resp=requests.get(url,verify=True)
    var=resp.text
    status=resp.status_code
    #print("Response:::",var)
    i=0
    d=list()
    for i in range(int(hits)):
        list_entries=str(i)+'::'+current_time+'::'+'RespCode:'+str(status)
        d.append(list_entries)
        print("Entries:",d,"Type:",type(d))
        #print("Components:\n",d[i].split("::"))
        clist=d[i].split("::")
        print("Type::clist",type(clist))
        data=clist[0]+' '+clist[1]+' '+clist[2]
        print("Data cleansed",data,"Type",type(data))
        time.sleep(float(pollperiod))
        if i>int(hits):
          break  
     
    def events(): 
     for k in range(len(d)):
        yield str(d[k].split("::"))
        yield '\n'    
    
    return Response(events(),content_type='text/event-stream')


