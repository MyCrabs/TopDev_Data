from venv import logger 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import mysql.connector

def get_profile_urls_24(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        a = page_source.find_all('a', class_='relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white !bg-[#FFF5E7] border-se-blue-10')
        all_profile_urls = []
        for profile in a:
            profile_url = 'https://vieclam24h.vn' + profile.get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    
def get_profile_urls_123(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        div = page_source.find_all('div', class_ = 'job__list-item-content')
        all_profile_urls = []
        for profile in div:
            profile_url = profile.find('h2',class_ = 'job__list-item-title').find('a').get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    
def get_profile_info_24(driver, url):
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
        exp_year = div_exp_year.find('p', class_ = 'text-14').get_text(' ', strip=True)
        div_c1 = page_source.find_all('div', class_ = 'jsx-d84db6a84feb175e md:flex md:border-b border-[#DDD6FE] mb-4')
        divv = div_c1[0].find_all('div', class_='flex items-center mb-4 md:w-[33%]')
        if len(div_c1[0].find_all('div', class_ = 'flex items-center mb-4 md:w-[33%]'))== 2:
            div_level = divv[1]
            level = div_level.find('p', class_='text-14').get_text(' ', strip=True)
        elif len(div_c1[0].find_all('div', class_ = 'flex items-center mb-4 md:w-[33%]'))== 3:
            div_level = divv[2]
            level = div_level.find('p', class_='text-14').get_text(' ', strip=True)
        if len(div_c1[1].find_all('div', class_ = 'flex items-center mb-4 md:w-[33%]')) == 1:
            num_div = div_c1[1].find('div', class_ = 'flex items-center mb-4 md:w-[33%]')
            num_of_employee = num_div.find('p', class_ = 'text-14').get_text(' ', strip=True)
        elif len(div_c1[1].find_all('div', class_ = 'flex items-center mb-4 md:w-[33%]')) == 2:
            num_div = div_c1[1].find_all('div', class_ = 'flex items-center mb-4 md:w-[33%]')
            num_of_employee = num_div[1].find('p', class_ = 'text-14').get_text(' ', strip=True)
        div_edu = div[1]
        edu = div_edu.find('p', class_='text-14').get_text(' ', strip=True)
        pic_div = page_source.find('div', class_ ='md:flex w-full items-start')
        src_pic = pic_div.find('img').get('src')
        last_div = page_source.find_all('div', class_ ='text-14 text-se-grey-48 font-semibold')
        head_quater = last_div[0].get_text(' ',strip=True)
        describe_div = page_source.find_all('div', class_ = 'jsx-d84db6a84feb175e mb-2 text-14 break-words text-se-neutral-80 text-description')
        description = describe_div[0].get_text(' ',strip=True)
        requirement = describe_div[1].get_text(' ',strip=True)
        job = page_source.find('p', class_ = 'text-14 text-se-accent font-semibold').get_text(' ',strip=True)    
        return [title, company_name, job, head_quater, num_of_employee, exp_year, level, salary, edu, description, requirement, date, src_pic]
    except Exception as e:
        logger.error(f"Error occurred while scraping data from {url}: {e}")
        return []

def get_profile_info_123(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        div_pic = page_source.find('div',class_ ='logo-item')
        src_pic = div_pic.find('img').get('src')
        company_name = page_source.find('div', class_='col-md-9 content-group box-apply-top js-item-job').find('p').get_text(' ', strip=True)
        title = page_source.find('div', class_='col-md-9 content-group box-apply-top js-item-job').find('h1').get_text(' ', strip=True)
        div_salary = page_source.find('div', class_='item salary').find_all('b')
        salary = div_salary[1].get_text(' ', strip=True)
        eight_div = page_source.find_all('div', class_='item text-black')
        venue = eight_div[0].get_text(' ', strip=True)
        part_venue = venue.split(":")
        venue = part_venue[1].lstrip()
        exp_year = eight_div[2].get_text(' ', strip=True)
        part = exp_year.split(':')
        exp_year = part[1].lstrip()
        edu = eight_div[4].get_text(' ', strip=True)
        part_edu = edu.split(':')
        edu = part_edu[1].lstrip()
        div = page_source.find_all('div', class_='item time-expiry-date')
        level = div[1].get_text(' ', strip=True)
        part_level = level.split(':')
        level = part_level[1].lstrip()
        date = div[0].get_text(' ', strip=True)
        part_date = date.find(':')
        date = date[part_date + 2:]
        description_div = page_source.find_all('div',class_ ='content-group__content')
        description = description_div[0].find('p').get_text(' ', strip=True)
        requirement = description_div[1].find('p').get_text(' ', strip=True)
        div_more = page_source.find('div', class_ ='mt-2 company-entity')
        span = div_more.find_all('span',class_='block-mobile')
        num_of_employee = span[0].get_text(' ',strip=True)
        head_quater = span[1].get_text(' ',strip=True)
        return [title, company_name, head_quater, date, exp_year, level, salary, edu, description, requirement, num_of_employee, src_pic]
    except Exception as e:
        print(f"Error occurred while scraping data from {url}: {e}")
        return []
    
def is_duplicated(info, data):
    for i in data:
        if i[1] == info[0] and i[2] == info[1]:
            return True
    return False

def get_data_from_DB():
    try:
        connection = mysql.connector.connect(user='root', password='123456', host='localhost')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM crawl_data.job_data")
        data = cursor.fetchall()
        connection.close()
        return data
    except Exception as e:
        print(f"Error occurred while retrieving data from database: {e}")
        return []

def get_vieclam24(driver, max_num):
    try:
        url ='https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?page=2&sort_q='
        print('>>> URL: ',url)
        driver.get(url)
        sleep(2)
        profile_urls = get_profile_urls_24(driver, url)
        data_DB = get_data_from_DB()
        data =[]
        for i in profile_urls:
            info = get_profile_info_24(driver, i)
            print('>> Vieclam24:',info)
            if info == []:
                pass
            else:
                if len(data) >= max_num:
                    break
                else:
                    if not is_duplicated(info , data_DB):
                        data.append(info)
        return data
    except Exception as e:
        print(f"Error occurred while get data 24h: {e}")
        return []

def get_123job(driver, max_num):
    url = 'https://123job.vn/tuyen-dung?s=0&sort=up_top&q=&l='
    driver.get(url)
    sleep(2)
    profile_urls = get_profile_urls_123(driver, url)
    data_DB = get_data_from_DB()
    data =[]
    for i in profile_urls:
        info = get_profile_info_123(driver, i)
        print('>> 123Job:',info)
        if info == []:
            pass
        else:
            if len(data) >= max_num: 
                break
            else:
                if not is_duplicated(info, data_DB):
                    data.append(info)
    print('>>>',data)
    return data

