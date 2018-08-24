from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://play.google.com/store/apps/details?id=com.samsung.android.gametuner.thin&hl=ko&showAllReviews=true')

f = open("store_comments.txt", 'w', encoding = 'utf-8')

for item in driver.find_elements_by_class_name('UD7Dzf'):
	f.write(item.text + '\n')
    #print(item.text)
    #print("-"*80)
f.close()
driver.close()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(3)