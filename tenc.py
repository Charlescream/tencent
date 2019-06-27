#encoding=utf-8
import unittest
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from MySQLdb import connect
import time
#创建一个集合
aa=[]
def tencent_demo():

    for i in range(1,4):#爬取前3页
        #谷歌浏览器
        driver = webdriver.Chrome()

        driver.get("https://careers.tencent.com/search.html?index="+str(i))

        soup = bs(driver.page_source,"lxml")
        #职位
        positions = soup.find_all("h4",{"class":"recruit-title"})

        #城市和时间
        citys = soup.find_all("p",{"class":"recruit-tips"})

        #具体细节
        details = soup.find_all("p",{"class":"recruit-text"})

        for position,city,publish_time,detail in zip(positions,citys,citys,details):
            # print("职位："+position.get_text().strip()+"\n"+
            #       "工作地点："+city.find_all('span')[1].get_text().strip()+"\n"+
            #       "发布时间："+publish_time.find_all('span')[3].get_text().strip()+"\n"+
            #       "具体详情："+"\n"+detail.get_text().strip()+'\n')
            aa.append([position.get_text().strip(),city.find_all('span')[1].get_text().strip(),
                      publish_time.find_all('span')[-1].get_text().strip(),
                      detail.get_text().strip()])

    return aa





