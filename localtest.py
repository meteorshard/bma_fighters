#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from classes.bmamember import BMAMember
from classes.bmadb import BMAdb

def main():
    member_test = BMAMember(name='super dashabi', wechat_id='hahahawechat',
            sex=1)
    db_test = BMAdb()
    print(db_test.search_member(member_test))

if __name__ == '__main__':
    main()
