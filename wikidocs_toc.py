from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://wikidocs.net/book/2'
driver.get(url)

html = driver.page_source

#print(html)

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.list-group-item > span')
#print(titles)
for title in titles[1:]:
     s = title.select('span')[0].text.strip()
     print(s)
