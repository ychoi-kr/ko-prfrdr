import urllib.request
from bs4 import BeautifulSoup


url = 'https://wikidocs.net/book/1530'
with urllib.request.urlopen(url) as f:
    html = f.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.list-group-item > span')
for title in titles[1:]:
     s = title.select('span')[0].text.strip()
     print(s)
