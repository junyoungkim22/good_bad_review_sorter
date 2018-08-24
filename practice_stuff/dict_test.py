from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from konlpy.tag import Komoran
import time
import pickle
import sys

pkl_file = open('kodict.pkl', 'rb')
kodict = pickle.load(pkl_file)
pkl_file.close()
kodict_size = len(kodict)

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

    #driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div > div:nth-child(2) > div.Ir7OJc > div > content").click()
    komoran = Komoran()

    #kodict = dict()
    #kodict_size = 0
    review_num = 0
    word_num = 0
    hits = 0

    for item in driver.find_elements_by_class_name('UD7Dzf'):
        print(item.text)
        review_num += 1
        p_list = []
        morph_list = komoran.morphs(item.text)
        for m in morph_list:
            word_num += 1
            if m in kodict:
                hits += 1
                p_list.append(kodict[m])
            else:
                p_list.append(0)

        print(p_list)
        print("*"*80) 

    print("dict size: ", kodict_size)
    print("# of reviews: ", review_num)
    #print("# of words: ", word_num)
    print("dictionary hits / words: ", hits, " / ", word_num)
    print("percentage: ", (hits / word_num) * 100, "%")
    driver.close()
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #time.sleep(3)