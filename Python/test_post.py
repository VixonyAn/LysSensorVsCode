import requests
url='https://localhost:7169/api/LightSensor'
payload={'TimeTurnedOn':int(1e9),'LightLevel':1.0,'IsDrawn':False,'LightsOn':False}
print('Posting to',url)
try:
    # skip verification of the local dev self-signed cert
    r=requests.post(url,json=payload,verify=False,timeout=5)
    print('status',r.status_code)
    print('text',r.text)
except Exception as e:
    print('error',repr(e))
