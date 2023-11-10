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
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://topdev.vn/it-jobs?src=topdev.vn&medium=mainmenu')
sleep(2)
data_save_file_csv =[]
def Get_URL(): 
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    profiles = page_source.find_all('a',class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL
   
URL_onepage = Get_URL()
for url in URL_onepage:
    driver.get(url)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    info_div_pl3 = page_source.find_all('div',class_ = 'item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
    info_div_md4 = page_source.find_all('div',class_ = 'item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
    print('test = ',info_div_md4)