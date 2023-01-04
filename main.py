import os
import requests
from pprint import pprint
from time import sleep
TOKEN = os.environ['TOKEN']

def getUpdates():
    url =  f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    r = requests.get(url,params={'limit':5})
    data = r.json()
    updates = data['result']
    return updates


upd_len = len(getUpdates())
upd_new = 0
while True:
    update = getUpdates()[-1]
    upd_len = len(getUpdates())
    if upd_len != upd_new:
        upd_new = upd_len
        text = update['message']['text']
        print(text)

    print(f'upd_len = {upd_len}, upd_new = {upd_new}')
    sleep(2)
    
