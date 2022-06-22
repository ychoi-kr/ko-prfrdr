from bs4 import BeautifulSoup

import yes24
import spider


def bookinfo(goodsid, showurl):
    url = yes24.site + "/Product/Goods/" + goodsid
    if showurl:
        print(url)

    html = spider.readurl(url)
    soup = BeautifulSoup(html, 'html.parser')

    ebook = soup.select_one("div.gd_titArea > strong.icon_res")
    if ebook:
        title = '[' + ebook.text + '] ' + soup.select_one("h2.gd_name").text
    else:
        title = soup.select_one("h2.gd_name").text

    author = soup.select_one("span.gd_auth").text
    moreAuthArea = soup.select_one("span.moreAuthArea")
    if moreAuthArea:
        author = author.replace(moreAuthArea.text, '')

    return {
        "goodsid": goodsid,
        "title": title,
        "url": url,
        "author": author.strip(),
        "pubdate": soup.select_one("span.gd_date").text
    }

