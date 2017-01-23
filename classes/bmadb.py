#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

class BMAdb(object):

    DB_INFO = {
        'host': '127.0.0.1',
        'user': 'root',
        'passwd': 'bolomma0',
        'charset': 'utf8'
    }

    DB_NAME = 'bmagym'

    def __init__(self):
        """ 初始化数据库
        1. 建立数据库bmagym
        2. 建立数据表pay_log，用于存储付款log
            表结构说明：
                l_id: log id
                u_id: 付款用户id
                pay_time: 付款时间
                buy_duration: 本次付款所购买的时长
                buy_count: 本次付款所购买的次数
                event_id: 生效的活动id
                recommended_by: 推荐人/会籍顾问id
                comment: 备注

        3. 建立数据表members，用于存储会员信息
            表结构说明：
                u_id: 用户id
                name: 名字
                wechat_id: 微信id
                sex: 性别 0-female 1-male
                tel: 电话
                paper_type: 证件类型
                paper_number: 证件号码
                email: 邮箱
                birthday: 生日
                duration left: 剩余时间
                count left: 剩余次数
                comment: 备注

        4. 建立数据表events，用于存储活动信息
        """
        try:
            conn = MySQLdb.connect(**self.DB_INFO)

            with conn:
                cursor = conn.cursor()

                # 如果没有数据库就新建一个
                sql = 'CREATE DATABASE IF NOT EXISTS %s' %self.DB_NAME
                cursor.execute(sql)
                conn.select_db(self.DB_NAME)

                # 如果没有pay_log表就新建一个
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

                # 如果没有members表就建一个
                sql = (
                    'CREATE TABLE IF NOT EXISTS members('
                        'u_id int NOT NULL AUTO_INCREMENT,'
                        'name varchar(30) NOT NULL,'
                        'wechat_id varchar(30) NOT NULL,'
                        'sex tinyint(1) NOT NULL,'
                        'tel varchar(13),'
                        'paper_type varchar(10),'
                        'paper_number varchar(30),'
                        'email varchar(30),'
                        'birthday date,'
                        'duration_left smallint,'
                        'count_left smallint,'
                        'comment text,'
                        'PRIMARY KEY(u_id)'
                    ')'
                )
                cursor.execute(sql)

                conn.commit()

        except MySQLdb.Error, e:
            # 如果出错就输出错误消息
            print('MySQL Error [%d]: %s' %(e.args[0], e.args[1]))

        finally:
            cursor.close()
            conn.close()

    def insert_log(self, )
