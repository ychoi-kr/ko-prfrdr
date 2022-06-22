#!/usr/bin/python3

import re
import argparse

import html2text

import yes24_bookinfo


def main(goodsid, strip):

    # let users just copy & paste URL
    goodsid = goodsid.replace("http://www.yes24.com/Product/Goods/", '')

    bookinfo = yes24_bookinfo.bookinfo(goodsid, showurl=None)
    print("TITLE:" + bookinfo["title"] + '\n')

    print("Table of Contents:")
    toc = bookinfo["toc"]
    for line in html2text.html2text(toc).splitlines():
        if strip:
            line = line.strip().strip('**').strip('__')
        print(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("goodsid", type=str)
    parser.add_argument("--strip", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    main(args.goodsid, args.strip)
