import requests
import time
    
url="https://api.btcturk.com/api/v2/ticker"

while (1):
    response=requests.get(url)
    dt=response.json()
    data={}
    data['denominatorSymbol']=dt["data"][5]["denominatorSymbol"]     
    data['numeratorSymbol']=dt["data"][5]["numeratorSymbol"]
    data['last']=dt["data"][5]["last"]
    print(""+data['numeratorSymbol']+" / "+data['denominatorSymbol']+" = "+str(data['last'])+"\n")
    time.sleep(1)
