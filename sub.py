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
driver.get('https://topdev.vn/viec-lam-it/c-sharp-kt24')
sleep(2)


def GetURL():
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    profiles = page_source.find_all(
        'a', class_='text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL


def is_duplicate(new_info, file_name):
    with open(os.path.join("data", file_name), 'r', encoding='UTF-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if new_info == row:
                return True
    return False


URL_onepage = GetURL()
data_save_file_csv = set()
for url in URL_onepage:
    driver.get(url)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    info_div_pl3 = page_source.find_all(
        'div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
    info_div_md4 = page_source.find_all(
        'div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
    a_exp_year = info_div_md4[0].find_all(
        'a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
    a_level = info_div_pl3[0].find_all(
        'a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
    a_work_place = info_div_md4[1].find_all(
        'a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
    # info_b = page_source.find_all('span',class_ = 'whitespace-nowrap rounded border border-solid font-normal transition-all inline-flex items-center justify-center border-blue-light text-blue-dark bg-blue-light hover:border-blue-dark h-[1.625rem] px-2 text-xs md:h-7 md:px-2 md:text-sm')
    company_names = page_source.find(
        'p', class_='my-1 text-base font-bold text-gray-500').get_text(' ', strip=True)
    exp_years = a_exp_year[0].get_text(' ', strip=True)
    levels = a_level[0].get_text(' ', strip=True)
    work_places = a_work_place[0].get_text(' ', strip=True)
    new_info = [company_names, exp_years, levels, work_places]
    new_info = tuple(new_info)
    # data_save_file_csv.add(new_info)
    # if new_info not in data_save_file_csv:
    #     data_save_file_csv.append(new_info)

# Em trình tạo 1 folder tên 'data' để lưu file csv vô nghe
file_name = 'topdev_dataa.csv'
# with open(os.path.join("data",file_name),'a+',encoding='UTF-8',newline='') as f:
#     writer = csv.writer(f)
#     if f.tell() == 0:
#         writer.writerow(['Company Name', 'Experience Years', 'Levels', 'Work Places'])
#     for info in data_save_file_csv:
#         writer.writerow(info)
if not is_duplicate(new_info, file_name):
    with open(os.path.join("data", file_name), 'a+', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(
                ['Company Name', 'Experience Years', 'Levels', 'Work Places'])
            writer.writerow(new_info)
sleep(2)
print('Successfully')
