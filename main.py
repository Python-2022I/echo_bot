import os
import requests
TOKEN = os.environ['TOKEN']

url =  f'https://api.telegram.org/bot{TOKEN}/getUpdates'
r = requests.get(url)
print(r.json())