import csv 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def get_profile_urls(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    profiles = page_source.find_all('a', class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_urls = []
    for profile in profiles:
        profile_id = profile.get('href')
        profile_url = 'https://topdev.vn/' + profile_id
        if profile_url not in all_profile_urls:
            all_profile_urls.append(profile_url)
    return all_profile_urls

def get_profile_info(driver, url):
    driver.get(url)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    info_div_pl3 = page_source.find_all('div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
    info_div_md4 = page_source.find_all('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
    a_exp_year = info_div_md4[0].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
    a_level = info_div_pl3[0].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
    a_work_place = info_div_md4[1].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')

    company_names = page_source.find('p', class_='my-1 text-base font-bold text-gray-500').get_text(' ', strip=True)
    exp_years = a_exp_year[0].get_text(' ', strip=True)
    levels = a_level[0].get_text(' ', strip=True)
    work_places = a_work_place[0].get_text(' ', strip=True)
    return company_names, exp_years, levels, work_places

def write_to_csv(file_name, data):
    with open(os.path.join('data', file_name),'a+',encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['Company Name', 'Experience Years', 'Levels', 'Work Places'])
        for info in data:
            writer.writerow(info)

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu'
    driver.get(url)
    sleep(2)
    profile_urls  = get_profile_urls(driver, url)
    data = []
    for profile_url in profile_urls:
        company_names, exp_years, levels, work_places = get_profile_info(driver, profile_url)
        data.append((company_names, exp_years, levels, work_places))
    write_to_csv('topdev_dataa.csv',data)
    driver.close()
if __name__ == '__main__':
    main()