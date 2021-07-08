#!/usr/bin/python

import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main(playlist_id):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    playlist_url = "https://www.youtube.com/playlist?list=" + playlist_id
    driver.get(playlist_url)
    links = driver.find_elements_by_css_selector("#video-title")
    
    for link in links:
        title = link.text
        video_url = link.get_attribute('href').split('&')[0]
        print(f"\"{title}\",\"{video_url}\"")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_id")
    args = parser.parse_args()
    main(args.playlist_id)
