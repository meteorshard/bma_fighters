#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from classes.bmamember import BMAMember
from classes.bmadb import BMAdb

def main():
    member_test = BMAMember(u_id=2)
    db_test = BMAdb()
    # print(repr(db_test.search_member(member_test)))
    for each_member in db_test.search_member(member_test):
        print(repr(each_member.serialize()))

if __name__ == '__main__':
    main()
