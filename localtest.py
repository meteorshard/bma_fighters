#!usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb

def main():
    conn = MySQLdb.connect('localhost', 'root', 'mataleao0', 'bmagym')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXIST bmagym_members(Id INT PRIMARY KEY AUTO INCREASEMENT, Name VARCHAR(25))")
        cur.execute("INSERT INTO bmagym(Name) VALUES('test')")

if __name__ == '__main__':
    main()
