import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyclip as pyperclip
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:/chromedriver.exe")  # 크롬창 켜기
driver.get("http://naver.com") # 네이버 접속
xpath = '//a[@class="link_login"]'
xpath2 = '//input[@id="id"]'
xpath3 = '//input[@id="pw"]'
xpath4 = '//input[@id="log.login"]'
my_id="id"
my_pw="pw"
driver.find_element_by_xpath(xpath).click() # NAVER 로그인 클릭
driver.implicitly_wait(10)
pyperclip.copy(my_id) # id 복사
driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v') # id 붙여넣기
pyperclip.copy(my_pw) # 비밀번호 복사
driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v') # 비밀번호 붙여넣기
driver.find_element_by_xpath(xpath4).click() # 로그인 클릭
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[8]/a'))).click()
