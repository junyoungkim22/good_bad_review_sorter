from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from konlpy.tag import Komoran
import time
import pickle
import sys

train_data_pkl_file = open('train_data.pkl', 'rb')
train_label_pkl_file = open('train_label.pkl', 'rb')
dict_pkl_file = open('kodict.pkl', 'rb')

train_data = pickle.load(train_data_pkl_file)
train_label = pickle.load(train_label_pkl_file)
kodict = pickle.load(dict_pkl_file)

train_data_pkl_file.close()
train_label_pkl_file.close()
dict_pkl_file.close()

if(len(train_data) != len(train_label)):
    print("number of train data and train labels do not match")
    exit()

first = True

while True:
    print("input url, or enter quit to stop")
    url = input()

    if url == 'quit':
        driver.close()
        break

    if(first == False):
        driver.close()

    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(url + "&hl=ko")
    #driver.get('https://play.google.com/store/apps/details?id=com.kakao.talk&hl=ko&showAllReviews=true')
    driver.find_element_by_xpath('/html/body').click()

    start_time = time.time()

    while(time.time() - 15 < start_time):
        for _ in range(10):
            driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)

    komoran = Komoran()

    review_num = 0
    rank_num = 0
    hits = 0

    review_text = []
    review_rank = []
    good = 0
    bad = 0

    for item in driver.find_elements_by_class_name('UD7Dzf'):
        p_list = []
        morph_list = komoran.morphs(item.text)
        for m in morph_list:
            if m in kodict:
                p_list.append(kodict[m])
        print(p_list)
        train_data.append(p_list)
        review_num += 1

    print("-"*80)

    for i in range(review_num):
        rank = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[' + str(i+1) + ']/div/div[2]/div[1]/div[1]/div/span[1]/div/div')
        rank_string = rank.get_attribute("aria-label")
        #print(rank_string)
        if(rank_string == "별표 5개 만점에 5개를 받았습니다."):
            train_label.append(1)
            good += 1
            print('* * * * *')
        elif(rank_string == "별표 5개 만점에 4개를 받았습니다."):
            train_label.append(1)
            good += 1
            print('* * * *')
        elif(rank_string == "별표 5개 만점에 3개를 받았습니다."):
            train_label.append(0)
            bad += 1
            print('* * *')
        elif(rank_string == "별표 5개 만점에 2개를 받았습니다."):
            train_label.append(0)
            bad += 1
            print('* *')
        elif(rank_string == "별표 5개 만점에 1개를 받았습니다."):
            train_label.append(0)
            bad += 1
            print('*')
        rank_num += 1

    print("-"*80)

    print("New Review text num: ", review_num)
    print("New Review rank num: ", good + bad)
    print("GOOD: ", good)
    print("BAD: ", bad)
    print("Total number of reviews: ", len(train_data))
    print("Total number of ranks: ", len(train_label))

    if(len(train_data) != len(train_label)):
        print("num of train data and train labels do not match")
        break

    total_good = 0
    total_bad = 0

    for e in train_label:
        if e == 1:
            total_good += 1
        else:
            total_bad += 1

    print("Total Good: ", total_good)
    print("Total Bad: ", total_bad)

    train_data_output = open('train_data.pkl', 'wb')
    train_label_output = open('train_label.pkl', 'wb')

    pickle.dump(train_data, train_data_output)
    pickle.dump(train_label, train_label_output)

    train_data_output.close()
    train_label_output.close()

    first = False