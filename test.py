import requests_html
from bs4 import BeautifulSoup
from time import sleep

url ='https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu'


def Get_URL():
    res = requests_html.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    profiles = soup.find_all('a', class_ = 'text-lg font-bold transition-all text-primary')
    all_profile_URL = []
    for profile in profiles:
        profile_ID = profile.get('href')
        profile_URL = 'https://topdev.vn/' + profile_ID
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL

URL_onepage = Get_URL()
for url in URL_onepage:
    res = requests_html.get(url)
    sleep(2)
    page_source = BeautifulSoup(res.text,'html.parser')
    info_div_pl3 = page_source.find_all('div',class_ = 'item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
    info_div_md4 = page_source.find_all('div',class_ = 'item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
    print('test = ',info_div_pl3)

# def GetProfileInfo(url):
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     # Find the experience year
#     info_div_md4 = soup.find_all('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full')
#     a_exp_year = info_div_md4[0].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
#     exp_year = a_exp_year[0].get_text(' ',strip=True)
#     # Find the level
#     info_div_pl3 = soup.find_all('div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0')
#     a_level = info_div_pl3[0].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
#     level = a_level[0].get_text(' ',strip=True)
#     # Find the workplace
#     a_work_place = info_div_md4[1].find_all('a', class_='text-sm hover:text-primary-300 hover:underline md:text-base')
#     work_place = a_work_place[0].get_text(' ',strip=True)
#     return {
#         'exp_year': exp_year,
#         'level': level,
#         'work_place': work_place
#     }
# URL_onepage = Get_URL()
# for url in URL_onepage:
#     profile_info = GetProfileInfo(url)

