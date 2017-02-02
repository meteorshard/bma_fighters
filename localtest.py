#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from classes.bmamember import BMAMember
from classes.bmadb import BMAdb

def main():
    member_test = BMAMember(sex=1, tel=18601127903, comment='大傻逼')
    db_test = BMAdb()
    db_test.update_member(2, member_test)

if __name__ == '__main__':
    main()
