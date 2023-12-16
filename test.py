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
url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?page='+'3'+'&sort_q='
driver.get(url)
sleep(2)
page_source = BeautifulSoup(driver.page_source,'html.parser')





