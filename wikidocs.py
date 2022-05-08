#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
import sys
import re


usage = '''Usage:
python wikidocs.py <command> [content id]
'''

description = '''Description:
Available commands are toc, content and help.
Content id should be a number.
'''

examples = '''Examples:
python wikidocs.py toc 2
python wikidocs.py content 43
'''

if not 2 <= len(sys.argv) <= 3:
    print("Number of arguments is not matched")
    print("Try \"python wikidocs.py help\".")
    sys.exit(1)

cmd = sys.argv[1]

if cmd == "help":
    print(usage)
    print(description)
    print(examples)
    sys.exit()

contentid = sys.argv[2]
if not re.match("[0-9]+", contentid):
    print(f"{contentid} is not a number")
    sys.exit(usage)

if cmd == "toc":
    url = 'https://wikidocs.net/book/' + contentid
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('.list-group-item > span')
    for title in titles[1:]:
         s = title.select('span')[0].text.strip()
         print(s)

elif cmd == "content":
    url = 'https://wikidocs.net/' + contentid
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    for content in soup.select('div.page-content'):
        print(content.text)

else:
    print(f"Not available command: {cmd}")
    print("Try \"python wikidocs.py help\".")
    sys.exit(usage)
