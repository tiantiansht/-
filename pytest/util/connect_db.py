import pymysql
import json
class connectDb():
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="interface_test",cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def search_one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return json.dumps(result)


