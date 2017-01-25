#!usr/bin/python
# -*- coding: utf-8 -*-

from classes.bmadb import BMAdb

if __name__ == '__main__':
    dictinsert = {
            'u_id': 546456,
            'buy_duration': 30,
            'buy_count': 10,
            'comment': 'test log'
            }
    main_db = BMAdb()
    main_db.insert_dict('pay_log', dictinsert)
