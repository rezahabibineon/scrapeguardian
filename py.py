##
## script for run cronjob
##


import requests
from apps.helper import Log


url = 'http://192.168.97.160:8001/scrape_news'

headers = {
    'X-Api-Token': 'dev'
    } 

try:
    resp = requests.post(url=url, headers=headers)
    Log.info('success scraping')
except Exception as e:
    Log.warn(f'error scraping : {e}')   