import concurrent.futures
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Get_info import get_123job,get_vieclam24
from DB import save_data_into_DB
        
def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:
            pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
            max_num = 5
            future = pool.submit(get_vieclam24, driver, max_num)
            data = future.result()
            # future = pool.submit(get_vieclam24, driver, max_num)
            #data.extend(future.result())
            pool.shutdown(wait=True)
            save_data_into_DB(data)
    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')
    
if __name__ == '__main__':
    main()
