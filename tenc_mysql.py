#encoding=utf-8
from MySQLdb import connect

from tencent import tenc


def tencen_mysql():
    try:
        conn = connect(host="localhost",port=3306,db="tencent",user="root",passwd="123456")

        cursor = conn.cursor()

        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS TENCENT")

        # 创建数据表SQL语句
        sql = """CREATE TABLE TENCENT (
                  ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                 POSITION VARCHAR(100),
                 LOCATION VARCHAR(100),
                 PUBLISHTTIME VARCHAR(100),
                 DETAILS VARCHAR(2000)
                  )
                 """

        cursor.execute(sql)

        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
aa = tenc.tencent_demo()
def tencent_add():
    for each in aa:
        try:
            conn = connect(host="localhost", port=3306, db="tencent", user="root", passwd="123456")

            cursor = conn.cursor()
            #插入sql
            sql = "insert into tencent(id,position,location,publishttime,details) VALUES (0,'"+each[0]+"','"+each[1]+"','"+each[2]+"','"+each[3]+"')"

            #print(sql)
            cursor.execute(sql)

            cursor.close()
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
tencen_mysql()
tencent_add()