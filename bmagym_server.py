#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

DB_INFO = {
    'host': '127.0.0.1',
    'user': 'root',
    'passwd': 'bolomma0',
    'charset': 'utf8'
}

DB_NAME = 'bmagym'

def init_db():
    try:
        conn = MySQLdb.connect(**DB_INFO)

        with conn:
            cursor = conn.cursor()

            # 如果没有数据库就新建一个
            sql = 'CREATE DATABASE IF NOT EXISTS %s' %DB_NAME
            cursor.execute(sql)
            conn.select_db(DB_NAME)

            # 如果没有pay_log表就新建一个
            """ 表结构说明：
            l_id: log id
            u_id: 付款用户id
            pay_time: 付款时间
            buy_duration: 本次付款所购买的时长
            buy_count: 本次付款所购买的次数
            event_id: 生效的活动id
            recommended_by: 推荐人/会籍顾问id
            comment: 备注
            """
            sql = (
                'CREATE TABLE IF NOT EXISTS pay_log('
                    'l_id int NOT NULL AUTO_INCREMENT,'
                    'u_id int NOT NULL,'
                    'pay_time datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,'
                    'buy_duration smallint,'
                    'buy_count smallint,'
                    'event_id int,'
                    'recommended_by int,'
                    'comment text,'
                    'PRIMARY KEY(l_id)'
                ')'
            )
            cursor.execute(sql)
            conn.commit()
    except MySQLdb.Error, e:
        print('MySQL Error [%d]: %s' %(e.args[0], e.args[1]))
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    init_db()
