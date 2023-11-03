from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu')
sleep(2)

def GetURL(): #Hàm dùng để lặp đi lăp lại nếu muốn search nhiều trang web
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    profiles = page_source.find_all('a',class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL
    
URL_onepage = GetURL()
for url in URL_onepage:
    driver.get(url)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source,'html.parser')
    info = page_source.find_all('a',class_ = 'text-sm hover:text-primary-300 hover:underline md:text-base')
    info_b = page_source.find_all('span',class_ = 'whitespace-nowrap rounded border border-solid font-normal transition-all inline-flex items-center justify-center border-blue-light text-blue-dark bg-blue-light hover:border-blue-dark h-[1.625rem] px-2 text-xs md:h-7 md:px-2 md:text-sm')
    company_name = page_source.find('p',class_ = 'my-1 text-base font-bold text-gray-500').get_text(' ',strip=True)
    exp_year = info[0].get_text(' ',strip=True)
    level = info[1].get_text(' ',strip=True)
    work_place = info[2].get_text(' ',strip=True)
    print(company_name,';',exp_year,';',level,';',work_place)

