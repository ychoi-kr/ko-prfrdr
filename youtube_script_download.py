#!/usr/bin/python

import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from youtube import youtube

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video_id")
    args = parser.parse_args()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    print(youtube.get_transcript(driver, args.video_id))
