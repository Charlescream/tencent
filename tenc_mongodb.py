#encoding=utf-8
from pymongo import *

from tencent import tenc


def setup_mongo():
    #获得客户端，建立连接
    client = MongoClient('mongodb://admin:123456@localhost:27017/py3')
    #切换数据库
    db = client.py3
    #删除如果有tencent
    db.tencent.drop()
    # 获得集合
    info=db.tencent

    #获得对象aa
    aa = tenc.tencent_demo()

    for each in aa:
        info.insert_one({'position':each[0],'location':each[1],'publishttime':each[2],'details':each[3]})
    #查询目前的tencent
    # cursor = db.tencent.find()
    #
    # for each in cursor:
    #     print(each)

setup_mongo()
