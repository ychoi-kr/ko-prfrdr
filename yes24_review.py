#!/usr/bin/python3

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import sys
import time


site = "http://www.yes24.com"


def main(goodsid_list, order, csv):
    if not goodsid_list:
        goodsid_list = sys.stdin

    if csv:
        print(
            '"책 제목"',
            '"URL"',
            '"저자/역자"',
            '"발행일"',
            '"작성일"',
            '"작성자"',
            '"구매"',
            '"평점"',
            '"리뷰"',
            sep=','
        )

    for goodsid in goodsid_list:
        info = bookinfo(goodsid.strip())
        time.sleep(1)
        display(
            info,
            goodsReviewList(info, order, csv) + awordReviewList(info, order, csv),
            csv
        )
        time.sleep(1)


def display(info, reviewlist, csv):
    for review in reviewlist:
        if csv:
            quote = lambda s: '"' + s.replace('"', '\"') + '"' if csv else s
            print(
                quote(info["title"]),
                quote(info["url"]),
                quote(info["author"]),
                quote(info["pubdate"]),
                quote(review["reviewdate"]),
                quote(review["reviewerid"]),
                quote(review["buy"]),
                quote(review["ratings"]),
                quote(review["review"]),
                sep=','
            )
        else:
            print(
                review["reviewdate"] + ' ' + review["reviewerid"] + ' ' + review["buy"],
                review["ratings"],
                review["review"],
                sep='\n',
                end='\n\n'
            )


def bookinfo(goodsid):
    url = site + "/Product/Goods/" + goodsid

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    return {
        "goodsid": goodsid,
        "title": soup.select_one("h2.gd_name").text,
        "url": url,
        "author": soup.select_one("span.gd_auth").text.strip(),
        "pubdate": soup.select_one("span.gd_date").text
    }


def goodsReviewList(info, order, csv):
    result = []

    sortorder = {
        "최근순": 1,
        "추천순": 2,
        "별점순": 3,
    }

    qrylist = [
        ("type", "ALL"),
        ("sort", sortorder[order]),
        ("PageNumber", 1)
    ]

    qrystr = parse.urlencode(qrylist)
    url = site + "/Product/communityModules/GoodsReviewList/" + info["goodsid"] + '?' + qrystr

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    for review in soup.select('div.reviewInfoGrp'):
        buy = review.select_one("span.buy")
        result.append({
            "reviewdate": review.select_one("em.txt_date").text,
            "reviewerid": review.select_one("em.txt_id > a").text,
            "buy": buy.text.strip() if buy else '',
            "ratings": "내용 " + review.select_one("span.rating").text.strip() + "  편집/디자인 " + review.select_one("span.rating").text.strip(),
            "review": review.select_one("div.reviewInfoBot").text.replace('\n', '').strip(),
        })
        
    return result
   

def awordReviewList(info, order, csv):
    result = []

    sortorder = {
        "최근순": 1,
        "추천순": 2,
        "별점순": 3,
    }

    qrylist = [
        ("type", "ALL"),
        ("sort", sortorder[order]),
        ("PageNumber", 1)
    ]

    qrystr = parse.urlencode(qrylist)
    url = site + "/Product/communityModules/AwordReviewList/" + info["goodsid"] + '?' + qrystr

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    for review in soup.select('div.cmtInfoGrp'):
        buy = review.select_one("span.buy")
        result.append({
            "reviewdate": review.select_one("em.txt_date").text,
            "reviewerid": review.select_one("em.txt_id > a").text,
            "ratings": review.select_one("span.rating").text.strip(),
            "buy": buy.text.strip() if buy else '',
            "review": review.select_one("div.cmt_cont").text.strip(),
        })
        
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", default="최근순", choices=["최근순", "추천순", "별점순"])
    parser.add_argument("--csv", action=argparse.BooleanOptionalAction)
    parser.add_argument("goodsid_list", nargs='?', type=str)
    args = parser.parse_args()
    main(args.goodsid_list, args.order, args.csv)


