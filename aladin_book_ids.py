#!/usr/bin/python3

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import re


site = "https://www.aladin.co.kr"


def main(publisher, page):

    qrylist = [
        ("SearchTarget", "Book"),
        ("KeyPublisher", publisher),
        ("KeyMonthStart", "01"),
        ("KeyMonthEnd", "01"),
        ("KeyRecentPublish", "0"),
        ("OutStock", "0"),
        ("ViewType", "Detail"),
        ("SortOrder", "5"),
        ("CustReviewCount", "0"),
        ("CustReviewRank", "0"),
        ("SearchFieldEnable", "1"),
        ("KeyWord", ""),
        ("CategorySearch", ""),
        ("DetailSearch", "1"),
        ("chkKeyTitle", ""),
        ("chkKeyAuthor", ""),
        ("chkKeyPublisher", "on"),
        ("chkKeyISBN", ""),
        ("chkKeyTag", ""),
        ("chkKeyTOC", ""),
        ("chkKeySubject", ""),
        ("ViewRowCount", "50"),
        ("page", page)
    ]

    qrystr = parse.urlencode(qrylist)
    url = site + "/search/wsearchresult.aspx?" + qrystr

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    for x in soup.find_all("a", "bo3"):
        print(x.attrs["href"].split('=')[1])
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--publisher", default="위키북스", type=str)
    parser.add_argument("--page", default=1, type=int)
    args = parser.parse_args()
    main(args.publisher, args.page)


