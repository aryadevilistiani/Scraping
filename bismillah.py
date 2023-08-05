import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
from getpass import getpass
# from bs4 import BeautifulSoup


option = webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--incognito')  # membuka web driver dalam mode incognito
option.add_experimental_option('excludeSwitches', ['enable-logging'])
# option.add_argument('--headless') #tanpa membuka window web driver

# user ig yang akan di tarik datanya
user = 'syifahadju'

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
time.sleep(3)
# num_posts dpt diganti n angka, jika hanya ingin mengambil data n postingan
for x in range(2):

    x += 1
    print(x)

    dict_posts = {'link': (driver.find_element(
        By.CSS_SELECTOR, '._aaqb a')).get_attribute('href')}
    dict_posts['no'] = x
    dict_posts['date'] = (driver.find_element(
        By.CSS_SELECTOR, '._aaqb a time')).get_attribute('title')

    # dict_posts['img_link'] = (driver.find_element(By.CSS_SELECTOR, '._2dDPU .KL4Bh')).get_attribute('src')

    comments = driver.find_elements(By.CSS_SELECTOR, '._a9z6')
    coll_comments = []
    user_names = []
    user_comments = []
    time.sleep(3)
    for line_comment in comments:
        comment = line_comment.find_elements(By.CSS_SELECTOR, '._a9zr')
        # name_author = comment.find_element(By.CSS_SELECTOR, '.xw3qccf a')
        # captions = {'author': name_author[0].text}
        # name_author.append(captions)
        single_comment = {'author': comment[0].find_element(
            By.CSS_SELECTOR, '.xw3qccf a').text}
        single_comment['comment'] = comment[1].find_element(
            By.CLASS_NAME, '_a9zs').text
        coll_comments.append(single_comment)
        # container = com.find_element(By.CLASS_NAME, '_a9zr')
        # name = comments.find_element(By.CSS_SELECTOR, '._a9zc a').text
        # content = comments.find_element(By.CLASS_NAME, '_a9zs').text
        # user_names.append(name)
        # user_comments.append(content)

    dict_posts['comments'] = coll_comments
    # dict_posts['comments'] = captions
    coll_posts.append(dict_posts)
    if x != 2:
        next_but = driver.find_element(By.CSS_SELECTOR, '._aaqg span')
        next_but.click()
        time.sleep(4)

with open('output.json', 'w', encoding='utf8') as output:
    json.dump(coll_posts, output,  ensure_ascii=False, indent=4)


driver.close()
driver.quit()
