import requests
import time
    
url="https://api.btcturk.com/api/v2/ticker"

while (1):
    response=requests.get(url)
    dt=response.json()
    data={}
    data['pair']='USDTTRY'
    for i in range(0,len(dt['data'])):
        if dt['data'][i]['pair']==data['pair']:
                dataindex=i
    data['denominatorSymbol']=dt["data"][dataindex]["denominatorSymbol"]     
    data['numeratorSymbol']=dt["data"][dataindex]["numeratorSymbol"]
    data['last']=dt["data"][dataindex]["last"]
    print(""+data['numeratorSymbol']+" / "+data['denominatorSymbol']+" = "+str(data['last'])+"\n")
    time.sleep(1)
 
