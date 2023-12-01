from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://123job.vn/tuyen-dung?sort=up_top&q=IT+ph%E1%BA%A7n+m%E1%BB%81m&l=')
driver.maximize_window()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
driver.close()