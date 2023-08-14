import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import pandas as pd
from getpass import getpass
# from bs4 import BeautifulSoup


option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--incognito')  # membuka web driver dalam mode incognito
option.add_experimental_option('excludeSwitches', ['enable-logging'])
# option.add_argument('--headless') #tanpa membuka window web driver

# user ig yang akan di tarik datanya
user = 'jeromepolin'

# information for login
username = "lilybeautypure.official"
password = "lilybeauty1999"

ig = 'https://www.instagram.com/'
driver = webdriver.Chrome(options=option)
driver.get(f'{ig}accounts/login/')
driver.implicitly_wait(5)

u_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
u_input.send_keys(username)
p_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
p_input.send_keys(password)

b_login = driver.find_element(By.CSS_SELECTOR, '._acap')
b_login.click()

time.sleep(3)
b_login = driver.find_element(By.CSS_SELECTOR, '._ac8f')
b_login.click()
time.sleep(3)

driver.get(f'{ig}{user}')
time.sleep(3)

# jika ingin scrape data sebanyak jumlah postingannya
# num_posts = (driver.find_element(By.CSS_SELECTOR, '.k9GMp .g47SY')).text
# num_posts = num_posts.replace(",", "")
# num_posts = int(num_posts)

posts = driver.find_elements(By.CSS_SELECTOR, '._aa8k')
coll_posts = []
temp = ''
x = 0
y = 21

##
pop_up = posts[0].find_element(By.CSS_SELECTOR, '._aagw')
pop_up.click()
time.sleep(4)
# num_posts dpt diganti n angka, jika hanya ingin mengambil data n postingan
for x in range(20):

    x += 1
    print(x)
    dict_posts = {'link_post': (driver.find_element(
        By.CSS_SELECTOR, '._aaqb a')).get_attribute('href')}
    dict_posts['no'] = x
    dict_posts['datetime_post'] = (driver.find_element(
        By.CSS_SELECTOR, '._aaqb a time')).get_attribute('datetime')
    dict_posts['account_instagram_artist'] = (driver.find_element(
        By.CSS_SELECTOR, '._aa_y h2')).text

    dict_posts['img_link'] = (driver.find_element(
        By.CSS_SELECTOR, '._aagv img')).get_attribute('src')
    dict_posts['caption_postingan'] = (
        driver.find_element(By.CSS_SELECTOR, '._a9zs h1')).text

    comments = driver.find_elements(By.CSS_SELECTOR, '._a9ym')
    coll_comments = []
    time.sleep(6)
    for line_comment in comments:
        comment = line_comment.find_elements(By.CSS_SELECTOR, '._a9zr')
        single_comment = {'author': comment[0].find_element(
            By.CSS_SELECTOR, '.xw3qccf a').text}
        single_comment['comment'] = comment[0].find_element(
            By.CSS_SELECTOR, '._a9zs span').text
        coll_comments.append(single_comment)
    time.sleep(4)
    dict_posts['comments'] = coll_comments
    # dict_posts['comments'] = captions
    coll_posts.append(dict_posts)
    if x != 21:
        next_but = driver.find_element(By.CSS_SELECTOR, '._aaqg span')
        next_but.click()
        time.sleep(4)

with open('output.json', 'w', encoding='utf8') as output:
    json.dump(coll_posts, output,  ensure_ascii=False, indent=4)


driver.close()
driver.quit()
# df = pd.read_json(r'D:\Scraping\output.json')
# df.to_csv(r'D:\Scraping\syifahadju.csv', index=None)
# df = pd.DataFrame()
# df = pd.json_normalize(data, record_path='')
# data = r'D:\Scraping\output.json'
# df2 = pd.json_normalize(data, record_path='comments', meta=[
#    'link', 'no', 'date', 'akun_artis'])
# df2.to_csv(r'D:\Scraping\syifahadju1.csv', index=None)
# time.sleep(4)
