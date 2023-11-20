import csv 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import mysql.connector

def get_profile_urls(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        a = page_source.find_all('a', class_='relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white border-se-blue-10')
        all_profile_urls = []
        for profile in a:
            profile_url = 'https://vieclam24h.vn' + profile.get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        print(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    
def get_profile_info(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        company_name = page_source.find('h3', class_='font-normal text-16 text-se-neutral-64 mb-4').get_text(' ', strip=True)
        title = page_source.find('h1', class_='font-semibold text-18 md:text-24 leading-snug').get_text(' ', strip=True)
        a = page_source.find('a', class_ ='hover:text-se-accent')
        venue = a.find('span').get_text(' ',strip=True)
        date_div = page_source.find_all('div', class_ ='ml-3 text-14 md:flex pt-0 md:pt-[5px]')
        date_ = date_div[1].get_text(' ',strip=True)
        part = date_.find(':')
        date = date_[part + 2:]
        salary = page_source.find('p', class_='font-semibold text-14 text-[#8B5CF6]').get_text(' ', strip=True)
        div = page_source.find_all('div', class_='flex items-center mb-4 w-full md:w-[33%]')
        div_exp_year = div[2]
        exp_year = div_exp_year.find('p').get_text(' ', strip=True)
        divv = page_source.find_all('div', class_='flex items-center mb-4 md:w-[33%]')
        div_level = divv[1]
        level = div_level.find('p', class_='text-14').get_text(' ', strip=True)
        div_edu = div[1]
        edu = div_edu.find('p', class_='text-14').get_text(' ', strip=True)
        pic_div = page_source.find('div', class_ ='md:flex w-full items-start')
        src_pic = pic_div.find('img').get('src')
        return [title, company_name, venue, date, exp_year, level, salary, edu, src_pic]
    except Exception as e:
        print(f"Error occurred while scraping data from {url}: {e}")
        return [] 

def save_data_into_database(data):
    connection = mysql.connector.connect(user='root', password='123456', host='localhost')
    cursor = connection.cursor()
    query = "INSERT INTO `test`.`test_table3` (`title`, `company_name`, `venue`, `date`, `exp_year`, `level`, `salary`, `edu`, `src_pic`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for i in data:
        cursor.execute(query, i)
    connection.commit()
    connection.close()          

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?q=nh%C3%A2n%20vi%C3%AAn%20it'
    driver.get(url)
    sleep(2)
    profile_urls  = get_profile_urls(driver, url)
    data = []
    infos = []
    max_num_data = 30
    for profile_url in profile_urls:
        info = get_profile_info(driver, profile_url)
        print('>>> Info:', info)
        if info == []:
            pass
        else: 
            if len(data) >= max_num_data:
                break
            else:
                data.append(info)
    save_data_into_database(data)            
    driver.close()
if __name__ == '__main__':
    main()