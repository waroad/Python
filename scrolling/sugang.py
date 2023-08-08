import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyclip as pyperclip
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome("C:/chromedriver.exe")  # 크롬창 켜기
driver.get("https://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action") # 사이트 접속
p = driver.current_window_handle
f = open("id.txt", "r")
xpath = '//*[@id="stdno"]'
xpath2 = '//*[@id="userId"]'
xpath3 = '//*[@id="pssrd"]'
xpath4 = '//*[@id="btn_login"]'
xpath_gguromi='//*[@id="tabs2"]'
xpath5_1 = '//*[@id="grid01"]/tr['
xpath5_2 = ']/td[11]'
xpath6_1 = '//*[@id="grid01"]/tr['
xpath6_2 = ']/td[12]'
xpath7_1 = '//*[@id="grid01"]/tr['
xpath7_2= ']/td[2]/a'
xpath_time = '//*[@id="timeStatus"]'
xpath_logout = '//*[@id="header"]/div[1]/div/div/div/ul/li[4]/a'
xpath_size='//*[@id="lectPackReqGrid"]/div[2]/table/tbody/tr'

my_num=f.readline()
my_id=f.readline()
my_pw=f.readline()
f.close()
n=0
size=1
while size>0:
    parent = driver.window_handles[0]
    # chld = driver.window_handles[1]
    # driver.switch_to.window(chld)
    # driver.close()
    # driver.switch_to.window(parent)
    pyperclip.copy(my_num) # 학번 복사
    driver.find_element_by_xpath(xpath).send_keys(Keys.CONTROL, 'v') # 학번 붙여넣기
    pyperclip.copy(my_id) # id 복사
    driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v') # id 붙여넣기
    pyperclip.copy(my_pw) # 비밀번호 복사
    driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v') # 비밀번호 붙여넣기
    time.sleep(0.3)
    driver.find_element_by_xpath(xpath4).click() # 로그인 클릭
    driver.implicitly_wait(25)
    start=time.time()
    driver.find_element_by_xpath(xpath_gguromi).click() # 꾸러미 목록 클릭
    time.sleep(1)
    tt=driver.find_elements_by_xpath('//*[@id="grid01cnt"]')
    print(tt[0].text, tt[0].get_attribute('textContent'))
    size=int(tt[0].get_attribute('textContent')[0])# 수꾸에 담긴 과목 개수
    while size>0:
        driver.implicitly_wait(3)
        for i in range(1,size+1):
            limited=driver.find_element_by_xpath(xpath5_1+str(i)+xpath5_2).text
            current=driver.find_element_by_xpath(xpath6_1+str(i)+xpath6_2).text
            if limited>current:
                driver.find_element_by_xpath(xpath7_1+str(i)+xpath7_2).click()
                alert = Alert(driver)
                driver.implicitly_wait(500)
                alert.accept()
                time.sleep(0.5)
                alert.dismiss()
                print(i,datetime.datetime.now())
                n=1
                break
        if int(time.time()-start)>1000:
            n=1
        if n==1:
            driver.find_element_by_xpath(xpath_logout).click()
            break
        driver.refresh()
