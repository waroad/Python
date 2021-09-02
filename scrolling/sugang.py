import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyclip as pyperclip

driver = webdriver.Chrome("C:/chromedriver.exe")  # 크롬창 켜기
driver.get("https://sugang.knu.ac.kr/Sugang/comm/support/login/loginForm.action?redirUrl=%2FSugang%2Fcour%2FlectReq%2FonlineLectReq%2Flist.action") # 사이트 접속
p = driver.current_window_handle
f = open("id.txt", "r")
xpath = '//*[@id="user.stu_nbr"]'
xpath2 = '//*[@id="user.usr_id"]'
xpath3 = '//*[@id="user.passwd"]'
xpath4 = '//*[@id="loginForm"]/table/tbody/tr[4]/td/button[1]'
xpath5_1 = '//*[@id="lectPackReqGrid_'
xpath5_2 = '"]/td[8]'
xpath6_1 = '//*[@id="lectPackReqGrid_'
xpath6_2 = '"]/td[9]'
xpath7 = '//*[@id="lectPackReqGrid_0"]/td[11]'
xpath_time = '//*[@id="timeStatus"]'
xpath_logout = '//*[@id="logout"]/button[1]'
xpath_size='//*[@id="lectPackReqGrid"]/div[2]/table/tbody/tr'

my_num=f.readline()
my_id=f.readline()
my_pw=f.readline()
f.close()
n=0
while n==0:
    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)
    driver.close()
    driver.switch_to.window(parent)
    pyperclip.copy(my_num) # 학번 복사
    driver.find_element_by_xpath(xpath).send_keys(Keys.CONTROL, 'v') # 학번 붙여넣기
    pyperclip.copy(my_id) # id 복사
    driver.find_element_by_xpath(xpath2).send_keys(Keys.CONTROL, 'v') # id 붙여넣기
    pyperclip.copy(my_pw) # 비밀번호 복사
    driver.find_element_by_xpath(xpath3).send_keys(Keys.CONTROL, 'v') # 비밀번호 붙여넣기
    driver.find_element_by_xpath(xpath4).click() # 로그인 클릭
    driver.implicitly_wait(25)
    start=time.time()
    size=len(driver.find_elements_by_xpath(xpath_size)) # 수꾸에 담긴 과목 개수
    while True:
        driver.implicitly_wait(3)
        for i in range(size-1):
            limited=driver.find_element_by_xpath(xpath5_1+str(i)+xpath5_2).text
            current=driver.find_element_by_xpath(xpath6_1+str(i)+xpath6_2).text
            if limited>current:
                driver.find_element_by_xpath(xpath7).click()
                n=1
                break
        if n==1:
            break
        driver.refresh()
        cur=int(time.time()-start)
        if cur>1000:
            driver.find_element_by_xpath(xpath_logout).click()
            break
