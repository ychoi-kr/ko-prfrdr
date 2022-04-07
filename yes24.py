from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse


def main(keyword):
    site = "http://www.yes24.com"
    #qry = "domain=BOOK&query=" + "%20%".join(keyword)
    qry = parse.urlencode([("domain", "BOOK"), ("query", ' '.join(keyword))])
    url = site + "/Product/Search?" + qry
    
    print("Opening", url, "...\n")

    with urlopen(url) as f:
        html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    yesSchList = soup.select('#yesSchList > li')
    for item in yesSchList:
        if item.select_one("span.gd_res").text == "[eBook]":
            continue

        saleNum = item.select_one("span.saleNum").text.strip() if item.select_one("span.saleNum") else None
        if not saleNum:
            continue
        
        gd_name = item.select_one("div.info_row.info_name > a").text
        url = site + item.select_one("div.info_row.info_name > a")['href']
        
        #author = [x.text for x in item.select("span.authPub.info_auth > a")]
        author = item.select_one("span.authPub.info_auth").text.split('\n')[1].strip()
        publisher = item.select_one("span.authPub.info_pub > a").text
        pubdate = item.select_one("span.authPub.info_date").text
        
        print(gd_name)
        print(url)
        print(author, '|', publisher, '|', pubdate)
        print(saleNum)
        print('')
   
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", nargs="+", type=str)
    args = parser.parse_args()
    main(args.keyword)
    



