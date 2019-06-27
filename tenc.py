#encoding=utf-8
import unittest
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from MySQLdb import connect
import time
aa=[]
def tencent_demo():

    for i in range(1,4):
        driver = webdriver.Chrome()

        driver.get("https://careers.tencent.com/search.html?index="+str(i))

        soup = bs(driver.page_source,"lxml")

        positions = soup.find_all("h4",{"class":"recruit-title"})
        # for each_p in positions:
        #     #职位
        #     #print(each_p)
        #     pass
        citys = soup.find_all("p",{"class":"recruit-tips"})
        # #print(name)
        # #print(city)
        # for each in citys:
        #     each_city = each.find_all('span')
        #     #print(each.find_all('span')[1].get_text())
        #     #工作地点
        #     # print(each_city[1].get_text())
        #     #发布时间
        #     # print(each_city[3].get_text())
        details = soup.find_all("p",{"class":"recruit-text"})
        # for e in details:
        #     #具体详情
        #     #print(e.get_text())
        #     aa.append(e.get_text())
        for position,city,publish_time,detail in zip(positions,citys,citys,details):
            # print("职位："+position.get_text().strip()+"\n"+
            #       "工作地点："+city.find_all('span')[1].get_text().strip()+"\n"+
            #       "发布时间："+publish_time.find_all('span')[3].get_text().strip()+"\n"+
            #       "具体详情："+"\n"+detail.get_text().strip()+'\n')
            aa.append([position.get_text().strip(),city.find_all('span')[1].get_text().strip(),
                      publish_time.find_all('span')[-1].get_text().strip(),
                      detail.get_text().strip()])

    return aa





