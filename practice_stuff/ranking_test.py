from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from konlpy.tag import Komoran
import time
import pickle
import sys

while True:
    print("input url, or enter quit to stop")
    url = input()

    if url == 'quit':
        break

    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(url)
    #driver.get('https://play.google.com/store/apps/details?id=com.kakao.talk&hl=ko&showAllReviews=true')
    driver.find_element_by_xpath('/html/body').click()

    start_time = time.time()

    while(time.time() - 15 < start_time):
        for _ in range(10):
            driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)

    review_num = 0
    hits = 0

    review_text = []
    review_rank = []
    good = 0
    bad = 0

    for item in driver.find_elements_by_class_name('UD7Dzf'):
        review_text.append(item.text)
        review_num += 1

    for i in range(len(review_text)):
        rank = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[' + str(i+1) + ']/div/div[2]/div[1]/div[1]/div/span[1]/div/div')
        rank_string = rank.get_attribute("aria-label")
        #print(rank_string)
        if(rank_string == "별표 5개 만점에 5개를 받았습니다."):
            review_rank.append(5)
            good += 1
        elif(rank_string == "별표 5개 만점에 4개를 받았습니다."):
            review_rank.append(4)
            good += 1
        elif(rank_string == "별표 5개 만점에 3개를 받았습니다."):
            review_rank.append(3)
            bad += 1
        elif(rank_string == "별표 5개 만점에 2개를 받았습니다."):
            review_rank.append(2)
            bad += 1
        elif(rank_string == "별표 5개 만점에 1개를 받았습니다."):
            review_rank.append(1)
            bad += 1

    for i in range(len(review_rank)):
        print(review_text[i])
        print("- "*40)
        print("RANK: ", review_rank[i])
        print("*"*80)

    print("Review text num: ", len(review_text))
    print("Review rank num: ", len(review_rank))
    print("GOOD: ", good)
    print("BAD: ", bad)
    driver.close()
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(3)