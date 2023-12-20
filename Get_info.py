from venv import logger 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from DB import get_data_from_DB
from get_24 import get_company_name_24, get_title_24, get_job_24, get_headquater_24, get_NumEmployee_24, get_Exp_24, get_level_24, get_Salary_24,get_Edu_24, get_Requirement_24, get_Description_24, get_Date_24, get_SrcPic_24

def get_profile_urls_24(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        class_name = 'relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white !bg-[#FFF5E7] border-se-blue-10'
        a = page_source.find_all('a', class_=class_name)
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
        company_name = get_company_name_24(page_source)
        title = get_title_24(page_source)
        date = get_Date_24(page_source)
        salary = get_Salary_24(page_source)
        exp_year = get_Exp_24(page_source)
        level = get_level_24(page_source)
        num_of_employee = get_NumEmployee_24(page_source)
        edu = get_Edu_24(page_source)
        src_pic = get_SrcPic_24(page_source)
        head_quater = get_headquater_24(page_source)
        description = get_Description_24(page_source)
        requirement = get_Requirement_24(page_source)
        job = get_job_24(page_source)   
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
        if i[1] == info[0] and i[2] == info[1] and i[3] == info[2]:
            return True
    return False

def get_vieclam24(driver, max_num):
    try:
        num_page = 14
        data =[]
        while len(data) < max_num:
            url = f'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?page={num_page}&sort_q='
            print('>>> URL: ',url)
            driver.get(url)
            sleep(2)
            profile_urls = get_profile_urls_24(driver, url)
            data_DB = get_data_from_DB()     
            for i in profile_urls:
                info = get_profile_info_24(driver, i)
                print('>> Vieclam24:',info)
                if info == []:
                    pass
                else:
                    if not is_duplicated(info , data_DB):
                        data.append(info)
            num_page += 1
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

