from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import os
import csv   #Em Trình install beautifulsoup4 với selenium bằng cmd nghe
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu')
sleep(2)
data_save_file_csv =[]
def GetURL(): #Hàm dùng để lặp đi lăp lại nếu muốn search nhiều trang web
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    profiles = page_source.find_all('a',class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL

URL_onepage = GetURL()
for url in URL_onepage:
    driver.get(url)
    sleep(2)