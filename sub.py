from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import os
import csv  # Em Trình install beautifulsoup4 với selenium bằng cmd nghe
import pandas as pd

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://vieclam24h.vn/it-phan-mem/it-executive-software-tai-bac-ninh-c8p90id200283176.html')
sleep(2)

page_source = BeautifulSoup(driver.page_source, 'html.parser')
pic_div = page_source.find('div', class_ ='md:flex w-full items-start')
src_pic = pic_div.find('img').get('src')
print ('>>>a:',src_pic)

# def GetURL():
#     page_source = BeautifulSoup(driver.page_source, 'html.parser')
#     profiles = page_source.find_all(
#         'a', class_='text-lg font-bold transition-all text-primary')
#     all_profile_URL = []
#     for profile in profiles:
#         profile_ID = profile.get('href')
#         profile_URL = 'https://topdev.vn/' + profile_ID
#         if profile_URL not in all_profile_URL:
#             all_profile_URL.append(profile_URL)
#     return all_profile_URL


# def is_duplicate(new_info, file_name):
#     with open(os.path.join("data", file_name), 'r', encoding='UTF-8', newline='') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if new_info == row:
#                 return True
#     return False

