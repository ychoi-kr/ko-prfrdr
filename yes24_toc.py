#!/usr/bin/python3

import argparse

import html2text

import yes24_bookinfo


def main(goodsid):
    toc = yes24_bookinfo.bookinfo(goodsid, showurl=None)["toc"]
    print(html2text.html2text(toc))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("goodsid", type=str)
    args = parser.parse_args()
    main(args.goodsid)
