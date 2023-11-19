import csv 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def get_profile_urls(driver, url):
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
        print(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []

def get_profile_info(driver, url):
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
        return [title, company_name, venue, date, exp_year, level, salary, edu, src_pic]
    except Exception as e:
        print(f"Error occurred while scraping data from {url}: {e}")
        return []

def write_to_csv(file_name, data):
    with open(os.path.join('data', file_name),'a+',encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['Title', 'Company Name', 'Venue', 'Date', 'Experience Year', 'Level', 'Salary', 'Education_Requirement', 'Source Picture'])
        for info in data:
            writer.writerow(info)

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://123job.vn/tuyen-dung?sort=top_related&q=Nh%C3%A2n+Vi%C3%AAn+IT&l='
    driver.get(url)
    sleep(2)
    profile_urls  = get_profile_urls(driver, url)
    data = []
    infos = []
    max_num_data = 35
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
    write_to_csv('123job.csv',data)
    driver.close()
if __name__ == '__main__':
    main()