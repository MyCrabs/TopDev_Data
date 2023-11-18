import csv 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def get_profile_urls(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    a = page_source.find_all('a',class_ = 'relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white border-se-blue-10')
    all_profile_urls = []
    for profile in a:
        profile_url = 'https://vieclam24h.vn' + profile.get('href')
        if profile_url not in all_profile_urls:
            all_profile_urls.append(profile_url)
    return all_profile_urls

def get_profile_info(driver, url):
    driver.get(url)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    company_name = page_source.find('h3', class_='font-normal text-16 text-se-neutral-64 mb-4').get_text(' ', strip=True)
    salary = page_source.find('p', class_='font-semibold text-14 text-[#8B5CF6]').get_text(' ', strip=True)
    div = page_source.find_all('div', class_='flex items-center mb-4 w-full md:w-[33%]')  # Co 3 div duoi
    div_exp_year = div[2]
    exp_year = div_exp_year.find('p').get_text(' ', strip=True)
    divv = page_source.find_all('div', class_='flex items-center mb-4 md:w-[33%]')  # Co 4 div tren
    div_level = divv[1]
    level = div_level.find('p', class_='text-14').get_text(' ', strip=True)
    div_edu = div[1]
    edu = div_edu.find('p', class_='text-14').get_text(' ', strip=True)
    return company_name, exp_year, level, salary, edu

def write_to_csv(file_name, data):
    with open(os.path.join('data', file_name),'a+',encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(['Company Name', 'Experience Years', 'Levels', 'Salary', 'Education_Requirement'])
        for info in data:
            writer.writerow(info)

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?q=nh%C3%A2n%20vi%C3%AAn%20it'
    driver.get(url)
    sleep(2)
    profile_urls  = get_profile_urls(driver, url)
    data = []
    max_num_data = 10
    for profile_url in profile_urls:
        company_names, exp_years, levels, salaries, edu = get_profile_info(driver, profile_url)
        print('>>> Name:', company_names,'>>>year:',exp_years)   #Dung de check khi co loi xay ra
        if len(data) >= max_num_data:
            break
        else:
            data.append((company_names, exp_years, levels, salaries, edu))
    write_to_csv('vieclam24.csv',data)
    driver.close()
if __name__ == '__main__':
    main()