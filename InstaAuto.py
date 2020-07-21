from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
from getpass import getpass

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.instagram.com/'

driver.get(url)

usr = input('Enter user-name\n')
user_name = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
user_name.send_keys(usr)


print('Enter Password')
pas = getpass()
password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys(pas)

log_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
log_in.click()

name = input('Enter whose profile you want to visit\n')
search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys(name)
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)

time.sleep(10)

first_pic = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
first_pic.click()

time.sleep(3)
like_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like_button.click()

time.sleep(1)
first_next = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
first_next.click()

while True:
    try:
        time.sleep(3)
        like_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like_button.click()

        time.sleep(1)
        all_next = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        all_next.click()

    except NoSuchElementException as e:
        close = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button/div/svg/path')
        close.click()
        break
