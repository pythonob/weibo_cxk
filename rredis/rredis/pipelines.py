# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class RredisPipeline(object):

    def __init__(self):
        self.HOST = '192.168.100.110'
        self.PORT = 3306
        self.USER = 'mysql'
        self.PASSWD = 'P@ssw0rd'

        self.conn = pymysql.connect(host=self.HOST, port=self.PORT, user=self.USER, passwd=self.PASSWD,
                                    db="weibo", charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into items ( u_id, u_name, gender, fwd_text, follows, followers, device, description,fwd_id)  " \
              "values ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            res = self.cursor.execute(sql, args=(item["u_id"], item["u_name"], item["gender"], item["fwd_text"], item["follows"],
                item["followers"], item["device"], item["desc"], item["fwd_id"]))
            if res == 1:
                self.conn.commit()

        except Exception as e:
            print(e)
            pass
        return item

    def close_spider(self):
        self.cursor.close()
        self.conn.close()



def write_log(item):
    with open ("error.txt","a+") as f:
        for val in item.values():
            f.write(str(val)+",")