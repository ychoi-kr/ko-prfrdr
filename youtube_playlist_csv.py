#!/usr/bin/python

import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from youtube import youtube


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_id")
    args = parser.parse_args()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    for row in youtube.get_playlist_table(driver, args.playlist_id):
        dquo = "\""
        print(','.join(map(lambda x: dquo + x + dquo, row)))
