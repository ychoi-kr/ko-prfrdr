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
