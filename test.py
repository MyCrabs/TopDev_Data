from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get('https://vieclam24h.vn/cham-soc-khach-hang/nhan-vien-dich-vu-khach-hang-c30p73id200290054.html')
sleep(2)
page_source = BeautifulSoup(driver.page_source,'html.parser')
p = page_source.find('p', class_ = 'text-14 text-se-accent font-semibold').get_text(' ',strip=True)
print('>>', p)


# def GetURL(): 
#     page_source = BeautifulSoup(driver.page_source,'html.parser')
#     a = page_source.find_all('a', class_='relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white !bg-[#FFF5E7] border-[#FFC372] bg-white border-[1.5px]')
#     all_profile_urls = []
#     for profile in a:
#             profile_url = 'https://vieclam24h.vn' + profile.get('href')
#             if profile_url not in all_profile_urls:
#                 all_profile_urls.append(profile_url)
#     return all_profile_urls
#URL_onepage = GetURL()
# for url in URL_onepage:
#     driver.get(url)
#     sleep(2)
    # page_source = BeautifulSoup(driver.page_source, 'html.parser')
    # company_name = page_source.find('h3', class_='font-normal text-16 text-se-neutral-64 mb-4').get_text(' ', strip=True)
    # title = page_source.find('h1', class_='font-semibold text-18 md:text-24 leading-snug').get_text(' ', strip=True)
    # a = page_source.find('a', class_ ='hover:text-se-accent')
    # venue = a.find('span').get_text(' ',strip=True)
    # date_div = page_source.find_all('div', class_ ='ml-3 text-14 md:flex pt-0 md:pt-[5px]')
    # date_ = date_div[1].get_text(' ',strip=True)
    # part = date_.find(':')
    # date = date_[part + 2:]
    # salary = page_source.find('p', class_='font-semibold text-14 text-[#8B5CF6]').get_text(' ', strip=True)
    # div = page_source.find_all('div', class_='flex items-center mb-4 w-full md:w-[33%]')
    # div_exp_year = div[2]
    # exp_year = div_exp_year.find('p').get_text(' ', strip=True)
    # divv = page_source.find_all('div', class_='flex items-center mb-4 md:w-[33%]')
    # div_level = divv[1]
    # level = div_level.find('p', class_='text-14').get_text(' ', strip=True)
    # div_edu = div[1]
    # edu = div_edu.find('p', class_='text-14').get_text(' ', strip=True)
    # pic_div = page_source.find('div', class_ ='md:flex w-full items-start')
        # src_pic = pic_div.find('img').get('src')


