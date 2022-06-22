#!/usr/bin/python3

from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse
import re


site = "http://www.yes24.com"

domainmap = {
    "전체": "ALL",
    "국내도서": "BOOK",
    "ebook": "EBOOK",
    "중고샵": "USED_GOODS",
}

basefilter = {
    "인기도순": "SINDEX_ONLY",
    "정확도순": "RELATION",
    "신상품순": "RECENT",
    "최저가순": "LOW_PRICE",
    "최고가순": "HIGH_PRICE",
    "평점순": "CONT_NT",
    "리뷰순": "REVIEW_CNT"
}

categorymap = {
    "art": "001001007",
    "biz": "001001025",
    "elementary": "001001044",
    "exam": "001001015",
    "humanity": "001001019",
    "it": "001001003",
    "kid": "001001016",
    "kids": "001001016",
    "literature": "001001046",
    "middle": "001001013",
    "sci": "001001002",
    "self": "001001026",
    "teen": "001001005",
    "test": "001001015",
    "univ": "001001014",
    "경영": "001001025",
    "경제": "001001025",
    "과학": "001001002",
    "대학교재": "001001014",
    "문학": "001001046",
    "수험서": "001001015",
    "어린이": "001001016",
    "예술": "001001007",
    "인문": "001001019",
    "자격증": "001001015",
    "자기개발": "001001026",
    "자기계발": "001001026",
    "자연과학": "001001002",
    "중고등": "001001013",
    "중고등참고서": "001001013",
    "청소년": "001001005",
    "초등": "001001044",
    "초등참고서": "001001044",
}

mkEntrNo = {
    "위키북스": "120040",
    "위키북스(eBook)": "284569"
}

def main(keyword, domain, order, category, publisher, page, showurl, csv, id_only):


    display(search(keyword, domain, order, category, publisher, page, showurl), order, csv, id_only)


def display(booklist, order, csv, id_only):
    if csv:
        print(
            '"URL"',
            '"제목"',
            '"부제"',
            '"저자/역자"',
            '"출판사"',
            '"발행일"',
            '"판매지수"',
            sep=','
        )

    booklist = sorted(booklist, key=lambda x: int(x["saleNum"].replace(',', '')), reverse=True) if order == "판매지수순" else booklist

    for book in booklist:
        if id_only:
            print(re.search(r"(\d+)$", book["url"]).group())
        elif csv:
            quote = lambda s: '"' + s.replace('"', '\"') + '"' if csv else s
            print(
                quote(book["url"]),
                quote(book["gd_res"] + ' ' + book["title"]),
                quote(book["subtitle"]),
                quote(book["author"]),
                quote(book["publisher"]),
                quote(book["pubdate"]),
                quote(book["saleNum"]),
                sep=','
            )
        else:
            print(
                book["url"],
                book["gd_res"] + ' ' + (": ".join([book["title"], book["subtitle"]]) if book["subtitle"] else book["title"]),
                book["author"] + '|' + book["publisher"] + '|' + book["pubdate"],
                "판매지수 " + book["saleNum"],
                sep='\n',
                end='\n\n'
            )


def search(keyword, domain, order, category, publisher, page, showurl):
    result = []

    inckey = [k for k in keyword.split() if not k.startswith('-')]
    exckey = [k[1:] for k in keyword.split() if k.startswith('-')]

    qrylist = [
        ("domain", domainmap[domain.lower()]),
        ("query", ' '.join(inckey)),
        ("page", page),
    ]

    if order in ["인기도순", "정확도순", "신상품순", "최저가순", "평점순", "리뷰순"]:
        qrylist.append(("order", basefilter[order]))
    elif order == "판매지수순":
        pass  # implemented by sorting because it's not provided by Yes24

    if category and category.lower() != "all":
        if category.startswith('0'):
            qrylist.append(("dispno2", category))
        else:
            qrylist.append(("dispno2", categorymap[category.lower()]))

    if publisher:
        qrylist.append((
            "mkEntrNo",
            ','.join(map(lambda x: mkEntrNo[x], publisher.split(',')))
        ))

    qrystr = parse.urlencode(qrylist)
    url = site + "/Product/Search?" + qrystr

    if showurl:
        print("Opening", url, "...\n")

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    yesSchList = soup.select('#yesSchList > li')

    for item in yesSchList:
        saleNum = item.select_one("span.saleNum").text.replace("판매지수", '').strip() if item.select_one("span.saleNum") else None
        
        title = dict()
        title["gd_res"] = item.select_one("span.gd_res").text
        title["title"] = item.select_one("div.info_row.info_name > a.gd_name").text.strip()
        title["subtitle"] = item.select_one("span.gd_nameE").text if item.select_one("span.gd_nameE") else ''
        title["url"] = site + item.select_one("div.info_row.info_name > a")['href']
        title["author"] = item.select_one("span.authPub.info_auth").text.split('\n')[1].strip()
        title["publisher"] = item.select_one("span.authPub.info_pub > a").text
        title["pubdate"] = item.select_one("span.authPub.info_date").text
        title["saleNum"] = saleNum if saleNum else ''
        
        skip = False
        for k in exckey:
            if any(map(lambda x: k in x, title.values())):
                skip = True

        if order == "판매지수순" and title["saleNum"] == '':
            skip = True

        if not skip:
            result.append(title)
    return result
   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", default="국내도서", choices=["전체", "국내도서", "외국도서", "eBook", "중고샵"])
    parser.add_argument("--order", default="인기도순", choices=["인기도순", "정확도순", "신상품순", "최저가순", "최고가순", "평점순", "리뷰순", "판매지수순"])
    parser.add_argument("--category", default="001001003", type=str)
    parser.add_argument("--publisher", type=str)
    parser.add_argument("--page", default=1, type=int)
    parser.add_argument("--showurl", action=argparse.BooleanOptionalAction)
    parser.add_argument("--csv", action=argparse.BooleanOptionalAction)
    parser.add_argument("--id_only", action=argparse.BooleanOptionalAction)
    parser.add_argument("keyword", nargs='?', type=str)
    args = parser.parse_args()
    main(args.keyword, args.domain, args.order, args.category, args.publisher, args.page, args.showurl, args.csv, args.id_only)


