#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

db_info = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'mataleao0',
    'charset': 'utf8'
}

def init_db():
    try:
        conn = MySQLdb.connect(**db_info)
        with conn:
            cur = conn.cursor()
            db_name = 'bmagym'
            sql = 'CREATE DATABASE IF NOT EXISTS %s' %db_name
            cur.execute(sql)
            conn.select_db(db_name)
            sql = ('CREATE TABLE IF NOT EXISTS pay_log('
                    'l_id int NOT NULL AUTO_INCREMENT,'
                    'u_id int NOT NULL,'
                    'pay_time datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,'
                    'pay_amount mediumint,'
                    'buy_duration smallint,'
                    'event_id int,'
                    'discount tinyint(3),'
                    'comment text(200),'
                    'PRIMARY KEY(l_id)'
                   ')')
            cur.execute(sql)
            conn.commit()
    except MySQLdb.Error, e:
        print('MySQL Error [%d]: %s' %(e.args[0], e.args[1]))
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    init_db()