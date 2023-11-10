from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import os
import csv

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.topcv.vn/tim-viec-lam-it?sort=top_related')
sleep(2)

def Get_URL():
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    a = page_source.find_all('h3',class_= 'title')
    all_profile_URL = []
    for profile in a:
        profile_URL = profile.get('href')
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL
URL_onepage = Get_URL()
print(URL_onepage[0])
#driver.get(URL_onepage[0])