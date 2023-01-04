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

def sendMessage(chat_id:str, text:str):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    r = requests.get(url,params={'chat_id':chat_id, 'text':text})
    data = r.json()
    return data

upd_len = len(getUpdates())
upd_new = 0
while True:
    update = getUpdates()[-1]
    # Get user id
  
    upd_len = len(getUpdates())
    if upd_len != upd_new:
        upd_new = upd_len
        text = update['message']['text'] # Get text
        chat_id = update['message']['chat']['id'] # Get chat id
        # Send message
        sendMessage(chat_id, text)
        print(text)

    print(f'upd_len = {upd_len}, upd_new = {upd_new}')
    sleep(2)
    
