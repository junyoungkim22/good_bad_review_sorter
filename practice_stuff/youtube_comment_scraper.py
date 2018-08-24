from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
#driver.implicitly_wait(3)
driver.get('https://www.youtube.com/watch?v=GKiORPfvMx4')

driver.implicitly_wait(0)
driver.find_element_by_xpath('/html/body').click()

while True:
    try:
        driver.find_element_by_id('content-text')
        break
    except:
        driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)

driver.implicitly_wait(3)


for item in driver.find_elements_by_id('content-text'):
    print(item.text)
    print("-"*80)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(3)