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
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    for row in youtube.get_playlist_table(driver, args.playlist_id):
        dquo = "\""
        title = f'{row[0]}({row[1]})'
        print(title)
        print('-' * len(title))
        video_id = row[1].split('=')[1]
        print(youtube.get_transcript(driver, video_id))
        print()
