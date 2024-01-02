from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
url = 'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=8&page=1&sort_q=actived_at_by_box%2Cdesc'
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)