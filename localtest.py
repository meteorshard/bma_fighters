#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
from classes.bmamember import BMAMember
from classes.bmadb import BMAdb

def test_update():
    member_test = BMAMember(nickname='杜姆斯呆', realname='周潇', sex=2, tel=18601127903, comment='大傻逼')
    member_test.birthday = datetime.date(1985, 7, 13) 
    db_test = BMAdb()
    db_test.update_member(2, member_test)

def test_insert():
    members=[]
    for i in range(10):
        member_test_insert = BMAMember()
        members.append(member_test_insert)
    db_test = BMAdb()
    for member in members:
        db_test.insert_member(member)

def main():
    # test_insert()
    test_update()

if __name__ == '__main__':
    main()
