# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from qichacha.settings import mysql_host,mysql_port,mysql_user,mysql_passwd,mysql_db

import MySQLdb
import hashlib
from twisted.enterprise import adbapi
class QichachaPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', host=mysql_host, port=mysql_port, user=mysql_user,
                                            passwd=mysql_passwd, db=mysql_db, charset="utf8", use_unicode=True)

    def close_sipder(self):
        self.dbpool.close()

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert, item)

    def insert(self, tx, item):
        qiye_name = item['qiye_name']
        registered_capital = item['registered_capital']
        real_capital = item['real_capital']

        insert_sql = 'insert into qichacha_info(qiye_name, registered_capital, real_capital) values (%s,%s,%s);'

        item = (
            qiye_name,
            registered_capital,
            real_capital,
        )
        print(item)
        tx.execute(insert_sql, item)

