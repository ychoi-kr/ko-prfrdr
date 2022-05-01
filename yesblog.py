#!/usr/bin/python3

import argparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse


def main(seqNo):
    url = "http://blog.yes24.com/document/" + seqNo
    
    with urlopen(url) as f:
        html = f.read()
    
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.select('.blogContArea')[0].text
        print(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("seqNo", type=str)
    args = parser.parse_args()
    main(args.seqNo)
