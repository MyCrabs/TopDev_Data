from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
url = 'https://vieclam24h.vn/cham-soc-khach-hang/tong-dai-vien-truc-hotline-vien-thong-viettel-tan-binh-c30p122id200289357.html'
driver.get(url)
sleep(2)
page_source = BeautifulSoup(driver.page_source,'html.parser')
div = page_source.find_all('div', class_ = 'jsx-d84db6a84feb175e md:flex md:border-b border-[#DDD6FE] mb-4')
age = div[2].find('div', class_ = 'flex items-center mb-4 md:w-[33%]').find('p', class_ = 'text-14').get_text(' ',strip = True)
print('>>>',len(div))





