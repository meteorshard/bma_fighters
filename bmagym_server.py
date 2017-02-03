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
    dict_testmember = {
            'name': 'shabi',
            'sex': 0
            }
    main_db = BMAdb()

    # main_db.insert_dict('pay_log', dictinsert)
    # main_db.insert_dict('member', dict_testmember)
    main_db.search_member_where("name='shabi'")
