import os
import requests
TOKEN = os.environ['TOKEN']

def getUpdates():
    url =  f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url)
    data = r.json()
    updates = data['result']
    return updates


upd = getUpdates()
print(upd)

