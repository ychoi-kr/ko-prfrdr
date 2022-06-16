import sys

import requests


def readurl(url):
    return requests.get(url).text


def print_csv_header():
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


def display(info, reviewlist, csv):
    for review in reviewlist:
        if csv:
            quote = lambda s: '"' + s.replace('"', '\'') + '"' if csv else s
            print(
                quote(info["title"]),
                quote(info["url"]),
                quote(info["author"]),
                quote(info["pubdate"]),
                quote(review["reviewdate"]),
                quote(review["reviewerid"]),
                quote(review["buy"]),
                quote(review["rating"]),
                quote(review["content"]),
                sep=','
            )
            sys.stdout.flush()
        else:
            print(
                review["reviewdate"] + ' ' + review["reviewerid"] + ' ' + review["buy"],
                review["rating"],
                review["content"],
                sep='\n',
                end='\n\n'
            )
