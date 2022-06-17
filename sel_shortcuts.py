#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

url_login ='https://www.uniqrank.com/admin', 
temp_username ='temp@thomsondigital.com', 
password ='P@ssw0rd', 
user_xpath = '//*[@id="email"]', 
pass_xpath = '//*[@id="password"]', 
login_btn_x = '/html/body/div[4]/div/div/div/div/div[2]/form/div[4]/button'


# This starts browser
# driver_path = r'C:\Users\USER\Desktop\chrmDrvrDir\chromedriver.exe'
# driver = webdriver.Chrome(driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Click an element after t second
def click(path, wait=0.5):
    sleep(wait)
    try:
        driver.find_element_by_xpath(path).click()
    except:
        sleep(2)
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(path))
    return


# Fill data to an input element after t second
def fill(path, val, wait=0.5):
    sleep(wait)
    driver.find_element_by_xpath(path).send_keys(val)
    return
    

# Login temp role if role=2 (for SME select role as 3 and so on)
def login_uniq(url_login='https://www.uniqrank.com/admin', username='temp@thomsondigital.com', password='P@ssw0rd', role=2, driver=driver, fill=fill, click=click, user_xpath = '//*[@id="email"]', pass_xpath = '//*[@id="password"]', login_btn_x = '/html/body/div[4]/div/div/div/div/div[2]/form/div[4]/button'):  
#     driver()
    driver.get(url_login)
    fill(user_xpath,username)
    fill(pass_xpath, password)
    role_xpath = f'//*[@id="usertype"]/option[{role}]'
    click(role_xpath)
    click(login_btn_x)
    return

