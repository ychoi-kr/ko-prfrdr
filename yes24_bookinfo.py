#!/usr/bin/python3

from bs4 import BeautifulSoup
import argparse

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

    detail = soup.select("textarea.txtContentText")
    desc = detail[0]
    toc = detail[1]

    return {
        "goodsid": goodsid,
        "title": title,
        "url": url,
        "author": author.strip(),
        "pubdate": soup.select_one("span.gd_date").text,
        "desc": desc.text,
        "toc": toc.text
    }

def main(goodsid):
    for k, v in bookinfo(goodsid, showurl=None).items():
        print(k, v)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("goodsid", type=str)
    args = parser.parse_args()
    main(args.goodsid)

