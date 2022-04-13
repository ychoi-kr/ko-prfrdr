from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse


def main(keyword, order, category):
    site = "http://www.yes24.com"

    basefilter = {"인기도순": "SINDEX_ONLY",
                  "정확도순": "RELATION",
                  "신상품순": "RECENT",
                  "최저가순": "LOW_PRICE",
                  "최고가순": "HIGH_PRICE",
                  "평점순": "CONT_NT",
                  "리뷰순": "REVIEW_CNT"}

    qry = parse.urlencode([
        ("domain", "BOOK"),
        ("query", ' '.join(keyword)),
        ("order", basefilter[order]),
        ("dispno2", category)
    ])

    url = site + "/Product/Search?" + qry
    
    print("Opening", url, "...\n")

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    yesSchList = soup.select('#yesSchList > li')

    result = []
    for item in yesSchList:
        if item.select_one("span.gd_res").text == "[eBook]":
            continue

        saleNum = item.select_one("span.saleNum").text.strip() if item.select_one("span.saleNum") else None
        if not saleNum:
            continue
        
        title = dict()
        title["gd_name"] = item.select_one("div.info_row.info_name > a").text
        title["url"] = site + item.select_one("div.info_row.info_name > a")['href']
        title["author"] = item.select_one("span.authPub.info_auth").text.split('\n')[1].strip()
        title["publisher"] = item.select_one("span.authPub.info_pub > a").text
        title["pubdate"] = item.select_one("span.authPub.info_date").text
        title["saleNum"] = saleNum
        
        result.append(title)

    for title in sorted(result,
                        key=lambda d: int(d["saleNum"].split(' ')[1].replace(',', '')),
                        reverse=True
                        ):
        print(title["gd_name"])
        print(title["url"])
        print(title["author"], '|', title["publisher"], '|', title["pubdate"])
        print(title["saleNum"])
        print('')
   
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", default="인기도순", choices=["인기도순", "정확도순", "신상품순", "최저가순", "최고가순", "평점순", "리뷰순"])
    parser.add_argument("--category", default="001001003", type=str)
    parser.add_argument("keyword", nargs="+", type=str)
    args = parser.parse_args()
    main(args.keyword, args.order, args.category)


