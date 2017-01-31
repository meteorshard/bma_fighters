#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from classes.bmamember import BMAMember

def main():
    member_test = BMAMember(name='testA', wechat_id='testWechatID')
    member_test.serialize()

if __name__ == '__main__':
    main()
