#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
import sys
import re
import time
import urllib


usage = '''Usage:
python wikipedia.py <command> [content id]
'''

description = '''Description:
Available commands are page and help.
'''

examples = '''Examples:
python wikipedia.py page "파이썬"
'''


def pagecontent(url):
    result = ''
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    for content in soup.select('.mw-body'):
        result += content.text

    return result


if not 2 <= len(sys.argv) <= 3:
    print("Number of arguments is not matched")
    print("Try \"python wikipedia.py help\".")
    sys.exit(1)

cmd = sys.argv[1]

if cmd == "help":
    print(usage)
    print(description)
    print(examples)
    sys.exit()

contentid = sys.argv[2]

if cmd == "page":
    pageurl = 'https://ko.wikipedia.org/wiki/' + urllib.parse.quote(contentid)
    print(pagecontent(pageurl))

else:
    print(f"Not available command: {cmd}")
    print("Try \"python wikipedia.py help\".")
    sys.exit(usage)

