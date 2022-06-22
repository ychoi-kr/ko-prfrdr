import requests


def readurl(url):
    return requests.get(url).text

