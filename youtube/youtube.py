import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_playlist_table(driver, playlist_id):
    playlist_table = []

    playlist_url = "https://www.youtube.com/playlist?list=" + playlist_id
    driver.get(playlist_url)
    links = driver.find_elements_by_css_selector("#video-title")

    for link in links:
        title = link.text
        video_url = link.get_attribute('href').split('&')[0]
        playlist_table.append([title, video_url])

    return playlist_table


def get_transcript(driver, video_id):

    video_url = "https://youtube.com/watch?v=" + video_id
    driver.get(video_url)

    time.sleep(3)

    # https://stackoverflow.com/questions/51014205/automating-opening-transcript-for-youtube-automatic-generated-captions
    driver.find_elements_by_xpath("//button[@aria-label = '추가 작업']")[1].click()

    # https://github.com/ikitcheng/chinamatt_youtube/blob/main/2020-02-14-Youtube_Transcript/get_youtube_transcript.py
    driver.find_element_by_xpath("//*[@id='items']/ytd-menu-service-item-renderer/tp-yt-paper-item").click()

    time.sleep(3)
    transcript = driver.find_element_by_xpath("//*[@id='body']/ytd-transcript-body-renderer")

    return transcript.text
